import pytest
from constants import BASE_URL
import requests

class TestNegativeBookings:
    def test_post_with_invalid_data(self, auth_session):
        invalid_data = {
            "lastname": "Brown",
            "totalprice": "abc",
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-01-04",
                "checkout": "2025-01-15"
            },
            "additionalneeds": "Breakfast"
        }
        response = auth_session.post(f"{BASE_URL}/booking", json=invalid_data)
        assert response.status_code in [400, 500], \
            f"Ожидался статус 400/500, но получен {response.status_code}"

    def test_get_non_existing_booking(self, auth_session):
        response = auth_session.get(f"{BASE_URL}/booking/99999999")
        assert response.status_code == 404, \
            f"Ожидался статус 404, но получен {response.status_code}"

    @pytest.mark.xfail(reason="Restful-Booker при PATCH {} возвращает 200, а не 400/403")
    def test_patch_without_data(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        booking_id = create_booking.json().get("bookingid")

        response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json={})
        assert response.status_code in [400, 403], \
            f"Ожидался статус 400/403, но получен {response.status_code}"

        auth_session.delete(f"{BASE_URL}/booking/{booking_id}")

    def test_delete_without_auth(self, booking_data):
        create_booking = requests.post(f"{BASE_URL}/booking", json=booking_data)
        booking_id = create_booking.json().get("bookingid")

        response = requests.delete(f"{BASE_URL}/booking/{booking_id}")
        assert response.status_code in [401, 403], \
            f"Ожидался статус 401/403, но получен {response.status_code}"
