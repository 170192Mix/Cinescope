import json
import logging
import os

class CustomRequester:
    """
    Универсальный HTTP-клиент поверх requests.Session с логированием.
    Ожидает, что session уже создана снаружи (фикстурой).
    """
    base_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    def __init__(self, session, base_url, headers=None):  # добавил headers
        self.session = session
        self.base_url = base_url.rstrip("/")
        self.headers = {**self.base_headers, **(headers or {})}  # ← объединили
        self.session.headers.update(self.headers)

        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            _h = logging.StreamHandler()
            _h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
            self.logger.addHandler(_h)

    # ——— Удобные методы ———
    def get(self, endpoint, expected_status=200, params=None, **kwargs):
        return self.send_request("GET", endpoint, expected_status=expected_status, params=params, **kwargs)

    def post(self, endpoint, data=None, expected_status=200, **kwargs):
        # если передаёшь JSON, используй json=data
        return self.send_request("POST", endpoint, data=data, expected_status=expected_status, **kwargs)

    def put(self, endpoint, data=None, expected_status=200, **kwargs):
        return self.send_request("PUT", endpoint, data=data, expected_status=expected_status, **kwargs)

    def patch(self, endpoint, data=None, expected_status=200, **kwargs):
        return self.send_request("PATCH", endpoint, data=data, expected_status=expected_status, **kwargs)

    def delete(self, endpoint, expected_status=200, **kwargs):
        return self.send_request("DELETE", endpoint, expected_status=expected_status, **kwargs)

    # ——— Базовый универсальный метод ———
    def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True, params=None, headers=None, json=None):
        """
        endpoint может быть либо абсолютным URL, либо относительным ("/booking").
        Если передаёшь 'json' — он имеет приоритет над 'data'.
        """
        url = endpoint if endpoint.startswith("http") else f"{self.base_url}{endpoint}"
        # если явно передали headers — не теряем базовые
        req_headers = {**self.headers, **(headers or {})}

        # Если не передан json, а передан data — решаем, что это JSON-тело
        # (в тестах удобнее всегда отправлять через json=payload)
        if json is None and data is not None:
            json = data
            data = None

        response = self.session.request(
            method=method,
            url=url,
            headers=req_headers,
            params=params,
            json=json,
            data=data,
        )

        if need_logging:
            self._log_request_and_response(response)

        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status}")

        return response

    def update_headers(self, **kwargs):
        """Обновить хедеры как на объекте, так и в сессии (например, добавить Authorization)."""
        self.headers.update(kwargs)
        self.session.headers.update(self.headers)

    # ——— Логирование ———
    def _log_request_and_response(self, response):
        if not hasattr(self, "logger"):
            self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
            self.logger.setLevel(logging.INFO)
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
            self.logger.info(
                f"{GREEN}{full_test_name}{RESET}\n"
                f"curl -X {req.method} '{req.url}' \\\n"
                f"{headers} \\\n"
                f"{body}"
            )

            # красивый вывод JSON-ответа, если это JSON
            resp_text = response.text
            try:
                resp_text = json.dumps(response.json(), indent=4, ensure_ascii=False)
            except Exception:
                pass

            color = GREEN if response.ok else RED
            self.logger.info(f"\n{'='*40} RESPONSE {'='*40}")
            self.logger.info(
                f"\tSTATUS_CODE: {color}{response.status_code}{RESET}\n"
                f"\tDATA:\n{resp_text}"
            )
            self.logger.info(f"{'='*80}\n")
        except Exception as e:
            self.logger.error(f"Logging failed: {type(e)} - {e}")