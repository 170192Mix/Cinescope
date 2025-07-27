# Удаление лишних пробелов
# Задание 1
greeting = "   Добрый день!   "
cleaned_greeting = greeting.strip() # Удаляем пробелы в начале и в конце строки с помощью метода strip()
print(cleaned_greeting)

left_trimmed = greeting.lstrip()
print(left_trimmed)

right_trimmed = greeting.rstrip()
print(right_trimmed)

# Задание 2
text  = "  Учимся Python.   "
new_text = text.strip() # удаляем пробелы слева и право
print(new_text)

# Задание 3
sentence = "   Python   - это  круто!   "
lew_sentence = sentence.lstrip() # удаляем пробелы слевой стороны
print(lew_sentence)

single_spaced_sentence = sentence.replace("  ", " ")
print(single_spaced_sentence)
