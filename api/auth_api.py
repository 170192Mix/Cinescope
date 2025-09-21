from constants import CINESCOPE_AUTH_BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT
from custom_requester.custom_requester import CustomRequester


class AuthAPI(CustomRequester):
    """Аутентификация Cinescope на общей session"""

    def __init__(self, session):
        super().__init__(session=session, base_url=CINESCOPE_AUTH_BASE_URL)

    def login(self, login_data: dict, expected_status=200):
        """Базовый логин: принимает dict {'email': ..., 'password': ...}"""
        return self.send_request(
            "POST",
            LOGIN_ENDPOINT,
            json=login_data,
            expected_status=expected_status,
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

    # для совместимости со старыми тестами
    def register_user(self, user_data: dict, expected_status=201):
        """Совместимость: принимает готовый dict с полями регистраци"""
        return self.send_request(
            "POST",
            REGISTER_ENDPOINT,
            json=user_data,
            expected_status=expected_status,
        )

    def login_user(self, login_data: dict, expected_status=201):
        """Совместимость: принимает dict {'email': ..., 'password': ...}"""
        return self.login(login_data, expected_status=expected_status)


    def authenticate(self, email: str, password: str, expected_status=200) -> str:
        """Логин кладёт Bearer-токен в headers общей session. Возвращает токен"""
        resp = self.login({"email": email, "password": password}, expected_status=expected_status)
        data = resp.json()
        token = data.get("accessToken") or data.get("token")
        if not token:
            raise RuntimeError("Не получили токен от auth-сервиса")
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        return token