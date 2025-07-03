temperature = 100

if temperature < 0:
    print("Вода замёрзла (лёд)")
elif 0 <= temperature < 100:
    print("Вода жидкая")
elif temperature <= 100:
    print("Вода закипела")
else:
    print("Вода в состоянии пара")

# if-elif-else для проверки переменной day, чтобы вывести:
day = int(input("Введите номер дня недели (1-7): "))

if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 6 or day == 7:
    print("Выходной")
else:
    print("Другой день недели")
