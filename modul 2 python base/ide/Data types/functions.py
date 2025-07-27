# Задание 1
def greet(): # вызов функции, чтобы она сработала.
    print("Hello, world!")

# Задание 2
def greet_user(name):
    print(f"Привет: {name}") # выводит строку с подставленным именем.

greet_user("Богдан")
greet_user("Вова")
greet_user("Олег")

# Задание 3
def sum_numbers(a, b):
    print("Сумма:", a + b)

sum_numbers(5,3)   # Должно вывести 8
sum_numbers(-1,10) # Должно вывести 9

# Задание 4
def is_even(number):
    if number % 2 == 0: # остаток от деления на 2, если остаток на 0 то четное
        print("Четное")
    else:
        print("Нечетное")

is_even(4)    # Четное
is_even(7)    # Нечетное
is_even(0)    # Четное

# Задание 5
def rectangle_area(width, height):
    if width > 0 and height > 0: # проверка, что оба числа положительные
        area = width * height # вычисление площади
        print("Площадь прямоугольника:", area)
    else:
        print("Некорректные значения")

# Пример вызова:
rectangle_area(5, 10)   # Должно вывести 50
rectangle_area(-2, 5)   # Должно вывести "Некорректные значения"
rectangle_area(5, -2)    # Должно вывести "Некорректные значения"
rectangle_area(0, 10) # Должно вывести "Некорректные значения"