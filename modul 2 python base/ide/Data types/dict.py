# Задание 1
menu = {
    "Пицца": 600,
    "Паста": 450,
    "Борщ": 300,
    "Салат Цезарь": 550
}

menu["Карпачо"] = 1500 # menu["Карпачо"] = 1500 — добавление нового блюда

print("Меню с добавленным блюдом:")
for dish, price in menu.items():
    print(f"{dish}: {price} руб.")

menu["Карпачо"] = 1100 # menu["Карпачо"] = 1100 — обновление цены.

print("\nОбновлённое меню (после изменения цены Карпачо):")
for dish, price in menu.items(): # for dish, price in menu.items() — перебор и вывод всех пунктов меню
    print(f"{dish}: {price} руб.")

# Задание 2
# Словарь с товарами и ценами
products = {"яблоко": 100, "банан": 50, "апельсин": 70}

# Первый случай: товар есть
order = "яблоко"

if order in products:
    print(f"Цена товара '{order}': {products[order]} руб.")
else:
    print("У нас нет такого товара.")

# Второй случай: товар отсутствует
order = "черви"

if order in products:
    print(f"Цена товара '{order}': {products[order]} руб.")
else:
    print("У нас нет такого товара.")
