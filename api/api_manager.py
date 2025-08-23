
import requests # Импортируем библиотеку requests

from constants import API_BASE, HEADERS # Тянем базовый URL и дефолтные заголовки
from api.movies_api import MoviesAPI # Импортируем конкретные клиенты API
from api.auth_api import AuthAPI
from api.user_api import UserAPI

class ApiManager:
    """
    Единая точка доступа к API-клиентам, все работают на одной requests.Session()
    """
    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()

        self.auth_api = AuthAPI(self.session) # Создаем клиент авторизации
        self.user_api = UserAPI(self.session) if 'UserAPI' in globals() else None # Защитная конструкция на случай, если класса UserAPI нет

    @property
    def movies_api(self) -> MoviesAPI: # Свойство, которое каждый вызов возвращает новый экземпляр MoviesAPI

        return MoviesAPI(session=self.session, base_url=API_BASE, headers=HEADERS)
