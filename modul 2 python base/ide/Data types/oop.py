# Задание 1: Зелье восстановления Тема: Функции

def restore_health(current_health, potion):
    max_health = 100
    new_health = current_health + potion
    if new_health > max_health:
        new_health = max_health
    return new_health

# Пример использования
print(restore_health(90, 15))  # Вывод: 100
print(restore_health(50, 30))  # Вывод: 80

# Задание 2: Гоблинский торговец Тема: Методы класса

class GoblinTrader:
    def __init__(self, gold):
        self.gold = gold

    def buy_item(self, item_name, item_price):
        if self.gold >= item_price:
            self.gold -= item_price
            print(f"Куплен {item_name}")
        else:
            print("Недостаточно золота")

# Пример использования
trader = GoblinTrader(200)
trader.buy_item("Свиток скорости", 150)  # Вывод: Куплен Свиток скорости
trader.buy_item("Книга заклинаний", 100)  # Вывод: Недостаточно золота!

# Задание 2.1: Гоблинский торговец (Методы класса и статические методы)
# Тема: Методы класса, статические методы, операции с золотом

class GoblinMerchant: # определение класса
    def __init__(self, gold):
        self.gold = gold

    @staticmethod # метод, не использует self или cls
    def tax_rate(): # Статический метод: не зависит от конкретного объекта
        return 0.1 # Возвращает налоговую ставку 10%

    @classmethod # получает cls вместо self
    def from_rich_merchant(cls): # Метод класса: принимает сам класс в качестве первого аргумента
        return cls(1000) # Создаёт "богатого" гоблина с 1000 золота

    def buy_item(self, item_name, item_price):  # Метод покупки предмета
        total_price = item_price + item_price * self.tax_rate() # Вычисляем полную цену с налогом
        if self.gold >= total_price: # Если золота хватает
            self.gold -= total_price # Вычитаем из баланса
            return f"Куплен {item_name}" # Покупка прошла успешно
        else:
            return "Недостаточно золота!" # Покупка не удалась

merchant = GoblinMerchant(200)
print(merchant.buy_item("Амулет удачи", 150))  # Ожидается успешная покупка или недостаток золота
rich_merchant = GoblinMerchant.from_rich_merchant()
print(rich_merchant.buy_item("Волшебный посох", 500))  # Ожидается успешная покупка

# Задание 3: Боец и маг Тема: Наследование

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")

class Warrior(Hero):
    def attack(self):
        return "Нанёс 20 урона мечом"

class Mage(Hero):
    def attack(self):
        return "Нанёс 15 урона заклинанием"

# Пример использования
warrior = Warrior("Тралл", 120)
mage = Mage("Джайна", 80)

print(warrior.attack())  # Вывод: Нанёс 20 урона мечом
print(mage.attack())     # Вывод: Нанёс 15 урона заклинанием

# Задание 4: Задание на полиморфизм
# Тема: Полиморфизм.

class Peon:
    def work(self):
        return "Собирает золото"

class Knight:
    def work(self):
        return "Сражается с врагами"

def daily_work(hero):
    print(hero.work())

# Пример использования
peon = Peon()
knight = Knight()

daily_work(peon)   # Вывод: Собирает золото
daily_work(knight) # Вывод: Сражается с врагами

# Задание 5: Секретные артефакты Тема: Абстракция.
# Тема: Абстракция.

from abc import ABC, abstractmethod

class Artifact:
    @abstractmethod
    def activate(self):
        pass
class HealingArtifact(Artifact):
    def activate(self):
        pass

class DamageArtifact(Artifact):
    def activate(self):
        return "Нанесено 30 урона врагу"

# Пример использования
heal_artifact = HealingArtifact()
damage_artifact = DamageArtifact()

print(heal_artifact.activate())  # Вывод: Восстановлено 50 здоровья
print(damage_artifact.activate()) # Вывод: Нанесено 30 урона врагу

# Задание 6: Гоблинский банк
# Тема: Инкапсуляция.

class GoblinBank:
    def __init__(self, initial__gold):
        if initial__gold < 0:
            raise ValueError("Начальное количество золота не может быть отрицательным!")
        self.__gold = initial__gold # Приватный атрибут для хранения золота

    def get_gold(self): # Геттер для получения количества золота
        return self.__gold

    def deposit_gold(self, amount): # Геттер для получения количества золота
        if amount > 0:
            self.__gold += amount
            print(f"Добавлено {amount} золота. Текущий баланс: {self.__gold}")
        else:
            print("Сумма должна быть больше 0!")

    def withdraw_gold(self, amount): # Метод для снятия золота
        if amount > self.__gold:
            print("Недостаточно золота!")
        elif amount > 0:
            self.__gold -= amount
            print(f"Снято {amount} золота. Текущий баланс: {self.__gold}")
        else:
            print("Сумма должна быть больше 0!")

# Пример использования
bank = GoblinBank(100)

print(bank.get_gold())  # Вывод: 100
bank.deposit_gold(50)   # Вывод: Добавлено 50 золота. Текущий баланс: 150
bank.withdraw_gold(30)  # Вывод: Снято 30 золота. Текущий баланс: 120
bank.withdraw_gold(200) # Вывод: Недостаточно золота!