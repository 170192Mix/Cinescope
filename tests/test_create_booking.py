import pytest
from constants import BASE_URL # импортируем константу BASE_URL

class TestBookings:
    def test_update_booking(self, auth_session, booking_data):
        # Создаем бронирование (POST)
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data) # Отправляем POST-запрос на BASE_URL/booking
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid") # Парсим ответ (create_booking.json()), достаём bookingid. Разобрать данные, которые вернулись от сервера, и достать нужную информацию
        assert booking_id is not None, "Идентификатор брони не найден"

        # Подготавливаем обновленные данные
        # Создаём словарь с новыми данными для бронирования
        updated_booking_data = {
            "firstname": "Anna",
            "lastname": "Smith",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-03-01",
                "checkout": "2025-03-10"
            },
            "additionalneeds": "Breakfast and Dinner"
        }

        # Обновляем бронирование (PUT)
        update_booking = auth_session.put(
            f"{BASE_URL}/booking/{booking_id}",
            json=updated_booking_data,
            headers={"Cookie": f"token={auth_session.token}"}
        )
        assert update_booking.status_code == 200, "Ошибка при обновлении брони"

        # Проверяем через GET, что данные обновились
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}") # Делаем GET-запрос к бронированию, чтобы убедиться, что данные изменились
        assert get_booking.status_code == 200, "Не удалось получить обновленную бронь"
        updated = get_booking.json()

        # Проверяем, что каждое поле на сервере совпадает с тем, что мы отправили
        assert updated["firstname"] == updated_booking_data["firstname"], "Имя не обновилось"
        assert updated["lastname"] == updated_booking_data["lastname"], "Фамилия не обновилась"
        assert updated["totalprice"] == updated_booking_data["totalprice"], "Цена не обновилась"
        assert updated["depositpaid"] == updated_booking_data["depositpaid"], "Депозит не обновился"
        assert updated["bookingdates"]["checkin"] == updated_booking_data["bookingdates"]["checkin"], "Дата заезда не обновилась"
        assert updated["bookingdates"]["checkout"] == updated_booking_data["bookingdates"]["checkout"], "Дата выезда не обновилась"
        assert updated["additionalneeds"] == updated_booking_data["additionalneeds"], "Пожелания не обновились"

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"