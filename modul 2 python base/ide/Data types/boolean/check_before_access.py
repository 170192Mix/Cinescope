# Проверка перед доступом к объекту
# Задание 1
employee = None
if employee is not None: # Проверяем, если employee существует (не равен None)
    print(employee.name)
else:
    print("Сотрудник не найден")

# Задание 2
car = None
if car is not None: # Проверяем, если employee существует (не равен None)
    print(car.model)
else:
    print("Автомобиль не указан")

# Задание 3
book = None
if book is not None: # Проверяем, инициализирована ли переменная book
    print(book.title) # Если есть объект book, выводим его атрибут title
else:
    print("Книга не найдена")