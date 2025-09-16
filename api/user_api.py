from custom_requester.custom_requester import CustomRequester
from constants import API_BASE, USER_ENDPOINT

class UserAPI(CustomRequester):
    """Клиент для /users на базовом API"""
    def __init__(self, session):
        super().__init__(session=session, base_url=API_BASE)

    def get_user_info(self, user_id, expected_status: int = 200):
        return self.send_request(
            method="GET",
            endpoint=f"{USER_ENDPOINT}/{user_id}",
            expected_status=expected_status,
        )

    def delete_user(self, user_id, expected_status: int = 204):
        return self.send_request(
            method="DELETE",
            endpoint=f"{USER_ENDPOINT}/{user_id}",
            expected_status=expected_status,
        )