import pytest
import requests
from constants import BASE_URL

@pytest.fixture
def auth_session():
    session = requests.Session()
    # Здесь настрой заголовки, если нужен токен авторизации
    session.headers.update({"Content-Type": "application/json"})
    return session

@pytest.fixture
def booking_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-05"
        },
        "additionalneeds": "Breakfast"
    }
