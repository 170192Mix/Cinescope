# Задание 1 Создайте свой модуль
# Файл: warcraft_store.py

class GoblinShop:
    def __init__(self):
        self.items = {"Зелье лечения": 100, "Зелье маны": 80, "Свиток скорости": 150}

    def show_items(self):
        print("📜 Товары гоблина:")
        for item, price in self.items.items():
            print(f"{item}: {price} золотых")

    def buy_item(self, item_name):
        if item_name in self.items:
            print(f"✔ Вы купили {item_name} за {self.items[item_name]} золотых.")
        else:
            print("❌ Такого товара нет в наличии!")

# Файл: main.py
from warcraft_store import GoblinShop  # Импорт класса из другого модуля

# Создаем объект магазина
shop = GoblinShop()

# Показываем товары
shop.show_items()

# Покупаем товар
shop.buy_item("Зелье маны")
shop.buy_item("Артефакт магии")