
import os
import sys
import pytest
import requests
from faker import Faker

# пусть проектный корень был виден для импортов
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# наши константы
from constants import (
    BASE_URL,
    CINESCOPE_AUTH_BASE_URL,
    REGISTER_ENDPOINT,
    HEADERS,
)

# API менеджер
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

    r = CustomRequester(session=session, base_url=CINESCOPE_AUTH_BASE_URL)
    r.update_headers(**HEADERS)
    session.verify = False
    return r

@pytest.fixture(scope="session")
def api_manager(session):
    """Единая точка входа для API-слоя (использует внутри ту же session)"""
    return ApiManager(session)

@pytest.fixture(scope="session")
def booker(session):
    """Кастомный реквестер на Restful Booker с базовым URL = BASE_URL"""
    r = CustomRequester(session=session, base_url=BASE_URL)
    return r

@pytest.fixture(scope="session")
def auth_session(booker):
    """
    Возвращаем requests.Session с установленным Cookie токена Booker.
    Так тесты могут делать auth_session.post(f"{BASE_URL}/booking", ...)
    """
    from constants import AUTH_ENDPOINT

    resp = booker.post(AUTH_ENDPOINT, json={"username": "admin", "password": "password123"}, expected_status=200)
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
    Регистрирует пользователя в Cinescope и возвращает dict с данными для логина.
    Если пользователь уже есть (409), просто возвращает его данные без повторного вызова.
    """
    resp = cinescope.post(REGISTER_ENDPOINT, json=test_user, expected_status=(201, 409))

    data = resp.json()
    return {
        "email": test_user["email"],
        "password": test_user["password"],
        "id": data.get("id") if resp.status_code == 201 else None
    }

@pytest.fixture(scope="session")
def requester(session):
    """Если где-то нужны просто вызовы относительно BASE_URL (Restful Booker)."""
    return CustomRequester(session=session, base_url=BASE_URL, headers={"Content-Type": "application/json"})


@pytest.fixture(scope="session")
def admin_api(api_manager):
    """
    Возвращает ApiManager с уже установленным Bearer токеном для админа.
    """
    # Вызов логина через auth API, чтобы получить токен
    resp = api_manager.auth.login(
        email="api1@gmail.com",
        password="asdqwe123Q",
        expected_status=200
    )

    token = resp.json().get("accessToken") or resp.json().get("token")
    if not token:
        raise RuntimeError("Не удалось получить токен администратора")

    # Устанавливаем токен в заголовки всех запросов
    api_manager.set_bearer(token)
    return api_manager
