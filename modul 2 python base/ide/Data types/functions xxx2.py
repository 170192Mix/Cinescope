# Базовые функции с логикой (без параметров), без return:
# 1
def print_even_number(n):
    print(n, end=' ') # печатаем n в одну строку.


for i in range(2, 20): # range - создаёт последовательность
    if i % 2 == 0: # проверка: число чётное.
        print_even_number(i)

# 2
for i in range(10, 0, -1): # range - создаёт последовательность
    print(i, end=' ')

# 3
def print_alphabet():
    alphabet = "abcdefghijklm" # англ. алфавит
    print(alphabet[:5]) # срез: первые 5 букв

print_alphabet()

# 4
def print_multiplication_table():
    for i in range(1, 6): # от 1 до 5 включительно, range - создаёт последовательность
        print(f"2 x {i} = {2 * i}")

print_multiplication_table()

# 5
def print_triangle():
    for i in range(1, 6): # от 1 до 5, range - создаёт последовательность
        print('*' * i)

print_triangle()

# с return:
# 1
def sum_first_ten():
    total = 0
    for i in range(1, 10):
        total += i # добавляем каждое число к общей сумме
    return total

print(sum_first_ten())

# 2
def count_vowels_in_hello(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    result = ''
    for char in text:
        if char in vowels:
            result += char
    return result

print(count_vowels_in_hello("Тестирование"))

# 3
get_max_from_list = [1, 5, 3, 9, 2]
maximum = max(get_max_from_list)
print("Максимальное число:", maximum)

# 4
def calculate_area_of_square():
    side = 4 # side — длина стороны квадрата
    return side * side # это формула площади

print(calculate_area_of_square())

# 5
def get_length_of_alphabet(alphabet):
    return len(alphabet)

alphabet = "абвгдеёжзийклмнопрстуфхцчш"
count = get_length_of_alphabet(alphabet)
print("Количество чисел:", count)