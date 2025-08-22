
import pytest
import requests
from faker import Faker
from constants import CINESCOPE_AUTH_BASE_URL, HEADERS, LOGIN_ENDPOINT, REGISTER_ENDPOINT

faker = Faker()
AUTH_BASE = CINESCOPE_AUTH_BASE_URL

@pytest.fixture
def valid_user():
    email = faker.email()
    pwd = "ValidPassword123"
    return {
        "email": email,
        "password": pwd,
        "fullName": "Valid User",
        "passwordRepeat": pwd,
        "roles": ["USER"],
    }

@pytest.fixture(scope="function")
def register_valid_user(valid_user):
    resp = requests.post(f"{AUTH_BASE}{REGISTER_ENDPOINT}", json=valid_user, headers=HEADERS)
    print(f"[REGISTER] {resp.status_code} {resp.text}")
    assert resp.status_code in (201, 409), f"Регистрация не удалась: {resp.status_code} {resp.text}"

class TestNegativeLogin:
    def test_wrong_password(self, register_valid_user, valid_user):
        login_data = {"email": valid_user["email"], "password": "WrongPassword123"}
        response = requests.post(f"{AUTH_BASE}{LOGIN_ENDPOINT}", json=login_data, headers=HEADERS)
        print(f"[LOGIN wrong password] {response.status_code} {response.text}")
        assert response.status_code == 401
        assert any(key in response.text for key in ("error", "message"))

    def test_nonexistent_email(self):
        login_data = {"email": "notregistered@example.com", "password": "AnyPassword123"}
        response = requests.post(f"{AUTH_BASE}{LOGIN_ENDPOINT}", json=login_data, headers=HEADERS)
        print(f"[LOGIN nonexistent email] {response.status_code} {response.text}")
        assert response.status_code == 401
        assert any(key in response.text for key in ("error", "message"))

    def test_empty_request_body(self):
        response = requests.post(f"{AUTH_BASE}{LOGIN_ENDPOINT}", headers=HEADERS)
        print(f"[LOGIN empty body] {response.status_code} {response.text}")
        assert response.status_code in (400, 401)
        assert any(key in response.text for key in ("error", "message"))