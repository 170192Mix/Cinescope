# Округление вниз и вверх — функции math.floor() и math.ceil()
# Задание 1
import math # Подключаем модуль math - чтобы получить полный доступ к этим функциям

price = 19.99

rounded_down = math.floor(price) # Округляем вниз до целого числа с помощью функции math.floor
rounded_up = math.ceil(price) # Округляем вверх до целого числа с помощью функции math.ceil

print(rounded_down)
print(rounded_up)

# Задание 2
height = 175.45

height_floor = math.floor(height) # Округляем вниз до целого числа с помощью функции math.floor
height_ceil = math.ceil(height) # Округляем вверх до целого числа с помощью функции math.ceil

print(height_floor)
print(height_ceil)

# Задание 3
score = 88.8

score_floor = math.floor(score) # Округляем вниз до целого числа с помощью функции math.floor
score_ceil = math.ceil(score) # Округляем вверх до целого числа с помощью функции math.ceil

print(score_floor)
print(score_ceil)