# Проверка на целое число — метод float.is_integer()
# Задание 1
number1 = 10.0
number2 = 10.5

is_whole_number1 = number1.is_integer() # Используем метод is_integer() для проверки целого числа
print(is_whole_number1)

is_whole_number2 = number2.is_integer() # Используем метод is_integer() для проверки целого числа
print(is_whole_number2)

# Задание 2
num = float(input("Введите число: ")) # input() всегда возвращает строку (тип str), даже если пользователь вводит цифры.

if num.is_integer(): # if — начинается проверка условия: если...
    print("Число целое")
else: # если условие в if оказалось ложным (False), выполняется всё, что написано после else:
    print("Число не является целым")