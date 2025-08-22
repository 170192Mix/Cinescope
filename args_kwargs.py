# 1 Смешанные аргументы
def process_data(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
process_data(1, 2, 3, name="Alice", age=25)
# Вывод:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}

# 2 Конфигурация функции
def configure_function(*args, **kwargs):
    return {key: kwargs[key] for key in args if key in kwargs}

    print(configure_function("theme", "volume", theme="dark", volume=50))
    # Вывод: {'theme': 'dark', 'volume': 50}

# 3 Функция-декоратор
def log_args_kwargs(func): # получает функцию как аргумент
    def wrapper(*args, **kwargs): # перехватывает все аргументы, переданные в оригинальную функцию
        print("Positional arguments:", args)
        print("Keyword argument:", kwargs)
        return func(*args, **kwargs)
    return wrapper()

@log_args_kwargs
def my_function(x, y, **kwargs):
    return x + y

result = my_function(10, 20, debug=True, verbose=False)
print("Result:", result)