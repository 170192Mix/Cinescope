import requests
from modul_4_python_base.Cinescope.Restful_Booker_API.conftest import requester
from modul_4_python_base.tests.test_booking import response

url = 'https://restful-booker.herokuapp.com/booking'
payload = { # Это словарь
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-01-04",
        "checkout": "2025-01-15"
    },
    "additionalneeds": "Breakfast"
}

response = requester.post(url, data=payload) # если вместо json=payload использовать data=payload - json=Преобразует payload в JSON тело выглядит b'{"key": "value"}'
# data=Отправляет как form-data (по умолчанию) тело выглядит b'key=value&key2=value2'b'key=value&key2=value2'
# Печать ответ от сервера
print("Ответ от сервера:")
print(response.text) # Это ответ от сервера. Скажет бронирование созданно вот его номер

# Печать тела запроса, который был отправлен
print("\nТело отправленного запроса:")
print(response.request.body) # Что именно я послал серверу