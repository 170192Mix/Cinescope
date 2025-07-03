class Account:
    def __init__(self, name, balance):
        if balance < 0: # Если начальный баланс меньше нуля — выдаём ошибку и не создаём объект.
            raise ValueError("Начальный баланс не может быть отрицательным.")

        self.name = name
        self.balance = balance

    def deposit(self, amount): # Метод deposit() — пополнение счёта
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount
        print(f"{self.name} пополнил счёт на {amount} рублей. Новый баланс: {self.balance}")

    def withdraw(self, amount): # Метод withdraw() — снятие денег
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            print(f"Недостаточно средств! Баланс: {self.balance}, попытка снять: {amount}")
        else:
            self.balance -= amount
            print(f"{self.name} снял {amount} рублей. Остаток на счёте: {self.balance}")

    def __str__(self): #  Метод __str__() — как объект выглядит при print()
        return f"Счёт {self.name}: {self.balance} рублей"

# Дочерний класс
class SavingsAccount(Account): # Создаём класс SavingsAccount, который наследует всё из Account.
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)  # вызывает родительский (Account) конструктор
        self.interest_rate = interest_rate  # добавляет процент на остаток как новый атрибут

    def withdraw(self, amount): # Расширенный метод withdraw() с минимальным остатком
        MIN_BALANCE = 100
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if self.balance - amount < MIN_BALANCE:
            print(f"Нельзя снять {amount} рублей — на счёте должен остаться минимум {MIN_BALANCE} рублей.")
        else:
            self.balance -= amount
            print(f"{self.name} снял {amount} рублей. Остаток на счёте: {self.balance}")

# Создание сберегательного счёта
savings = SavingsAccount("Ирина", 1000, 0.05)

# Пополнение
savings.deposit(300)

# Снятие, которое разрешено
savings.withdraw(500)  # Баланс останется 800

# Снятие, которое не разрешено (меньше минимального остатка)
savings.withdraw(750)  # Ошибка: меньше 100 рублей останется

# Вывод информации
print(savings)
print(f"Процентная ставка: {savings.interest_rate * 100}%")
