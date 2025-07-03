# Задание 1
# Без аргумента
def say_hello():
    print("Hello")

say_hello()

# С аргументом
def say_hello(name, age, city): # это параметры функции
    print("Hello,", name + "!")
    print("You are", age, "years old.")
    print("You were born in,", city, "Nizhnevartovsk")

say_hello("Max", 25, "city")
