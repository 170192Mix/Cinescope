# Базовые функции (с return и без return)
# 1
def say_hello():
    print("Привет")

say_hello()

# 2
def print_stars():
    print("*****")

print_stars()

# 3
def print_line():
    print("2" * 20)

print_line()

# 4
def goodbye():
    print("До свидания!")

goodbye()

# Задачи с return:
# 1
def get_my_name():
    name = "Максим"
    return name # Возвращаем кортеж

person_info = get_my_name()
print(person_info) # Вывод: Максим

# 2
def get_lucky_number():
    number = 7
    return number # возвращает число

print(get_lucky_number())

# 3
def get_greeting():
    we_are_glad_to_see_you = "Добро пожаловать"
    return we_are_glad_to_see_you

info_you = get_greeting()
print(get_greeting())