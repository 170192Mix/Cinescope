
import random # Подключаем случайный модуль
import string # Содержит готовые наборы символов
from faker import Faker # Подключаем библиотеку Faker

faker = Faker() # Создаём объект Faker

class DataGenerator: # Данный класс используется для все было в одном месте
    @staticmethod # означает, что метод не зависит от состояния объекта класса
    def generate_random_email():
        s = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) # Выбираем 8 случайных символов из букв и чисел. join склеивает в строку
        return f"{s}@gmail.com"

    @staticmethod
    def generate_random_name():
        return f"{faker.first_name()} {faker.last_name()}" # Используем faker для генерации случайного имени и фамилии

    @staticmethod
    def generate_random_password():
        # Методы для генерации валидного пороля
        letters = random.choice(string.ascii_letters)
        digits = random.choice(string.digits)
        special = "?@#$%^&*|:"
        pool = string.ascii_letters + string.digits + special
        rest = ''.join(random.choices(pool, k=random.randint(6, 18)))
        pwd = list(letters + digits + rest)
        random.shuffle(pwd)
        return ''.join(pwd)

    # Данные фильмов
    @staticmethod
    def generate_movie_payload() -> object:
        """
        Валидный payload под контракт /movies
        """
        return { # Формируем словарь для API
            "name": faker.sentence(nb_words=3), # случайное название фильма (3 слова)
            "price": random.randint(100, 500), # цена, случайное число от 100 до 500
            "description": faker.text(max_nb_chars=80), # текст до 80 символов
            "imageUrl": faker.image_url(), # случайная ссылка на картинку
            "location": random.choice(["MSK", "SPB", "NSK"]), # случайный город
            "published": random.choice([True, False]), # случайный булевый флаг
            "genreId": random.randint(1, 5), # случайное число
        }

    @staticmethod
    def movie_patch_payload():
        """
        Payload для PATCH, специальный метод
        """
        return {
            "description": faker.text(max_nb_chars=60) # Возвращаем одно поле, т.к. PATCH меняет частично
        }

    @staticmethod
    def movie_invalid_payload():
        """
        Битые данные для негативных кейсов
        """
        return {
            "name": "",      # пустое название
            "price": "free", # строка вместо числа
            "description": None, # None вместо текста
            "imageUrl": "not_a_url",
            "location": 12345,  # число вместо строки
            "published": "yes", # строка вместо bool
            "genreId": "abc"    # строка вместо int
        }