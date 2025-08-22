class TestAuthAPI:
    def test_register_user(self, api_manager, test_user):
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)
        data = response.json()

        assert data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in data, "ID пользователя отсутствует в ответе"
        assert "roles" in data, "Роли пользователя отсутствуют в ответе"
        assert "USER" in data["roles"], "Роль USER должна быть у пользователя"

    def test_register_and_login_user(self, api_manager, registered_user):
        """
        Тест на авторизацию.
        """
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        resp = api_manager.auth_api.login_user(login_data)
        data = resp.json()

        assert resp.status_code in (200, 201)
        assert "accessToken" in data, "Токен доступа отсутствует в ответе"
        assert data["user"]["email"] == registered_user["email"], "Email не совпадает"
