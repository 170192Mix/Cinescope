# 1
import requests

s = requests.Session()

# Первый запрос (сервер устанавливает cookie)
response1 = s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print(response1.text)

# Второй запрос (cookie автоматически отправляется)
response2 = s.get('https://httpbin.org/cookies')
print(response2.json()) # Видим, что cookie был отправлен