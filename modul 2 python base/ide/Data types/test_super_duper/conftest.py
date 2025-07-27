import pytest

@pytest.fixture
def input_data():
    return [1, 2, 3, 4, 5]

def test_sum(input_data): #используем фикстуру как аргумент функции
    assert sum(input_data) == 15

def test_len(input_data): #используем фикстуру как аргумент функции
    assert len(input_data) == 5

# Задание 1
import requests

URL = "https://restful-booker.herokuapp.com/booking"

def test_create_and_get_booking():
    # 1. Данные для бронирования
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-01",
            "checkout": "2023-10-10"
        },
        "additionalneeds": "Breakfast"
    }

    # 2. POST — создаём бронирование
    post_response = requests.post(URL, json=booking_data)

    # 3. Проверяем, что POST успешен
    assert post_response.status_code == 200 or post_response.status_code == 201

    # 4. Получаем ID бронирования
    booking_id = post_response.json()["bookingid"]

    # 5. Выполняем GET по этому ID
    get_response = requests.get(f"{URL}/{booking_id}")

    # 6. Проверяем, что GET успешен
    assert get_response.status_code == 200

    # 7. Проверяем, что имя такое же, как отправили
    get_data = get_response.json()
    assert get_data["firstname"] == booking_data["firstname"]
    assert get_data["lastname"] == booking_data["lastname"]