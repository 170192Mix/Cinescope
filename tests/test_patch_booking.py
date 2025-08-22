# 2. Покрытие метода PATCH
import pytest
import requests
from constants import BASE_URL

class TestBookings:
    @pytest.mark.xfail(reason="На Restful-Booker PATCH {} -> 200, а не 400/403")
    def test_patch_booking(self, booking_data):
        # 1. Получаем токен для авторизации
        auth_response = requests.post(f"{BASE_URL}/auth", json={ # отправляем POST запрос
            "username": "admin",
            "password": "password123"
        })
        assert auth_response.status_code == 200, "Ошибка при получении токена" # Проверяем что сервер ответил 200
        token = auth_response.json().get("token") # Парсим ответ достаем токен
        assert token, "Токен не получен"

        headers = {"Cookie": f"token={token}"} # Создаём заголовок Cookie с токеном для всех запросов

        # 2. Создаем бронирование через POST
        create_booking = requests.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid") # Забираем booking чтобы его менять и удалять
        assert booking_id, "Идентификатор брони не получен"

        # Сохраняем исходные данные
        original_data = create_booking.json()["booking"]

        # 3. PATCH — частично обновляем бронирование
        patch_data = {
            "firstname": "Alex",
            "additionalneeds": "Dinner" # хотим изменить имя и положение
        }
        patch_booking = requests.patch(
            f"{BASE_URL}/booking/{booking_id}",
            json=patch_data,
            headers=headers
        )
        assert patch_booking.status_code == 200, "Ошибка при частичном обновлении брони"

        # 4. Проверяем изменения
        updated = patch_booking.json()
        assert updated["firstname"] == patch_data["firstname"], "Имя не обновилось"
        assert updated["additionalneeds"] == patch_data["additionalneeds"], "Дополнительные пожелания не обновились"
        assert updated["lastname"] == original_data["lastname"], "Фамилия изменилась, хотя не должна"

        # 5. Удаляем бронирование
        deleted_booking = requests.delete(
            f"{BASE_URL}/booking/{booking_id}",
            headers=headers
        )
        assert deleted_booking.status_code == 201, "Бронь не удалилась"