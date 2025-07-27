import requests
import time

url = "https://httpbin.org/get"
num_requests = 10

print("Запросы с использованием сессии:")
start_time = time.time()

session = requests.Session()  # Создаем сессию
try:
    for i in range(num_requests):
        response = session.get(url)
        response.raise_for_status()
except Exception as e:
    print(f"ошибка: {e}")
finally:
    session.close()  # закрываем сессию
end_time = time.time()
print(f"Время выполнения с сессией: {end_time - start_time:.4f} секунд\n")

# Запросы БЕЗ использования сессии:
print("Запросы БЕЗ использования сессии:")
start_time = time.time()
try:
    for i in range(num_requests):
        response = requests.get(url)
        response.raise_for_status()
except Exception as e:
    print(f"Ошибка: {e}")
end_time = time.time()
print(f"Время выполнения без сессии: {end_time - start_time:.4f} секунд")