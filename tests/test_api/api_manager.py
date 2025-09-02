
import requests
from typing import Optional

from constants import API_BASE, HEADERS
from tests.test_api.api_movies import MoviesAPI
from api.auth_api import AuthAPI
from api.user_api import UserAPI

class ApiManager:
    """
    Единая точка доступа к API-клиентам на общей requests.Session()
    """
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        # Базовые заголовки на всю сессию
        self.session.headers.update(HEADERS)

        self.auth = AuthAPI(self.session)
        self.auth_api = self.auth
        self.user = UserAPI(self.session)

        @property
        def auth_api(self):
            return self.auth

        @property
        def movies_api(self):
            return self.movies

    @property
    def movies(self) -> MoviesAPI:
        # Если MoviesAPI умеет работать только с session
        # Если ему нужен base_url/headers — передаём (как у тебя сейчас)
        return MoviesAPI(session=self.session, base_url=API_BASE, headers=HEADERS)

    # Удобный хелпер: логин и установка токена в общий session
    def set_bearer(self, token: str) -> None:
        self.session.headers["Authorization"] = f"Bearer {token}"

    def login_admin(self, email: str, password: str) -> str:
        """
        Авторизует и сразу ставит токен в сессию.
        Возвращает сам токен
        """
        resp = self.auth.login(email=email, password=password, expected_status=200)  # подгони под свой AuthAPI
        token = resp.json().get("accessToken") or resp.json().get("token")
        if not token:
            raise RuntimeError("Не получили токен от auth-сервиса")
        self.set_bearer(token)
