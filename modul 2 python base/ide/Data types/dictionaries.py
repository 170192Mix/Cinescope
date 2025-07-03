# Вложенные словари
# Задание 1
personal_info = { # Создаём словарь с персональными данными
    "name": "Богдан",
    "age": 29,
    "email": "stik@gmail.com"
}

copied_info = personal_info.copy() # Копируем словарь с помощью метода copy()

assert personal_info == copied_info, "Словари не совпадают!" # Сравниваем оба словаря с помощью assert

print(copied_info)

# Задание 2
personal_info = {
    "name": "Алексей",
    "age": 28,
    "email": "aleksey@example.com"
}
personal_info["phone"] = "79781234533" # Добавляем новую пару ключ-значение — номер телефона

print("Оригинальный номер:", personal_info["phone"]) # Выводим номер телефона на экран

original_phone = personal_info["phone"] # Перезаписываем номер, скрывая часть цифр (фильтрация)
filtered_phone = original_phone[:3] + "*****" + original_phone[-2:] # Оставим только первые 3 и последние 2 цифры

personal_info["phone"] = filtered_phone

# Задание 3
address_info = { # Вложенный словарь с адресом
    "city": "Санкт-Петербург",
    "street": "Невский проспект",
    "house": "д. 12"
}
personal_info["address"] = address_info # Объединяем: добавляем вложенный словарь в основной

print("Город проживания:", personal_info["address"]["city"])
