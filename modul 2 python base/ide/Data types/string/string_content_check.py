# Проверка содержимого строки
# Задание 6
phrase = "The quick brown fox jumps over the lazy dog"
contains_fox = "fox" in phrase # Проверка, содержит ли фраза слово "fox"
print(contains_fox)

# Задание 6.1
greeting = "Hello, world!"
starts_with_hello = greeting.startswith("Hello")
print(starts_with_hello)

ends_with_world = greeting.endswith("world!")

# Задание 6.2
text = "12345"
is_digits = text.isdigit()
print(text)

# Задание 6.3
mixed_text = "Hello123"
is_alphanumeric = mixed_text.isalnum()
print(mixed_text)

# Задание 6.4
whitespace_text = "   "
print(whitespace_text.isspace())