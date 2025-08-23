# 1. Покрытие метода PUT
import requests
from constants import BASE_URL

class TestBookings:
    def test_update_booking(self, booking_data):
        # 1. Создаём сессию с токеном
        session = requests.Session()
        auth_payload = {"username": "admin", "password": "password123"}
        auth_response = session.post(f"{BASE_URL}/auth", json=auth_payload)
        assert auth_response.status_code == 200, "Не удалось получить токен"
        token = auth_response.json()["token"]
        session.headers.update({"Cookie": f"token={token}"})

        # 2. Создаём бронирование
        create_booking = session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id, "ID бронирования не получен"

        # 3. Обновляем данные брони (PUT)
        updated_booking_data = {
            "firstname": "Anna",
            "lastname": "Smith",
            "totalprice": 150,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2025-02-01",
                "checkout": "2025-02-10"
            },
            "additionalneeds": "Lunch"
        }
        update_booking = session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_booking_data)
        assert update_booking.status_code == 200, f"Ошибка при обновлении брони: {update_booking.text}"

        updated = update_booking.json()
        assert updated["firstname"] == updated_booking_data["firstname"], "Имя не обновилось"
        assert updated["lastname"] == updated_booking_data["lastname"], "Фамилия не обновилась"
        assert updated["totalprice"] == updated_booking_data["totalprice"], "Цена не обновилась"

        # Шаг 4: Удаляем бронирование
        deleted_booking = session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"