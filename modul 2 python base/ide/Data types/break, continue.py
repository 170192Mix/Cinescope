# Вывод нечётных чисел от 1 до 10
number = 1
while number <= 10:
    if number % 2 != 0:
        print(number)
    number += 1

# Оператор break
for num in range(1, 10):
    if num == 5:
        break  # Завершение цикла
    print(num)