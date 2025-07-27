# Проверка на None
# Задание 1
username = None
if username is None: # Используем оператор is для проверки, является ли переменная None
    print("Гость")

# Задание 2
def greet_user(name): #Определяем функцию greet_user с одним параметром name

    if name is None: # Проверяем: если name равно None, заменяем его на "Аноним"
        name = "Аноним"

    print(f"Привет, {name}!") # Выводим приветствие с именем

greet_user(None)  # Ожидаем: Привет, Аноним!
greet_user("Алексей")  # Ожидаем: Привет, Алексей!

# Задание 3
user_info = {
    "name": "Иван",
    "age": 30,
    "email": None # email пока не указан
}

if user_info["email"] is None: # is None используется именно для проверки отсутствующих значений.
    user_info["email"] = "не указан" # Если "email" действительно None, мы присваиваем этому ключу значение "не указан"

print(user_info)