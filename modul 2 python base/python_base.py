print("Hello World")

city = "Москва"
sub_string = city[0:3]  # 'Мос'
print(sub_string)

# Задание 1
# Создание переменных разных типов
number_int = 10          # целое число (int)
number_float = 3.14      # число с плавающей точкой (float)
is_active = True         # логическое значение (bool)
text = "Привет, мир!"     # строка (str)

# Вывод всех переменных
print("Целое число:", number_int)
print("Число с плавающей точкой:", number_float)
print("Логическое значение:", is_active)
print("Текст:", text)

# Задание 2
my_text = "Hello, Python!" # Создаём переменную типа str
print(type(my_text)) # Выводим тип переменной, передавая её в функцию type(), а результат — в print()

# len(list): возвращает длину списка
my_list = [1, 2, "крыша", False]
length = len(my_list)
print(length)  # 4

# Добавление элемента
# append
fruits = ["яблоко", "банан", "вишня"]
fruits.append("апельсин")
print(fruits) # ["яблоко", "банан", "вишня", "апельсин"]

# insert
fruits = ['банан', 'яблоко']
fruits.insert(1, 'апельсин')
print(fruits)  # ['банан', 'апельсин', 'яблоко']

# extend
fruits = ['банан', 'яблоко']
fruits.extend(['груша', 'апельсин', 'вишня'])
print(fruits)  # ['банан', 'яблоко', 'груша', 'апельсин', 'вишня']

# Получение индекса элемента
# index
fruits = ['банан', 'яблоко', 'апельсин']
index = fruits.index('апельсин')
print(index)

###

fruits = ['банан', 'яблоко', 'апельсин']
index = fruits.index('такого элемента нет в списке')
print(index)
# ValueError: 'такого элемента нет в списке' is not in list