# Разделение и объединение строк
# Задание 1
sentence = "Python - это весело!"
words = sentence.split() # Разделите строку по пробелам с помощью split()
print(words)

rejoined_sentence = " ".join(words) # Объедините words обратно в строку с пробелами между словами, используя join()
print(rejoined_sentence)

# Задаине 2
data = "яблоко,банан,вишня,груша"
fruits = data.split(",") # Разделите строку data по запятым , с помощью split()
print(fruits)

fruit_list = ", ".join(fruits) # Объедините fruits обратно в строку, используя join() с разделителем ", "
print(fruit_list)

# Задание 3
path = "home/user/documents/python/lesson1"
directories = path.split("/") # Разделите строку path по символу /, чтобы получить список директорий
print(directories)

windows_path = "\\".join(directories) # Используя join(), объедините элементы directories обратно в строку, но используйте \\ в качестве разделителя
print(windows_path)