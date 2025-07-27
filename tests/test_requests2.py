# Написать запрос без обработки ошибок на url "https://httpbin.org/status/204" и попробовать преобразовать json. Ознакомиться с результатом работы (исключением)

import requests


url = "https://httpbin.org/status/204" # Пустой ответ
response = requests.get(url)

# Без try/except - напрямую вызываем json()
data = response.json() # Здесь произойдет ошибка

print("JSON:", data)


