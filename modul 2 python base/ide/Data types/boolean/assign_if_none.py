# Присвоение значения, если переменная None
# Задание 1
city = None
capital_city = "Москва" # Присваиваем значение
city = city or capital_city # Если она равна None, используя оператор or
print(city)

# Задание 2
language = None
programming_language = "Python"
language = language or programming_language
print(language)

# Задание 3
user_name = None
user_name = user_name or "Guest"
print(user_name)