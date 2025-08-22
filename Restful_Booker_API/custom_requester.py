import requests

class CustomRequester:
    def __init__(self, session: requests.Session, base_url: str):
        self.session = session
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }

    def send_request(self, method, endpoint, data=None, expected_status=200, need_logging=True):
        """
        Универсальный метод для отправки запросов.
        :param method: HTTP метод (GET, POST, PUT, DELETE и т.д.).
        :param endpoint: Эндпоинт (например, "/login").
        :param data: Тело запроса (JSON-данные).
        :param expected_status: Ожидаемый статус-код (по умолчанию 200).
        :param need_logging: Флаг для логирования (по умолчанию True).
        :return: Объект ответа requests.Response.
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, json=data, headers=self.headers)

        if need_logging:
            self.log_request_and_response(response)

        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status}")

        return response

    def _update_session_headers(self, session, **kwargs):
        """
        Обновление заголовков сессии.
        """
        self.headers.update(kwargs)  # Обновляем базовые заголовки
        session.headers.update(self.headers)  # Применяем к текущей сессии

    def log_request_and_response(self, response):
        """
        Логирование запроса и ответа.
        """
        print(f"Request URL: {response.request.url}")
        print(f"Request Method: {response.request.method}")
        print(f"Request Headers: {response.request.headers}")
        print(f"Request Body: {response.request.body}")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {response.text}")
