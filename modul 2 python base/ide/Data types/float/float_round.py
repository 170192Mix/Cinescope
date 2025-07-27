# Округление — функция round()
# Задание 1
value = 3.14159

rounded_value = round(value, 2) # Используем функцию round() для округления value до двух знаков после запятой
print(rounded_value)

# Задание 2
price = 19.999

rounded_price = round(price) # Используем функцию round() для округления price до целого числа
print(rounded_price)

# Задание 3
grades = [89.9, 92.75, 88.6, 91.3]

rounded_grades = [] # Создаём пустой список, куда будем складывать округлённые оценки

for grade in grades: # Запускаем цикл: который будет перебирать каждую оценку из исходного списка
    rounded_grade = round(grade, 1) # Округляем текущее значение grade до 1 знака после запятой
    rounded_grades.append(rounded_grade) # Добавляем округлённое значение в новый список rounded_grades
    print(rounded_grades)