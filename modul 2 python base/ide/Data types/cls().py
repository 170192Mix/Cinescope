# Задача 1
class CurrencyConverter: # шаблон (класс) для валютного конвертера.
    def usd_to_eur(self, amount): # Это метод класса. Он принимает amount — сумму в долларах.
        return amount * 0.85

    def eur_to_usd(self, amount): #  А это обратный метод: сумма в евро → умножается на 1.18 → получаем доллары.
        return amount * 1.18

converter = CurrencyConverter()

print(converter.usd_to_eur(100))  # Вывод: 85.0
print(converter.eur_to_usd(100))  # Вывод: 118.0

# Защита атрибутов
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # защищённый атрибут начинается с "_"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостаточно средств или некорректная сумма.")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)            # +500 → 1500
account.withdraw(2000)          # Недостаточно средств
print(account.get_balance())    # 1500