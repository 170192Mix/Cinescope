import requests
import json

urls = [
    "https://httpbin.org/json",    # Нормальный JSON
    "https://httpbin.org/status/204", # Пустой ответ
    "https://httpbin.org/status/500", # Ошибка 500
    "https://httpbin.org/html",    # HTML вместо JSON
]

for url in urls:
    print(f"URL: {url}")
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    try:
        data = response.json()
        print(f"JSON data: {data}")
    except json.decoder.JSONDecodeError:
        print(f"Ошибка декодирования JSON. Текст ответа: {response.text}")
    except Exception as e:
        print(f"Другая ошибка: {e}")
    print("-" * 30)

import requests

response = requests.get("https://httpbin.org/status/204")
print(response.json())
