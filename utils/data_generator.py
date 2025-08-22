import random
import string
from faker import Faker

faker = Faker()

class DataGenerator:
    @staticmethod
    def generate_random_email():
        s = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{s}@gmail.com"

    @staticmethod
    def generate_random_name():
        return f"{faker.first_name()} {faker.last_name()}"

    @staticmethod
    def generate_random_password():
        # хотя бы 1 буква + 1 цифра, длина 8-20, допустимые символы
        letters = random.choice(string.ascii_letters)
        digits = random.choice(string.digits)
        special = "?@#$%^&*|:"
        pool = string.ascii_letters + string.digits + special
        rest = ''.join(random.choices(pool, k=random.randint(6, 18)))
        pwd = list(letters + digits + rest)
        random.shuffle(pwd)
        return ''.join(pwd)
