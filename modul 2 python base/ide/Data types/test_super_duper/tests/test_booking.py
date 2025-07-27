# Отправить POST запрос, урл и дата ниже, передав payload в параметр json:
import requests

url = 'https://restful-booker.herokuapp.com/booking'

payload = {
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

# Отправляем запрос с data
response = requests.post(url, json=payload)

# Выводим информацию
print("Статус код:", response.status_code)
print("Ответ сервера:", response.text)
print("Отправленное тело:", response.request.body)
