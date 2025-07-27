from abc import ABC, abstractmethod

# Абстрактный базовый класс
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

# Подкласс Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return "Рисуем круг"

    def area(self):
        return 3.14 * self.radius ** 2

# Подкласс Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return "Рисуем прямоугольник"

    def area(self):
        return self.width * self.height

circle = Circle(5)
print(circle.draw())        # Рисуем круг
print(circle.area())        # 78.5

rect = Rectangle(4, 6)
print(rect.draw())          # Рисуем прямоугольник
print(rect.area())          # 24

# Создание приложения для интернет-магазина

class Product: #Создаём класс для одного товара — у него будет имя и цена.
    def __init__(self, name, price): # Конструктор: вызывается при создании товара.
        self.name = name # Сохраняем имя и цену как свойства объекта.
        self.price = price

class Cart: # Это класс для корзины покупателя. В неё будем добавлять товары.
    def __init__(self):
        self.items = [] # создаём пустой список items

    def add_product(self, product, quantity): # Добавляем товар в корзину
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self): # Считаем общую сумму корзины
        return sum(item["product"].price * item["quantity"] for item in self.items)

class Order: # Класс для оформления заказа на основе корзины.
    def __init__(self, cart):
        self.cart = cart
        self.status = "Pending"

    def complete_order(self): # Метод complete_order - Считаем итоговую сумму заказа через метод корзины, Меняем статус на "Completed", Возвращаем строку с финальной стоимостью
        total = self.cart.calculate_total()
        self.status = "Completed"
        return f"Заказ завершён. Итоговая стоимость: {total} рублей"

# Пример использования
laptop = Product("Laptop", 1000) # Создаём два товара: ноутбук за 1000 и мышку за 50.
mouse = Product("Mouse", 50)

cart = Cart() # Создаём пустую корзину
cart.add_product(laptop, 1) #  Добавляем 1 ноутбук и 2 мышки в корзину.
cart.add_product(mouse, 2)

order = Order(cart) # Создаём заказ на основе текущей корзины.
print(order.complete_order())  # Итоговая стоимость: 1100 рублей

