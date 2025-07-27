# Наследование
# Базовый класс

class Hero:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} бежит")

    def fight(self):
        print(f"{self.name} борется с врагом")

# Дочерний класс
class SpiderMan(Hero):  # Наследуем класс Hero
    def shoot_web(self):
        print(f"{self.name} выпускает паутину")

# Создаём героя
hero = SpiderMan("Человек-Паук")
hero.run()  # Человек-Паук бежит
hero.fight()  # Человек-Паук борется с врагом
hero.shoot_web()  # Человек-Паук выпускает паутину

# Пример из жизни
# Родительский класс

class Animal:
    def breathe(self):
        print("Дышит")

    def eat(self):
        print("Ест")

# Дочерний класс
class Bird(Animal):  # Наследуем класс Animal
    def fly(self):
        print("Летит")

# Создаём птицу
sparrow = Bird()
sparrow.breathe()  # Дышит
sparrow.eat()  # Ест
sparrow.fly()  # Летит

# Пример на Python: Наследование


# Родительский класс
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издаёт звук."

# Дочерний класс Dog
class Dog(Animal):
    def speak(self):
        return f"{self.name} лает."

# Дочерний класс Cat
class Cat(Animal):
    def speak(self):
        return f"{self.name} мяукает."

# Создаем объекты
dog = Dog("Барбос")
cat = Cat("Мурзик")

# Вызываем методы
print(dog.speak())  # Барбос лает.
print(cat.speak())  # Мурзик мяукает.

# Полиморфизм

class Instrument:
    def play(self):
        raise NotImplementedError("Метод должен быть переопределён в дочернем классе")

class Piano(Instrument):
    def play(self):
        print("Пианино играет мелодию")

class Guitar(Instrument):
    def play(self):
        print("Гитара играет аккорды")

class Drums(Instrument):
    def play(self):
        print("Барабаны задают ритм")

# Оркестр
instruments = [Piano(), Guitar(), Drums()]

for instrument in instruments:
    instrument.play()

# Пример из жизни

class Delivery:
    def deliver(self):
        raise NotImplementedError("Метод должен быть переопределён в дочернем классе")

class Car(Delivery):
    def deliver(self):
        print("Доставляет на машине")

class Bike(Delivery):
    def deliver(self):
        print("Доставляет на велосипеде")

class Drone(Delivery):
    def deliver(self):
        print("Доставляет на дроне")

# Система доставки
vehicles = [Car(), Bike(), Drone()]

for vehicle in vehicles:
    vehicle.deliver()

# Пример на Python: Полиморфизм
# Родительский класс

class Animal:
    def speak(self):
        return "Животное издаёт звук."

# Дочерний класс Dog
class Dog(Animal):
    def speak(self):
        return "Собака лает."

# Дочерний класс Cat
class Cat(Animal):
    def speak(self):
        return "Кошка мяукает."


# Общая функция для работы с животными
def make_sound(animal):
    print(animal.speak())

# Создаем объекты
dog = Dog()
cat = Cat()

# Используем один метод для разных объектов
make_sound(dog)  # Собака лает.
make_sound(cat)  # Кошка мяукает.