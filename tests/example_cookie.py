# Задание 1

import requests

# Создаем объект сессии
s = requests.Session()

# Первый запрос (сервер устанавливает cookie)
response1 = s.get('https://httpbin.org/cookie/set/sessioncookie/123456789') # сервер в ответе отправляет заголовок Set-Cookie: sessioncookie=123456789
print("Ответ после установки cookie:")
print(response1.text)

# Второй запрос - проверка, отправляется ли cookie
response2 = s.get('https://httbin.org/cookie') # сессия автоматически прикрепляет куку sessioncookie=123456789
print("\nОтвет после запроса с сохранённой cookie:")
print(response2.text)

# Задание 2

# Создаем объект сессии
s = requests.Session()

# Вручную добавляем куку в сессию (а не в один запрос)
s.cookies.set('from-my', 'browser') # s.cookies.set(...) добавляет куку в память сессии

# Выполняем GET-запрос
r1 = s.get('https://httpbin.org/cookies')
print("Первый запрос с cookie:")
print(r1.json())

# Второй запрос - кука все еще сохраняется и отправляется
r2 = s.get('https://httpbin.org/cookie')
print("\nВторой запрос с той же cokkie:")
print(r2.json)


