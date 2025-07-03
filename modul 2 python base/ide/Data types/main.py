# Задание 2
# Импорт и использование класса
# Файл: main.py

from warcraft_store import GoblinShop  # Импорт класса из другого модуля

# Создаем объект магазина
shop = GoblinShop()

# Показываем товары
shop.show_items()

# Покупаем товар
shop.buy_item("Зелье маны")
shop.buy_item("Артефакт магии")