# Здание 1
class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    # --- TITLE ---
    @property # Делает метод доступным как обычное свойство (book.title, а не book.title())
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value # self._title Скрытые (приватные) переменные

    # --- AUTHOR ---
    @property # Делает метод доступным как обычное свойство (book.title, а не book.title())
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value # self._author Скрытые (приватные) переменные

    # --- PAGES ---
    @property # Делает метод доступным как обычное свойство (book.title, а не book.title())
    def pages(self):
        return self._pages

    @pages.setter # Включает проверку: если pages < 0, не даёт установить и выводит ошибку
    def pages(self, value):
        if value < 0:
            print("Количество страниц не может быть отрицательным.")
        else:
            self._pages = value # self._pages Скрытые (приватные) переменные

# --- Пример использования ---
book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)

print(book.title)      # Вывод: Мастер и Маргарита

book.pages = -10       # Пытаемся установить отрицательное число
print(book.pages)      # Всё ещё 384, потому что установка не сработала

book.pages = 400       # Устанавливаем корректное значение
print(book.pages)      # Теперь 400

# Задание 2
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance  # Приватный атрибут

    # --- Геттер баланса ---
    @property # Возвращает текущий баланс
    def balance(self):
        return self._balance

    # --- Сеттер баланса (только увеличение) ---
    @balance.setter # Позволяет только увеличивать баланс
    def balance(self, value):
        if value < self._balance:
            print("Операция снятия средств не поддерживается. Используйте метод withdraw().")
        else:
            self._balance = value

    # --- Метод снятия средств ---
    def withdraw(self, amount): # Позволяет снимать деньги с проверками
        if amount < 0:
            print("Сумма снятия не может быть отрицательной.")
        elif amount > self._balance:
            print("Недостаточно средств на счёте.")
        else:
            self._balance -= amount
            print(f"Снято {amount} рублей. Остаток: {self._balance}")

account = BankAccount("123456789", 1000.0)

print("Баланс:", account.balance)  # 1000.0

account.balance = 1500.0           # Пополнение — разрешено
print("Баланс:", account.balance)  # 1500.0

account.balance = 1000.0           # Попытка снять через setter — запрещено
# → "Операция снятия средств не поддерживается. Используйте метод withdraw()"

account.withdraw(-100)            # Ошибка: сумма отрицательная
account.withdraw(2000)            # Ошибка: недостаточно средств
account.withdraw(300)             # Успешно снимает
print("Баланс:", account.balance) # 1200.0

