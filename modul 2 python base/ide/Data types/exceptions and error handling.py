# Задание 1, Функция с обработкой ошибок
def safe_divide(a, b):
    try: # пробует выполнить деление a / b
        result = a / b
        return result
    except ZeroDivisionError: # ловит ошибку, если b равно 0.
        print("Ошибка: Деление на ноль невозможно.")
        return None #возвращает None в случае ошибки, чтобы программа не упала.
    except TypeError: # ловит ошибку, если один из аргументов — не число (например, строка).
        print("Ошибка: Деление на ноль невозможно.")
        return None

print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # Ошибка: Деление на ноль невозможно. → None
print(safe_divide("10", 2))    # Ошибка: Оба аргумента должны быть числами. → None

# Задача 2, Проверка ввода и чтение файла
def read_file(filename):
    if not filename: # Проверка, что имя файла не пустое. Если пустое, выводится сообщение об ошибке.
        print("Ошибка: имя файла не может быть пустым.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as file: # Открытие файла в безопасном контексте (автоматическое закрытие файла после чтения).
            content = file.read() # Считывает всё содержимое файла в одну строку и сохраняет в переменную content
            print("Содержимое файла:")
            print(content)
    except FileNotFoundError: # Попытка открыть и прочитать файл. Если файл не найден, выводится сообщение об ошибке
        print(f"Ошибка: файл '{filename}' не найден.")

read_file("")  # Ошибка: имя файла не может быть пустым
read_file("nonexistent.txt")  # Ошибка: файл 'nonexistent.txt' не найден
read_file("example.txt")  # Покажет содержимое файла, если он существует

# Задача 3 Проверка деления чисел из списка
def divide_numbers(numbers):
    for num in numbers: # Пройдись по каждому элементу в списке numbers и временно называй его num
        try:
            result = 100 / num # Пробуем поделить 100 на текущее значение num.
            print(f"100 / {num} = {result}") # Если получилось — сохраняем результат в переменную result
        except ZeroDivisionError: # Если возникает ZeroDivisionError — сообщаем об ошибке деления на 0.
            print(f"Ошибка: Деление на ноль при числе {num}")
        except TypeError: # Если возникает TypeError — сообщаем, что элемент не является числом.
            print(f"Ошибка: Некорректный тип данных ({num}) — должен быть числом")

sample = [10, 0, 'a', 25, None, 4]
divide_numbers(sample)