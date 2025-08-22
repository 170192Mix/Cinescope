# 1 Приветсвие
def greet (**kwargs):
    name = kwargs.get('name', 'Stranger') # Пытаемся достать из словаря kwargs
    age = kwargs.get('age') # Пробуем достать значение по ключу age

    if age is not None: # Проверяем было ли что-то продано
        print(f"Hello, {name}! You are {age} years old")
    else:
        print(f"Hello, {name}!") # Если возраст не передали, то просто говорим Hello

# пример вызова
greet(name="Alice", age=25)
# Вывод: Hello, Alice! You are 25 years old.

# 2 Создание словаря
def create_dict(**kwargs):
    return kwargs

# Пример вызова
print(create_dict(a=1, b=2, c=3))
# Вывод: {'a': 1, 'b': 2, 'c': 3}

# 3 Обновление параметров
def update_settings(base_setting, **kwargs):
    updated_settings = base_setting.copy() # Создаем копию словаря
    updated_settings.update(kwargs) # Обновляем копию словаря

    return updated_settings # Возвращаем обновленный словарь из функции

# Пример вызова
default_setting = {"theme": "light", "notifications": True}
print(update_settings(default_setting, theme="dark", volue=80))
# Вывод: {'theme': 'dark', 'notifications': True, 'volume': 80}

# 4 Фильтрация данных
def filter_kwargs(**kwargs):
    result = {} # Создаем пустой словарь
    for key, value in kwargs.items(): # Начинаем перебор всех пар
        if value > 10: # Проверяем если значение больше 10
            result[key] = value # Добавляем эту пару в словарь
        return result

# Пример вызова
print(filter_kwargs(a=5, b=20, c=15, d=3))
# Вывод: {'b': 20, 'c': 15}

# 5 Декоратор для логирования
def log_kwargs(func): # Создаем декоратор
    def wrapper(*args, **kwargs): # создаём вложенную функцию wrapper
        print(f"Called with kwargs: {kwargs}")
        return func(*args, **kwargs) # Вызываем оригинальную функцию
    return wrapper # Возвращаем функцию

@log_kwargs # Декоратор
def my_function(a, b, **kwargs):
    return a + b # Складываем a и b

my_function(5, 10, debug=True, verbose=False)
# Вывод:
# Called with kwargs: {'debug': True, 'verbose': False}