# Программа, которая выводит таблицу сложения для чисел от 1 до 5.
for i in range(1, 6): # Внешний цикл for i in range(1, 6): проходит по числам от 1 до 5.
    for j in range(1, 6): # Внутренний цикл for j in range(1, 6): также проходит по числам от 1 до 5.
        print(f"{i} + {j} = {i + j}") # Внутри вложенного цикла выводится результат сложения текущих значений i и j.
    print()

numbers = [10, 0, 5, "abc", 2]

for item in numbers:
    try:
        result = 100 / item
        print(f"100 / {item} = {result}")
    except ZeroDivisionError:
        print(f"Ошибка: деление на ноль при значении {item}")
    except TypeError:
        print(f"Ошибка: невозможно делить на тип {type(item).__name__} ({item})")
