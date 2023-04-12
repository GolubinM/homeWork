print('Задание 1. Реализуйте класс «Автомобиль».')


class Car:
    VALID_KEYS = ("model", "engine_volume", "automaker", "car_color", "year")

    def __init__(self, model):
        self.model = model
        self.year = None
        self.car_color = None
        self.automaker = None
        self.engine_volume = None

    def set_info(self):
        self.model = input("Введите модель: ")
        self.year = input("Введите год выпуска: ")
        self.car_color = input("Введите цвет кузова: ")
        self.automaker = input("Введите производителя: ")
        self.engine_volume = input("Введите объем двигателя: ")

    def print_info(self):
        print(f'Автомобиль: {self.model}\n\t'
              f'объем двигателя: {self.engine_volume}\n\t'
              f'производитель: {self.automaker}\n\t'
              f'цвет кузова: {self.car_color}\n\t'
              f'год выпуска: {self.year};')

    def __setattr__(self, key, value):
        if key in self.VALID_KEYS and value != "":
            self.__dict__[key] = value
        elif key == "model":
            self.__dict__[key] = "Undefined model"
        elif key not in self.VALID_KEYS:
            raise AttributeError("Недопустимый атрибут")
        else:
            raise ValueError("Значение не должно быть пустым")

    def __repr__(self):
        return f"{self.model}, {self.year}, {self.car_color}"


colors = ("Black", "White", "Grey")
volumes = (3500, 2000, 2700)

a_car = Car("Mercedes SL350")
b_car = Car("BMW 320D")
c_car = Car("Toyota Camry")
cars = [a_car, b_car, c_car]
for car in cars: print(car.model)
for car, color, volume in zip(cars, colors, volumes): car.car_color = color; car.engine_volume = volume
d_car = Car("")  # Создает экземпляр Car, вместо пустого значения полю 'model' устанавливает значение "Undefined model"
print(d_car, d_car.__dict__)
d_car.model = "BMW 115i"
d_car.car_color = "white"
d_car.year = "2018"
d_car.engine_volume = "1600"
d_car.automaker = "BMW"
try:
    d_car.width = 2600  # не позволяет установить значение атрибута, не определенного в 'VALID_KEYS'
except AttributeError as ex:
    print('\u001b[38;5;001m' + ex.__repr__() + '\033[0m')
print(d_car, d_car.__dict__)
cars.append(d_car)
for car in cars: car.print_info()
# ==============================================================================
print('\n\nЗадание 2. Реализуйте класс «Книга».')


class Book:
    __slots__ = ("name", "author", "year", "publisher", "genre")

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.publisher = None
        self.genre = None

    def set_info(self):
        self.name = input("Введите название: ")
        self.author = input("Введите автора: ")
        self.year = input("Введите год издания: ")
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")

    def print_info(self):
        print(f'Книга: {self.name}\n\t'
              f'автор: {self.author}\n\t'
              f'год издания: {self.year}\n\t'
              f'издательство: {self.publisher}\n\t'
              f'жанр: {self.genre};')

    def __repr__(self):
        return f"{self.name}, {self.author}, {self.year}"


a_book = Book('АРХИТЕКТУРА ЭВМ', 'Жмакин А.П.', 2010)
b_book = Book('Мини-ЭВМ. Организация и программирование', 'Экхауз Р., Моррис Л.', 1983)
c_book = Book('PDP-11. Архитектура и программирование', 'Фрэнк Томас', 1986)
c_book.publisher = 'Радио и связь'
a_book.genre = "компьютерная литература"
b_book.genre = "компьютерная литература"
c_book.genre = "компьютерная литература"
a_book.print_info()
b_book.print_info()
c_book.print_info()
d_book = Book("Тимофей и фея", None, None)
d_book.genre = "стихи"
# d_book.pages = "100" # __slots__ не позволит определить данный атрибут, поднимет AttributeError:
# print(d_book, d_book.__dict__)
print(d_book, f"Допустимые атрибуты: {d_book.__slots__}", sep="; ")  # __slots__ не позволит вызвать метод __dict__

# ==============================================================================
print('\n\nЗадание 3. Реализуйте класс «Стадион».')


class Stadium:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.country = None
        self.year = None
        self.capacity = None

    def set_info(self):
        self.name = input("Введите название: ")
        self.city = input("Введите город: ")
        self.country = input("Введите страну: ")
        self.year = input("Введите год открытия: ")
        self.capacity = input("Введите вместимость: ")

    def print_info(self):
        print(f'Стадион: {self.name}\n\t'
              f'город: {self.city}\n\t'
              f'страна: {self.country}\n\t'
              f'год открытия: {self.year}\n\t'
              f'вместимость: {self.capacity};')
