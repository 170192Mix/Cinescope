# Замена подстрок
# Задание 7
sentence = "Кот сидит на крыше."
new_sentence1 = sentence.replace("Кот", "Пёс")
print(new_sentence1)

new_sentence2 = sentence.replace("крыше", "дереве")
print(new_sentence2)

# Задание 7.1
phrase = "Я люблю яблоки и яблоки - самые вкусные фрукты."
phrase_replace = phrase.replace("яблоки", "бананы", 1) # заменяет только первое вхождение.
print(phrase_replace)

new_phrase = phrase.replace("яблоки", "бананы")
print(new_phrase)

# Задание 7.2
text = "Привет, мир! Привет, люди! Привет, солнце!"
new_text = text.replace("Привет", "Здавствуй")
print(new_text)

greeting = text.replace("люди", "друзья")
print(greeting)