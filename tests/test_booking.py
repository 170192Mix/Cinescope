from typing import Any

def test_create_booking(booker):
    endpoint = "/booking"
    payload: dict[str, Any] = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-04",
            "checkout": "2025-01-15",
        },
        "additionalneeds": "Breakfast",
    }

    # JSON на Restful-Booker
    resp = booker.post(endpoint, json=payload, expected_status=200)

    print("Ответ от сервера:", resp.text)
    print("Тело отправленного запроса:", resp.request.body)

    data = resp.json()
    assert "bookingid" in data, "bookingid отсутствует в ответе"
    assert "booking" in data, "booking объект отсутствует в ответе"
    assert data["booking"]["firstname"] == payload["firstname"]
    assert data["booking"]["lastname"] == payload["lastname"]
