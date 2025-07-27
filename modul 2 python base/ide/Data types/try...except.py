# Задание 1
numbers = [10, 0, 5, "abc", 2]

for num in numbers:
    try:
        result = 100 / int(num)
        print(f"100 / {num} = {result}")
    except ZeroDivisionError:
        print(f"Ошибка: деление на ноль при значении {num}")
    except (ValueError, TypeError):
        print(f"Ошибка: невозможно преобразовать {num} в число")

# Задание 2
values = ["123", "text", None, "456"]

for value in values:
    try:
        number = int(value)
        print(f"Преобразовано число: {number}")
    except (ValueError, TypeError):
        print(f"Ошибка: невозможно преобразовать {value} в число")

# Задание 3
pairs = [ (10, 5), (3, 0), (7, "str") ]

for numerator, denominator in pairs:
    try:
        result = numerator / denominator
        print(f"{numerator} / {denominator} = {result}")
    except ZeroDivisionError:
        print(f"Ошибка: деление на ноль при делении {numerator} / {denominator}")
    except TypeError:
        print(f"Ошибка: неподходящий тип данных при делении {numerator} / {denominator}")
