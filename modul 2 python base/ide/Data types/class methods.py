# Задание 1
class Animal:
    def __init__(self, name, age):
        self.name = name # имя животного
        self.age = age # возраст животного

    def speak(self):
        print(f"I am an animal, my name is {self.name} and my age is {self.age}")

my_animal = Animal("Leo", 5)
my_animal.speak()

# Выводим атрибуты
my_animal.name = "Milo"
my_animal.age = 8

# Вызываем метод speak()
my_animal.speak()

# Задание 2
class NumberAnalyzer:
    def __init__(self, num1, num2): # __init__ запускается при создании объекта.
        self.num1 = num1
        self.num2 = num2

    def get_max(self):
        return max(self.num1, self.num2)

    def even_or_odd(self):
        number = self.get_max()
        if number % 2 == 0: # Если остаток от деления на 2 равен 0 (number % 2 == 0) — число чётное
            print(f"{number} — чётное число")
        else:
            print(f"{number} — нечётное число")

    def number_type(self):
        number = self.get_max()
        if number > 0:
            print(f"{number} — положительное число")
        elif number < 0:
            print(f"{number} — отрицательное число")
        else:
            print(f"{number} — это ноль")

analyzer = NumberAnalyzer(-7, 4) #  Создаём объект класса. Передаём два числа: -7 и 4.
print("Большее число:", analyzer.get_max())
analyzer.even_or_odd()  # -> 4 — чётное число
analyzer.number_type()  # -> 4 — положительное число

# Задача 1 Создать программу, моделирующую работу учетной системы
class Account:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.") # ... выбрасываем ошибку, программа дальше не пойдёт

        self.name = name
        self.balance = balance

    def deposit(self, amount): # Проверяет, что сумма > 0 и прибавляет её к балансу
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount
        print(f"{self.name} пополнил счёт на {amount} рублей. Новый баланс: {self.balance}")

    def withdraw(self, amount): # Проверяет, что сумма > 0 и есть достаточно денег — если да, вычитает
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            print(f"Недостаточно средств! Баланс: {self.balance}, попытка снять: {amount}")
        else:
            self.balance -= amount
            print(f"{self.name} снял {amount} рублей. Остаток на счёте: {self.balance}")

    def __str__(self):
        return f"Счёт {self.name}: {self.balance} рублей"