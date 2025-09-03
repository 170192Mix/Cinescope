
from custom_requester.custom_requester import CustomRequester
from constants import BASE_URL, USER_ENDPOINT

class UserAPI(CustomRequester):
    """
    Методы управления пользователем.
    """
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)

    def get_user_info(self, user_id, expected_status=200):
        return self.send_request(
            method="GET",
            endpoint=f"{USER_ENDPOINT}/{user_id}",
            expected_status=expected_status
        )

    def delete_user(self, user_id, expected_status=204):
        return self.send_request(
            method="DELETE",
            endpoint=f"{USER_ENDPOINT}/{user_id}",
            expected_status=expected_status
        )

    # опционально сахар
    def clean_up_user(self, user_id, expected_status=204):
        return self.delete_user(user_id, expected_status)