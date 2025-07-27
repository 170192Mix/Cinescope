# Функции
# Задача 1
def greet_person(name, age):
    print(f"Привет, {name}! Тебе {age} лет.")

greet_person("Ксюша", 17)
greet_person("Максим", 19)

# Задача 2
def circle_area(radius, pi=3.14159):
    return pi * radius ** 2
area1 = circle_area(5)  # Радиус 5, используем стандартное значение pi
print("Площадь круга (по умолчанию pi):", area1)

area2 = circle_area(5, pi=3.14) # Вызов с явно переданным значением pi
print("Площадь круга (pi = 3.14):", area2)

# Задача 3
def book_info(title, author, year, genre="Неизвестно"):
    print(f"Название: {title}")
    print(f"Автор: {author}")
    print(f"Год издания: {year}")
    print(f"Жанр: {genre}")

book_info("Капитал", "Карл Маркс", 1867, "Философия") # Позиционные аргументы

# Задание 4
def convert_currency(amount, rate, from_currency="USD", to_currency="EUR"):
    converted = amount * rate
    print(f"{amount} {from_currency} = {converted} {to_currency}")
    return converted

convert_currency(100, 0.92, "USD", "EUR") # Позиционные аргументы
convert_currency(amount=0.005, rate=60000, from_currency="BTC", to_currency="USD") # Именованные аргументы

# Задание 1 (return)
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

# Примеры вызова:
print(max_of_two(5, 10))  # Должно вывести: 10
print(max_of_two(15, 3))   # Должно вывести: 15
print(max_of_two(-1, -5))  # Должно вывести: -1

# Задание 2 (return)
def string_length(s):
    return len(s)

print(string_length("Hello"))  # Должно вывести: 5
print(string_length("Python is fun"))  # Должно вывести: 13
print(string_length(""))  # Должно вывести: 0

# Задание 1 (easy): Калькулятор стоимости доставки
def calculate_delivery_cost(weight, distance, fragile=False):
    base_cost = 10 * weight + 5 * distance # Рассчитывается базовая стоимость доставки:

    if fragile:
        base_cost *= 1.5 # увеличение на 50 %

    final_cost = max(base_cost, 200) # минимальная стоймость - 200 рублей
    return final_cost # Возвращает окончательную стоимость доставки из функции.

print(calculate_delivery_cost(5, 10)) # # 10*5 + 5*10 = 50 + 50 = 100 → минималка 200 → Вывод: 200.0
print(calculate_delivery_cost(10, 20, fragile=True)) # 10*10 + 5*20 = 100 + 100 = 200 → хрупкая: 200 * 1.5 = 300 → Вывод: 300.0
print(calculate_delivery_cost(15, 50))  # 10*15 + 5*50 = 150 + 250 = 400 → Вывод: 400.0

# Задание 2 (medium): Анализ списка чисел
def analyze_numbers(numbers):

    if not numbers: # возвращается словарь со значениями None для всех ключей.
        return {
            "average": None,
            "min": None,
            "max": None,
            "even_count": None
        }
    average = sum(numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    even_count = sum(1 for num in numbers if num % 2 == 0)

    return {
        "average": average,
        "min": minimum,
        "max": maximum,
        "even_count": even_count
    }
print(analyze_numbers([10, 5, 8, 3, 12]))
print(analyze_numbers([]))

# Задание 3 (medium): Фильтрация списка по условию
def filter_list(data, threshold):
    result = [x for x in data if x >= threshold] # Это генератор списка, который отбирает только те элементы x из data, которые больше или равны threshold.
    return result

data = [1, 5, 10, 2, 8, 12]
threshold = 7
result = filter_list(data, threshold)
print(result)  # Должно вывести: [10, 8, 12]