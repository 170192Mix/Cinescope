import os
import sys
import pytest
import requests
from faker import Faker

# чтобы корень проекта был виден для импортов
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from constants import (
    BASE_URL,
    AUTH_ENDPOINT,
    CINESCOPE_AUTH_BASE_URL,
    REGISTER_ENDPOINT,
    HEADERS,
)
from api.api_manager import ApiManager
from custom_requester.custom_requester import CustomRequester
from utils.data_generator import DataGenerator

faker = Faker()


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    # не тянуть системные прокси, не падать на dev-сертах
    s.trust_env = False
    s.verify = False
    yield s
    s.close()


@pytest.fixture(scope="session")
def cinescope(session):
    """Клиент auth-сервиса Cinescope на базе CustomRequester"""
    r = CustomRequester(session=session, base_url=CINESCOPE_AUTH_BASE_URL)
    r.update_headers(**HEADERS)
    return r


@pytest.fixture(scope="session")
def api_manager(session):
    """Единая точка входа в API-слой (использует ту же session)"""
    return ApiManager(session)


@pytest.fixture(scope="session")
def booker(session):
    """Клиент Restful-Booker (BASE_URL)"""
    return CustomRequester(session=session, base_url=BASE_URL)


@pytest.fixture(scope="session")
def auth_session(booker):
    """
    Возвращает requests.Session с cookie токена Booker
    Удобно для прямых вызовов
    """
    resp = booker.send_request(
        "POST", AUTH_ENDPOINT,
        json={"username": "admin", "password": "password123"},
        expected_status=200,
    )
    token = resp.json()["token"]

    s = requests.Session()
    s.headers.update(booker.headers)
    s.headers["Cookie"] = f"token={token}"
    s.token = token  # иногда удобно в тестах
    return s


@pytest.fixture(scope="session")
def booking_data():
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-04", "checkout": "2025-01-15"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture(scope="session")
def test_user():
    pwd = DataGenerator.generate_random_password()
    return {
        "email": DataGenerator.generate_random_email(),
        "fullName": DataGenerator.generate_random_name(),
        "password": pwd,
        "passwordRepeat": pwd,
        "roles": ["USER"],
    }


@pytest.fixture(scope="session")
def registered_user(cinescope, test_user):
    """
    Регистрирует пользователя (201 или 409) и отдаёт данные для логина
    """
    resp = cinescope.send_request(
        "POST",
        REGISTER_ENDPOINT,
        json=test_user,
        expected_status=(201, 409),
    )
    data = resp.json()
    return {
        "email": test_user["email"],
        "password": test_user["password"],
        "id": data.get("id") if resp.status_code == 201 else None,
    }


@pytest.fixture(scope="session")
def requester(session):
    """Если нужны прямые вызовы относительно BASE_URL (Booker)"""
    return CustomRequester(session=session, base_url=BASE_URL, headers={"Content-Type": "application/json"})


@pytest.fixture(scope="session")
def admin_api(api_manager):
    """
    ApiManager с уже установленным Bearer-токеном администратора.
    AuthAPI.authenticate сам кладёт токен в session.headers
    """
    api_manager.auth_api.authenticate(
        email="api1@gmail.com",
        password="asdqwe123Q",
        expected_status=200,
    )
    return api_manager