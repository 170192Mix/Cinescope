# Задание 1
# 1
class Animal: # это шаблон (чертёж).
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} издаёт звук.")

# 2
cat = Animal("Кошка")
dog = Animal("Собака")

cat.speak()   # Кошка издаёт звук.
dog.speak()   # Собака издаёт звук.

# Динамическое добавление атрибутов, изменение атрибутов
# Задание 1
# Создаём класс Book с атрибутами title, author, pages
class Book:
    def __init__(self, title, author, pages):
        self.title = title  # Название книги
        self.author = author  # Автор книги
        self.pages = pages  # Количество страниц

    # Метод info должен быть внутри класса, на том же уровне отступов, что и __init__
    def info(self):
        print("Название:", self.title)
        print("Автор:", self.author)
        print("Количество страниц:", self.pages)

# 2. Создаём объект на основе класса
my_book = Book("Мать", "Максим Горький", 240)

# 3. Вызов метода info
my_book.info()

# 4. Изменение названия
my_book.title = "Три товарища"
print("\nОбновленное название:", my_book.title)

# 5. Добавление нового атрибута
my_book.genre = "Роман"
print("Жанр:", my_book.genre)