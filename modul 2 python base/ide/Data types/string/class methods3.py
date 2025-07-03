# Задание 1 Реестр животных
class Animal:
    species = [] # Атрибут класса — общий список видов для всех животных

    def __init__(self, animal_type): # При создании объекта вызывает add_species
        self.animal_type = animal_type
        self.add_species(animal_type)

    @classmethod
    def add_species(cls, animal_type): # add_species Класс-метод, добавляет вид, если его ещё нет
        # Добавляем вид только если его ещё нет в списке
        if animal_type not in cls.species:
            cls.species.append(animal_type)

    @classmethod
    def show_species(cls): # show_species Класс-метод, выводит все виды
        print("Зарегистрированные виды животных:")
        for kind in cls.species:
            print("-", kind)

a1 = Animal("Кошка")
a2 = Animal("Собака")
a3 = Animal("Кошка")  # Повтор — не должен добавиться
a4 = Animal("Попугай")

Animal.show_species()