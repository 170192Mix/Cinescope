# Задание 1
has_ticket = True
has_passport = True

can_board_plane = has_ticket and has_passport
print(can_board_plane)

# Задание 2
is_adult = True
has_permission = True

can_access_content = is_adult and has_permission
print(can_access_content)

# Задание 3
num1 = int(input("Ввидите первое число: "))
num2 = int(input("Ввидите первое число: "))
# Проверяем, оба ли числа больше 10
# Оператор 'and' возвращает True только если оба условия истинны
both_greater_than_10 = num1 > 10 and num2 > 10
print("Оба числа больше 10:", both_greater_than_10)
