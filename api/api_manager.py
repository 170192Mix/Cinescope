import requests
from typing import Optional

from constants import API_BASE, HEADERS
from api.api_movies import MoviesAPI
from api.auth_api import AuthAPI
from api.user_api import UserAPI


class ApiManager:
    """
    Единая точка доступа к API-клиентам на общей requests.Session()
    """
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update(HEADERS)

        self.auth_api = AuthAPI(self.session)
        self.user_api = UserAPI(self.session)

    @property
    def movies_api(self) -> MoviesAPI:
        return MoviesAPI(session=self.session, base_url=API_BASE, headers=HEADERS)

    def set_bearer(self, token: str) -> None:
        self.session.headers["Authorization"] = f"Bearer {token}"

    def login_admin(self, email: str, password: str) -> str:
        """
        Авторизует и сразу ставит токен в сессию
        Возвращает сам токен
        """
        resp = self.auth_api.login(email=email, password=password, expected_status=200)
        token = resp.json().get("accessToken") or resp.json().get("token")
        if not token:
            raise RuntimeError("Не получили токен от auth-сервиса")
        self.set_bearer(token)
        return token