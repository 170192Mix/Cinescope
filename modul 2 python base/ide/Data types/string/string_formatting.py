# Вставка значений в строку
# Задание 1
name = "Дмитрий"
age = 28
greeting_f = f"Привет, меня завут {name}, и мне {age}" # Вставьте значения переменных name и age в строку с помощью f-строки
print(greeting_f)

# Задание 2
city = "Москва"
temperature = 15.5

weather_format = "В городе {}, сейчас {} градусов тепла".format(city, age) # Вставляем значения переменных city и temperature в строку с помощью метода .format()
print(weather_format)

# Задание 3
product = "ноутбук"
price = 54999

product_info_percent = "Товар: %s, Цена: %d руб." % (product, price) # Использование %s вставляет строку, а %d — целое число.
print(product_info_percent)