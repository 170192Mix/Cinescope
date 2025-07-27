# Защита атрибутов
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Защищенный атрибут

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance :
            self._balance -= amount
        else:
            print("Недостаточно средств или некорректная сумма.")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(2000)
print(account.get_balance())
"""Мы можем обратиться к защищенному атрибуту напрямую, но это не рекомендуется"""
print(account._balance)  # Вывод: 1500 (но лучше использовать account.get_balance())

account._balance = -1000 #можем изменить напрямую, но это плохо
print(account.get_balance()) #вывод -1000, что недопустимо
account.withdraw(100)
print(account.get_balance()) #вывод -1100, что недопустимо

# Здание 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title  # Название книги
        self.author = author  # Автор книги
        self.pages = pages  # Количество страниц

    # ---TITLE---
    @property # Делает метод доступным как обычное свойство
    def title(self):
        return self._title

    @title.setter # setter Позволяет установить значение через book.title = "..."
    def title(self, value):
        self._title = value

    #---AUTHOR---
    @property # Делает метод доступным как обычное свойство
    def author(self):
        return self._author

    @author.setter # # setter Позволяет установить значение через book.title = "..."
    def author(self, value):
        self._author = value

    #---PAGES---
    def pages(self):
        return self._pages

    @pages.setter # Включает проверку: если pages < 0, не даёт установить и выводит ошибку
    def pages(self, value):
        if value < 0:
            print("Ошибка: количество страниц не может быть отрицательным.")
        else:
            self._pages = value

# --- Пример использования ---
book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)

print(book.title)      # Вывод: Мастер и Маргарита

book.pages = -10       # Пытаемся установить отрицательное число
print(book.pages)      # Всё ещё 384, потому что установка не сработала

book.pages = 400       # Устанавливаем корректное значение
print(book.pages)      # Теперь 400