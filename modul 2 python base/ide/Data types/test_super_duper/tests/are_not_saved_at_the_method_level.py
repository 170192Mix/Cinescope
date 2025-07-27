# 2
import requests

s = requests.Session()

# Указываем cookie для первого запроса
r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# Вывод: '{"cookies": {"from-my": "browser"}}'

# Второй запрос не использует cookie
r = s.get('https://httpbin.org/cookies')
print(r.text)
# Вывод: '{"cookies": {}}'