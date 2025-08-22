
import requests

from constants import API_BASE, HEADERS
from api.movies_api import MoviesAPI
from api.auth_api import AuthAPI
from api.user_api import UserAPI  # если есть такой класс

class ApiManager:
    """
    Единая точка доступа к API-клиентам, все работают на одной requests.Session()
    """
    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()

        self.auth_api = AuthAPI(self.session)
        self.user_api = UserAPI(self.session) if 'UserAPI' in globals() else None

    @property
    def movies_api(self) -> MoviesAPI:

        return MoviesAPI(session=self.session, base_url=API_BASE, headers=HEADERS)
