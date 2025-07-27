import requests  # Сторонняя библиотека

def my_function(url):
    response = requests.get(url)  # брейкпоинт сюда
    if response.status_code == 200:
        return response.text
    else:
        return "Error"

url = "https://www.example.com"
content = my_function(url)
i = "i'm here"
print(content)