def test_create_booking(auth_session, booking_data):
    # 1 Создаем бронирование
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert create_response.status_code == 200, "Ошибка при создании брони"

    booking_id = create_response.json().get("bookingid")
    assert booking_id is not None, "ID брони не получен"

    # 2. Обновлённые данные (абсолютно все поля)
    updated_data = {
        "firstname": "Ivan",
        "lastname": "Petrov",
        "totalprice": 98765,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-07"
        },
        "additionalneeds": "Champagne"
    }

    # 3. Отправляем PUT запрос
    put_response = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_data)
    assert put_response.status_code == 200, "Ошибка при обновлении брони"

    # 4. Получаем обновлённую бронь и проверяем поля
    get_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_response.status_code == 200, "Бронь не найдена после обновления"
    booking = get_response.json()

    assert booking["firstname"] == updated_data["firstname"]
    assert booking["lastname"] == updated_data["lastname"]
    assert booking["totalprice"] == updated_data["totalprice"]
    assert booking["depositpaid"] == updated_data["depositpaid"]
    assert booking["bookingdates"]["checkin"] == updated_data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == updated_data["bookingdates"]["checkout"]
    assert booking["additionalneeds"] == updated_data["additionalneeds"]

    # 5. Удаляем бронирование
    del_response = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
    assert del_response.status_code == 201, "Ошибка при удалении брони"


