# Класс и объект

class Dog:
    def __init__(self, name, breed):
        self.name = name  # Атрибут объекта
        self.breed = breed  # Атрибут объекта

    def bark(self):
        return f"{self.name} говорит: Гав-гав!"

# Создание объекта
my_dog = Dog("Бобик", "Дворняга")

# Доступ к атрибутам и методам
print(my_dog.name)  # Бобик
print(my_dog.breed)  # Дворняга
print(my_dog.bark())  # Бобик говорит: Гав-гав!

# ---

class House:
    def __init__(self, floors, roof, material):
        self.floors = floors  # Количество этажей
        self.roof = roof      # Тип крыши
        self.material = material  # Материал стен

# Создаем два объекта дома
house1 = House(2, "черепичная", "кирпич")
house2 = House(1, "металлическая", "дерево")

print("Дом 1:", house1.floors, "этажа,", "крыша:", house1.roof, "материал:", house1.material)
print("Дом 2:", house2.floors, "этаж,", "крыша:", house2.roof, "материал:", house2.material)

# Инкапсуляция в классе Product

class Product:
    def __init__(self, name, price):
        self.name = name  # Открытый атрибут
        self.__price = price  # Приватный атрибут

    # Геттер для получения значения атрибута price
    @property
    def price(self):
        return self.__price

    # Сеттер для изменения значения атрибута price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self.__price = value

# Использование
product = Product("Ноутбук", 50000)

# Доступ к открытому атрибуту
print(product.name)  # Ноутбук

# Попытка получить доступ к приватному атрибуту (будет ошибка)
# print(product.__price)

# Работа с приватным атрибутом через геттер и сеттер
print(product.price)  # 50000
product.price = 45000  # Изменение цены
print(product.price)  # 45000

# Попытка установить некорректную цену
# product.price = -100  # ValueError: Цена не может быть отрицательной!



