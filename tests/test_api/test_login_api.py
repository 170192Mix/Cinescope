
from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT

class TestLoginAPI:
    def test_successful_login(self, cinescope, test_user):
        # Регистрация: допускаем 201 (успех) или 409 (уже зарегистрирован)
        register_url = f"{cinescope.base_url}{REGISTER_ENDPOINT}"
        reg_resp = cinescope.session.post(register_url, json=test_user, headers=cinescope.headers)
        assert reg_resp.status_code in (201, 409), f"Регистрация не удалась: {reg_resp.status_code} {reg_resp.text}"

        # Логин
        login_url = f"{cinescope.base_url}{LOGIN_ENDPOINT}"
        login_data = {
            "email": test_user["email"],
            "password": test_user["password"],
        }
        login_resp = cinescope.session.post(login_url, json=login_data, headers=cinescope.headers)
        print("Ответ логина:", login_resp.status_code, login_resp.text)
        assert login_resp.status_code in (200, 201), "Некорректный статус код при логине"
        data = login_resp.json()
        assert "accessToken" in data
        assert "user" in data
        assert data["user"]["email"] == test_user["email"]
