import json
import logging
import os
from collections.abc import Iterable

class CustomRequester:
    base_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    def __init__(self, session, base_url, headers=None):
        self.session = session
        self.base_url = base_url.rstrip("/")
        # держим базовые заголовки в session, чтобы не плодить
        self.session.headers.update({**self.base_headers, **(headers or {})})

        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            _h = logging.StreamHandler()
            _h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
            self.logger.addHandler(_h)

    @property
    def headers(self) -> dict:
        """Совместимость: отдаём текущие заголовки из session."""
        return self.session.headers

    # удобные обёртки
    def get(self, endpoint, *, expected_status=200, params=None, headers=None, **kwargs):
        return self.send_request("GET", endpoint, expected_status=expected_status, params=params, headers=headers, **kwargs)

    def post(self, endpoint, *, json=None, data=None, expected_status=200, headers=None, files=None, **kwargs):
        return self.send_request("POST", endpoint, json=json, data=data, expected_status=expected_status, headers=headers, files=files, **kwargs)

    def put(self, endpoint, *, json=None, data=None, expected_status=200, headers=None, files=None, **kwargs):
        return self.send_request("PUT", endpoint, json=json, data=data, expected_status=expected_status, headers=headers, files=files, **kwargs)

    def patch(self, endpoint, *, json=None, data=None, expected_status=200, headers=None, files=None, **kwargs):
        return self.send_request("PATCH", endpoint, json=json, data=data, expected_status=expected_status, headers=headers, files=files, **kwargs)

    def delete(self, endpoint, *, expected_status=200, headers=None, **kwargs):
        return self.send_request("DELETE", endpoint, expected_status=expected_status, headers=headers, **kwargs)

    # единая точка отправки
    def send_request(
        self, method, endpoint, *, json=None, data=None, expected_status=200,
        need_logging=True, params=None, headers=None, files=None
    ):
        # нормализуем endpoint
        if endpoint.startswith("http"):
            url = endpoint
        else:
            if not endpoint.startswith("/"):
                endpoint = "/" + endpoint
            url = f"{self.base_url}{endpoint}"

        req_headers = {**self.session.headers, **(headers or {})}

        response = self.session.request(
            method=method,
            url=url,
            headers=req_headers,
            params=params,
            json=json,   # JSON идёт сюда
            data=data,   # form/bytes сюда
            files=files
        )

        if need_logging:
            self._log_request_and_response(response)

        def _ok(status, expected):
            if isinstance(expected, Iterable) and not isinstance(expected, (str, bytes)):
                return status in expected
            return status == expected

        if not _ok(response.status_code, expected_status):
            raise AssertionError(f"{method} {url} -> {response.status_code}, ожидалось {expected_status}")

        return response

    def update_headers(self, **kwargs):
        # правим только session.headers
        self.session.headers.update(kwargs)

    def _log_request_and_response(self, response):
        try:
            req = response.request
            GREEN = '\033[32m'; RED = '\033[31m'; RESET = '\033[0m'
            headers = " \\\n".join([f"-H '{h}: {v}'" for h, v in req.headers.items()])

            body = ""
            if getattr(req, "body", None):
                b = req.body
                if isinstance(b, bytes):
                    b = b.decode("utf-8", errors="ignore")
                body = f"-d '{b}' \n" if b != '{}' else ''

            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"

            self.logger.info(f"\n{'='*40} REQUEST {'='*40}")
            self.logger.info(f"{GREEN}{full_test_name}{RESET}\n"
                             f"curl -X {req.method} '{req.url}' \\\n{headers} \\\n{body}")

            resp_text = response.text
            try:
                resp_text = json.dumps(response.json(), indent=4, ensure_ascii=False)
            except Exception:
                pass

            color = GREEN if response.ok else RED
            self.logger.info(f"\n{'='*40} RESPONSE {'='*40}")
            self.logger.info(f"\tSTATUS_CODE: {color}{response.status_code}{RESET}\n\tDATA:\n{resp_text}")
            self.logger.info(f"{'='*80}\n")
        except Exception as e:
            self.logger.error(f"Logging failed: {type(e)} - {e}")
