# Простейшие функции с одним параметром
# Задачи без return:
# 1
def greet(name):
    print("Привет, " + name + "!")

greet("Максим")

# 2
def print_number(num):
    print("Число", num)

print_number(5)

# 3
def repeat_word(word, times):
    for _ in range(times):
        print(word)

repeat_word("Привет", 3)

# 4
def print_length(text):
    print(len(text)) # len() — для подсчёта длины

print_length("Привет")

# 5
def print_double(number):
    print(number * 2)

print_double(7)

# 6
def add_ten(number):
    return number + 10

print(add_ten(7))

# 7
def multiply_by_three(num):
    return num * 3

print(multiply_by_three(2))

# 8
def is_even(number):
    if number % 2 == 0: # Оператор % 2 проверяет чётность
        return "Чётное"
    else:
        return "Нечетное"

print(is_even(8))  # → Чётное
print(is_even(5))  # → Нечётное

# 4. Функции с параметрами и логикой
# 1
def print_range(n):
    for i in range(1, n + 1): # for - цикл который повторяет
        print(i) # чтобы печатать каждое число по очереди, нужно выводить i

# 2
def print_stars(count):
    for i in range(count): # range(count) — цикл повторится count раз
        print("*")

print_stars(5)

# 3
def print_table(num):
    for i in range(1, 5): # i — будет по очереди принимать эти значения, range(1, 5) создаёт числа 1, 2, 3, 4 (до 5, но не включая)
        for j in range(1, 5): # j — по очереди принимает значения 1, 2, 3, 4
            print(f"{i*j:4}", end="") # i * j — здесь идёт перемножение текущих чисел строки и столбца, f"{i*j:4}" — форматированный вывод, :4 означает занять 4 позиции, чтобы числа красиво выровнялись
        print()

print_table(5)

# 4
def analyze_number(num):
    if num > 0:
        print("Положительное")
    elif num < 0:
        print("Отрицательное")
    else:
        print("Это ноль")

analyze_number(7)
analyze_number(-5)
analyze_number(0)

# 5
def count_digits(number):
    return len(str(abs(number))) # len считает количество символов (цифр),

print(count_digits(12345))
print(count_digits(-957))
print(count_digits(0))

# 6
def sum_to_n(n):
    return list(range(1, n + 1))

print(sum_to_n(5))

# 7
def get_grade(score):
    if score >= 90:
        return "Олично"
    elif score >= 80:
        return "Хорошо"
    elif score >= 70:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"

print(get_grade(80)) # Хорошо
print(get_grade(45)) # Неудовлетворительно

# 5. Функции с несколькими параметрами
# 1
def greet_person(first_name, last_name):
    print(f"Имя: {first_name}")
    print(f"Фамилия: {last_name}")

greet_person("Максим", "Антоньян")

# 2
def compare_numbers(a, b):
    if a > b:
        print(f"{a} ,больше чем {b}")

compare_numbers(7, 5)

# 3
def print_info(name, age, city):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {city}")

print_info("Анто", 47, "Краснодар")

# 4
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 4))

# 5
def get_full_name(first, last): # параметры, которые функция принимает:
    return f"{first} {last}" # f-строка (форматированная строка)

print(get_full_name("Николай", "Постушенко"))

# 6
def calculate_area(length, width):
    return length * width

print(calculate_area(4, 9))

# 7
def find_max(a, b, c):
    print(max(a, b, c))

find_max(4, 7, 2) # 7

# 6. Функции, использующие результаты других функций
# 1
def double(x):
    return x * 2 # возвращаем удвоенное значение.

result = double(7) # вызываем функцию и сохраняем результат
print(result)

# 2
def get_square(x):
    return x * x

def sum_of_squares(a, b):
    return get_square(a) + get_square(b)

result = sum_of_squares(7, 6)
print(result) # # Выведет 85 (т.к. 7² + 6² = 49 + 36)

# 3
def get_length(text): # возвращает длину строки.
    return len(text) # return len(text) возвращает длину строки text

def compare_lengths(text1, text2): # сравнивает длины двух строк и возвращает сообщение
    len1 = get_length(text1)
    len2 = get_length(text2)

    if len1 > len2:
        return "Первая строка длиннее."
    elif len1 > len2:
        return "Вторая строка длиннее."
    else:
        return "Строки одинаковой длины."

result = compare_lengths("привет", "здравствуйте")
print(result)

# 4
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 # Возвращает результат по формуле перевода из Цельсия в Фаренгейты:F = (C × 9/5) + 32

def compare_temperatures(c1, c2):
    f1 = celsius_to_fahrenheit(c1)

    if f1 > c2:
        return "Температура в Цельсиях выше."
    elif f1 < c2:
        return "Температура в Фаренгейтах выше."
    else:
        return "Температуры равны"

result = compare_temperatures(30, 90)
print(result) # Выведет: "Температура в Фаренгейтах выше."

# 5
def add_ten(x):
    return x + 10

def process_numbers(a, b):
    total = 0
    for num in a:
        total += add_ten(num)
    return total

result = process_numbers([1, 2, 3], 10)
print(result) # # (1+10) + (2+10) + (3+10) = 11 + 12 + 13 = 36

# 6
def multiply_by_two(x):
    return x * 2

def calculate_perimeter(length, width):
    return 2 * (length + width)

result = calculate_perimeter(5, 3)
print(result)  # Выведет: 16 потому что 2 * (5 + 3) = 2 * 8 = 16

# 7
def is_even(x):
    return x % 2 == 0  # Возвращает True, если x чётное

def filter_even_sum(a, b, c):
    total = 0
    if is_even(a): # is_even() для каждого числа и суммирует только чётные
        total += a
    if is_even(b): # is_even() для каждого числа и суммирует только чётные
        total += b
    if is_even(c): # is_even() для каждого числа и суммирует только чётные
        total += c
    return total  # Важно вернуть результат

print(filter_even_sum(5, 8, 13))  # Выведет: 8

# 7. Функции с вложенными функциями
# 1
def outer_function():
    def inner_function():
        print("Внутренняя функция")

    inner_function()

outer_function() # запуск ОДИН РАЗ

# 2
def number_analyzer(num):
    def is_positive():
        return num > 0

    def is_even():
        return num % 2 == 0

    if is_positive() and is_even():
        print("Положительное четное число")
    elif is_positive():
        print("Положительное нечетное число")
    else:
        print("Отрицательное число или ноль")