from pythonProject.tests.test_api.auth_api import AuthAPI
from pythonProject.tests.test_api.user_api import UserAPI

class ApiManager:
    """
    Держит инстансы API-классов на одной сессии.
    """
    def __init__(self, session):
        self.session = session
        self.auth_api = AuthAPI(session)
        self.user_api = UserAPI(session)
