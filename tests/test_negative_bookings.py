import pytest
from constants import BASE_URL
import requests

class TestNegativeBookings:

    def test_post_with_invalid_data(self, auth_session): # auth_session — это фикстура (создаёт сессию с авторизацией)
        invalid_data = {
            # Убираем firstname (портим)
            "lastname": "Brown",
            "totalprice": "abc",  # Некорректный формат числа, должно быть число
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-01-04",
                "checkout": "2025-01-15"
            },
            "additionalneeds": "Breakfast"
        }
        response = auth_session.post(f"{BASE_URL}/booking", json=invalid_data) # Отправляем POST запрос и проверяем что сервер вернет ошибку
        # Ожидаем ошибку
        assert response.status_code in [400, 500], \
            f"Ожидался статус 400/500, но получен {response.status_code}" # \ эксплицитным переносом строки кода на новую строку без разрыва команды

    def test_get_non_existing_booking(self, auth_session):
        response = auth_session.get(f"{BASE_URL}/booking/99999999") # Пытаемся получить бронирование с ID 99999999, которого точно нет
        assert response.status_code == 404, \
            f"Ожидался статус 404, но получен {response.status_code}"

    def test_patch_without_data(self, auth_session, booking_data):

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data) # Сначала создаем бронирование (чтобы было, что обновлять)
        booking_id = create_booking.json().get("bookingid")

        response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json={}) # Пытаемся частично обновить без данных
        assert response.status_code in [400, 403], \
            f"Ожидался статус 400/403, но получен {response.status_code}"

        auth_session.delete(f"{BASE_URL}/booking/{booking_id}") # Удаляем бронирование

    def test_delete_without_auth(self, booking_data):

        create_booking = requests.post(f"{BASE_URL}/booking", json=booking_data) # Создаем бронирование без авторизации
        booking_id = create_booking.json().get("bookingid")

        response = requests.delete(f"{BASE_URL}/booking/{booking_id}") # Пытаемся удалить без авторизации
        assert response.status_code in [401, 403], \
            f"Ожидался статус 401/403, но получен {response.status_code}"
