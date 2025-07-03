# Задание 1
is_raining = True
has_umbrella = False

can_go_outside = not is_raining or has_umbrella # Можно ли выйти на улицу

print("Можно выйти на улицу:", can_go_outside)

# Задание 2
is_hungry = True
has_snack = False

can_eat_now = is_hungry or has_snack

print("Голоден или перекусывает:", can_eat_now)

# Задание 3
# Запращиваем у пользователя первое число и преобразуем его в целое число
num1 = int(input("Введите первое число: "))

# Запрашиваем у пользователя второе число и преобразуем его в целое число
num2 = int(input("Введите второе число: "))

# Проверяем, больше ли первое число 50 ИЛИ второе число меньше 30
# Оператор 'or' возвращает True, если хотя бы одно из условий истинно
condition = num1 > 50 or num2 < 30

# Выводим результат логического выражения
print("Результат проверки:", condition)

