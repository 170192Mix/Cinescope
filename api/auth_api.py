
from constants import CINESCOPE_AUTH_BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT # Импортируешь конфигурацию
from custom_requester.custom_requester import CustomRequester # Базовый класс


class AuthAPI(CustomRequester): # Специализированный клиент, позволяет не дублировать низкоуровневую работу с HTTP
    """
    Класс для работы с аутентификацией Cinescope
    """

    def __init__(self, session):
        # важно: берём базовый URL из constants
        super().__init__(session=session, base_url=CINESCOPE_AUTH_BASE_URL)

    def register_user(self, user_data, expected_status=201): # Метод регистрации
        # сервер отвечает 201 на успешную регистрацию
        return self.send_request(
            "POST",
            REGISTER_ENDPOINT,
            json=user_data,
            expected_status=expected_status
        )

    def login_user(self, login_data, expected_status=200):
        # логин возвращает 200
        return self.send_request(
            "POST",
            LOGIN_ENDPOINT,
            json=login_data,
            expected_status=expected_status
        )

    def login(self, email: str, password: str, expected_status=200):
        return self.login_user({"email": email, "password": password}, expected_status=expected_status)

    def login(self, email: str, password: str, expected_status=200):
        return self.send_request(
            "POST", LOGIN_ENDPOINT,
            json={"email": email, "password": password},
            expected_status=expected_status
        )

    def register(self, email: str, password: str, fullName: str, roles=None, expected_status=(201, 409)):
        roles = roles or ["USER"]
        payload = {
            "email": email,
            "password": password,
            "passwordRepeat": password,
            "fullName": fullName,
            "roles": roles,
        }
        return self.send_request("POST", REGISTER_ENDPOINT, json=payload, expected_status=expected_status)