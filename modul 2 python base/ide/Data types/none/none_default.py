# Использование None как значения по умолчанию
# Задание 1
def calculate_discount(price, discount=None): # Определяем функцию с двумя параметрами: price и discount
    if discount is None: # Если discount не задан (равен None), устанавливаем скидку 5%
        discount = 0.05

    final_price = price * (1 - discount) # Вычесляем цену со скидкой

    return final_price # Возвращаем итоговую цену

print(calculate_discount(1000))
print(calculate_discount(1000, 0.1))

# Задание 2
def add_to_list(item, my_list=None):
    if my_list is None: # Если список не передан (None), создаём новый пустой список
        my_list = []

    my_list.append(item) # Добавляем элемент item в список

    return my_list # Возвращаем обновлённый список

result1 = add_to_list("Яблоко") # Вызов без существующего списка
print(result1)

existing_list = ["банан", "груша"] # Вызов с уже существующим списком
result12 = add_to_list("апельсин", existing_list)
print(result12)
print(existing_list) # Проверяем, изменился ли оригинальный список

# Задание 3
def send_email(subject, body, recipient=None): # Определяем функцию send_email
    if recipient is None: # Если получатель не указан, устанавливаем его по умолчанию
        recipient = "support@example.com"

    print(f"Отправка письма...") # Выводим информацию о письме
    print(f"Тема: {subject}")
    print(f"Текст: {body}")
    print(f"Получатель: {recipient}")

send_email("Ошибка на сайте", "Появляется ошибка 404 на главной странице.") # Вызов без указания получателя

print() # Просто для отделения выводов

send_email("Поздравление", "С наступающим праздником!", "friend@example.com")