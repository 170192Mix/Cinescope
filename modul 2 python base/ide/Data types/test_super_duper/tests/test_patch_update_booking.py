from constants import BASE_URL

def test_patch_update_booking(auth_session, booking_data):
    # 1. Создание бронирования
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert create_response.status_code == 200, "Ошибка при создании брони"

    booking_id = create_response.json().get("bookingid")
    assert booking_id is not None, "ID брони не получен"

    # 2. Обновляем только имя и дополнительные потребности
    patch_data = {
        "firstname": "Alex",
        "additionalneeds": "Late checkout"
    }

    patch_response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=patch_data)
    assert patch_response.status_code == 200, "Ошибка при частичном обновлении"

    # 3. Получаем обновлённую бронь
    get_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_response.status_code == 200, "Не удалось получить обновлённую бронь"
    updated_booking = get_response.json()

    # 4. Проверка: изменённые поля — изменены
    assert updated_booking["firstname"] == patch_data["firstname"]
    assert updated_booking["additionalneeds"] == patch_data["additionalneeds"]

    # 5. Проверка: остальные поля остались прежними
    assert updated_booking["lastname"] == booking_data["lastname"]
    assert updated_booking["totalprice"] == booking_data["totalprice"]
    assert updated_booking["depositpaid"] == booking_data["depositpaid"]
    assert updated_booking["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert updated_booking["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]

    # 6. Удаляем бронь
    delete_response = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
    assert delete_response.status_code == 201, "Ошибка при удалении брони"
