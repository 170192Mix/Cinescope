import requests
from typing import Optional

from constants import API_BASE, HEADERS
from api.api_movies import MoviesAPI
from api.auth_api import AuthAPI
from api.user_api import UserAPI


class ApiManager:
    """Единая точка доступа к API-клиентам на общей requests.Session()."""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update(HEADERS)

        # единообразно создаём клиентов один раз
        self.auth_api = AuthAPI(self.session)
        self.user_api = UserAPI(self.session)
        self.movies_api = MoviesAPI(session=self.session, base_url=API_BASE, headers=HEADERS)

    def set_bearer(self, token: str) -> None:
        self.session.headers["Authorization"] = f"Bearer {token}"

    def login_admin(self, email: str, password: str) -> str:
        """Авторизует админа и проставляет Bearer-токен в общую session."""
        token = self.auth_api.authenticate(email=email, password=password, expected_status=200)
        self.set_bearer(token)
        return token