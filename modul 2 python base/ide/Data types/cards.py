# Кортежи
# Задание 1
my_tuple = (10, 20, 30, 40)
print("оригинальный кортеж", my_tuple)

# Кортеж с данными
data_tuple = ("Иван", 30, "ivan@example.com")

copied_tuple = ("Иван", 30, "ivan@example.com") # Создаём второй кортеж с теми же значениями
assert data_tuple == copied_tuple, "Кортежи не совпадают!" # Сравниваем кортежи с помощью assert

print("Кортеж:", data_tuple)

fruits = ("apple", "banana", "cherry", "apple")

first_index = fruits.index("apple")
apple_count = fruits.count("apple") # Посчитать, сколько раз встречается "apple"

print("Индекс первого вхождения 'apple':", first_index)
print("Количество вхождений 'apple':", apple_count)

a, b, *rest = fruits # Распаковка: "apple" -> a, "banana" -> b, остальные элементы -> rest

tuple_2 = tuple(rest) # Создаём кортеж из оставшихся элементов
assert len(tuple_2) == 2, f"Ошибка: длина tuple_2 должна быть 2, а не {len(tuple_2)}" # Проверка длины кортежа с помощью assert

print("a =", a)
print("b =", b)
print("tuple_2 =", tuple_2)

# Уникальность значений множества
colors = ["red", "blue", "green", "red"]
colors_set = set(colors)
print(colors_set)

# Добавление и удаление элементов в множество
# Создаём множество из 4-х элементов
my_set = {10, 20, 30, 40}
print("Исходное множество:", my_set)

# Добавляем новый элемент
my_set.add(50)
print("После добавления 50:", my_set)

# Добавляем уже существующий элемент (например, 30)
my_set.add(30)
print("После повторного добавления 30 (уже есть):", my_set)
# Повторный элемент не добавляется — множество хранит только уникальные значения

# Попытка удалить несуществующий элемент методом remove()
try:
    my_set.remove(99)
except KeyError as e:
    print("Ошибка при remove(99):", e)

# Попытка удалить несуществующий элемент методом discard(). discard() не вызывает ошибку, если элемента нет
my_set.discard(99)
print("После discard(99):", my_set)

# Удаление случайного элемента методом pop()
for i in range(3):
    random_set = {100, 200, 300, 400, 500}
    popped = random_set.pop()
    print(f"Попытка {i+1}: Удалённый элемент: {popped}, оставшееся множество: {random_set}")

# Объединение множеств
num1 = {1, 2, 3}
num2 = {3, 4, 5}

union_set = num1 | num2
print(union_set)

# Практическое задание
list1 = [10, 20, 30, 40, 50]
list2 = [20, 25, 30, 35, 40]

set1 = set(list1) # Преобразуем в множества
set2 = set(list2)

difference = set1.difference(set2) # Разность множеств
difference_list = list(difference) # Если нужно обратно в список

print("Разность:", difference_list)

# Диапазоны range
r = range(2, 6) # Начинаем с 2 идем до 6 не включая 6
print(list(r))

r = range (2, 10, 2) # Начинаем с 2 идем до 10 не включая 10. Пропускаем 1 на каждом шаге
print(list(r))

r = range(10, 2, -2) # Идем с 10 доходим до 2 не включая 2. с -2 движемся в обратную сторрону
print(list(r))

r = range(10, 2) # Начинаем с 10 доходим до 2 не включая 2. Но шаг по умолчанию положительный
print(list(r))