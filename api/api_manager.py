from constants import API_BASE, HEADERS
from api.movies_api import MoviesAPI
from .auth_api import AuthAPI
from .user_api import UserAPI

class ApiManager:
    """
    Держит инстансы API-классов на одной сессии.
    """
    def __init__(self, session):
        self.session = session
        self.auth_api = AuthAPI(session)
        self.user_api = UserAPI(session)

class ApiManager:
    def __init__(self, session):
        self.session = session
        # уже было: self.auth_api = AuthAPI(...)

    @property
    def movies_api(self) -> MoviesAPI:

        return MoviesAPI(session=self.session, base_url=API_BASE, headers=HEADERS)