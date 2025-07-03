# Создаём переменную
number = 7  # можно заменить на любое число

# Проверяем с помощью if-else
if number % 2 == 0: # number % 2 вычисляет остаток от деления.
    print("Число чётное")
else:
    print("Число нечётное")

temperature = 120

if temperature < 0:
    print("Вода замёрзла (лёд)")
elif 0 <= temperature < 100:
    print("Вода жидкая")
elif temperature == 100:
    print("Вода закипела")
else:
    print("Вода в состоянии пара")

# Переменная с числом
number = 0

# Проверка условий
if number == 0:
    print("Число равно нулю")
elif number % 2 == 0 and number > 0:
    print("Чётное и положительное")
elif number % 2 == 0 and number < 0:
    print("Чётное и отрицательное")
elif number % 2 != 0 and number > 0:
    print("Нечётное и положительное")
elif number % 2 != 0 and number < 0:
    print("Нечётное и отрицательное")

# Переменные с числами
# Задание 1
a = 10
b = 7

if a > b: # Сравнение чисел
    print("Первое число больше:", a) # Первое число больше: 10
elif b > a:
    print("Второе число больше:", b) # Второе число больше: 9
else:
    print("Оба числа равны:", a) # Оба числа равны: 5

# Задание 2
used_logins = ["user123", "hacker", "test_bot"]

new_login = "user123" # Пробуем логин, который уже занят
if new_login in used_logins: # Проверяем, содержится ли new_login в списке used_logins
    print("Логин уже используется.")
else:
    print("Логин свободен.")

new_login = "cool_user" # Теперь логин уникален, не входит в список used_logins
if new_login in used_logins: # Снова проверяем: есть ли логин в списке
    print("Логин уже используется.")
else:
    print("Логин свободен.")