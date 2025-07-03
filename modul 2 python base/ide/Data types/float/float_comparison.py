# Приблизительное равенство — функция math.isclose()
# Задание 1
import math # Подключаем модуль math - чтобы получить полный доступ к этим функциям

x = 1.000001
y = 1.000002

print(math.isclose(x, y))

# Задание 2
price1 = 19.999
price2 = 20.0

is_close_strict = math.isclose(price1, price2, rel_tol=1e-5) # Сравнение с очень строгой точностью (rel_tol=1e-5)
is_close_loose = math.isclose(price1, price2, rel_tol=1e-3) # Сравнение с более мягкой точностью (rel_tol=1e-3)

print(is_close_strict)
print(is_close_loose)

# Задание 3
distance1 = 150.002
distance2 = 150.003

distance1_siring = math.isclose(distance1, distance2, abs_tol=0.001) # Сравниваем эти два числа с помощью math.isclose(), но теперь используем абсолютную точность (abs_tol)

print(distance1_siring)