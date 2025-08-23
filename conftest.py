
import os
import sys
import pytest
import requests
from faker import Faker

# пусть проектный корень был виден для импортов
ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, ROOT)

# наши константы
from constants import (
    BASE_URL,
    CINESCOPE_AUTH_BASE_URL,
    REGISTER_ENDPOINT,
    HEADERS,
)

# API менеджер + наш удобный реквестер
from api.api_manager import ApiManager
from custom_requester.custom_requester import CustomRequester
from utils.data_generator import DataGenerator

faker = Faker()

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    # чтобы не цеплялись системные прокси и не падал SSL на dev стенде
    s.trust_env = False
    s.verify = False  # dev-сертификат самоподписанный, отключаем проверку
    yield s
    s.close()

@pytest.fixture(scope="session")
def cinescope(session):
    """Кастомный реквестер для Cinescope auth."""
    from custom_requester.custom_requester import CustomRequester

    r = CustomRequester(session=session, base_url=CINESCOPE_AUTH_BASE_URL)
    r.update_headers(**HEADERS)
    session.verify = False  # у вас self-signed HTTPS на dev, чтобы не ловить SSL
    return r

@pytest.fixture(scope="session")
def api_manager(session):
    """Единая точка входа для API-слоя (использует внутри ту же session)."""
    return ApiManager(session)

@pytest.fixture(scope="session")
def booker(session):
    """Кастомный реквестер на Restful Booker с базовым URL = BASE_URL."""
    r = CustomRequester(session=session, base_url=BASE_URL)
    return r

@pytest.fixture(scope="session")
def auth_session(booker):
    """
    Возвращаем requests.Session с установленным Cookie токена Booker.
    Так тесты могут делать auth_session.post(f"{BASE_URL}/booking", ...).
    """
    from constants import AUTH_ENDPOINT

    resp = booker.post(AUTH_ENDPOINT, data={"username": "admin", "password": "password123"}, expected_status=200)
    token = resp.json()["token"]

    s = requests.Session()
    s.headers.update(booker.headers)
    # кладём токен в cookie и как отдельный атрибут — для тестов
    s.headers["Cookie"] = f"token={token}"
    s.token = token
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
    Регистрирует пользователя в Cinescope и возвращает dict с id.
    """
    try:
        resp = cinescope.post(REGISTER_ENDPOINT, json=test_user, expected_status=201)
        data = resp.json()
        user = {**test_user, "id": data.get("id")}
    except ValueError:
        resp = cinescope.post(REGISTER_ENDPOINT, json=test_user, expected_status=409)
        user = {**test_user, "id": None}
    return user

@pytest.fixture(scope="session")
def requester(session):
    """Если где-то нужны просто вызовы относительно BASE_URL (Restful Booker)."""
    return CustomRequester(session=session, base_url=BASE_URL, headers={"Content-Type": "application/json"})
