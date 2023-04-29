import pickle, json

print('Задание 1. Реализуйте класс «Автомобиль».')


class ItemsCollection:
    @staticmethod
    def save_pikle(item, filename):
        with open(filename, 'wb') as f:
            pickle.dump(item, f)

    @staticmethod
    def load_pikle(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def save_JSON(item, filename):
        with open(filename, 'w') as f:
            if isinstance(item, list) and all([isinstance(elm, ItemsCollection) for elm in item]):
                json_obj = []
                for elm in item:
                    json_obj.append(f'{elm.__class__.__name__}(**{elm.__dict__})')
                json.dump(json_obj, f)
            elif isinstance(item, ItemsCollection):
                json.dump(f'{item.__class__.__name__}(**{item.__dict__})', f)

    @staticmethod
    def load_JSON(filename):
        with open(filename, 'r') as f:
            json_obj = json.load(f)
        if isinstance(json_obj, list):
            item = [eval(elm) for elm in json_obj]
        else:
            item = eval(json_obj)
        return item


class Car(ItemsCollection):
    VALID_KEYS = ("model", "engine_volume", "automaker", "car_color", "year")

    def __init__(self, model, year=None, car_color=None, automaker=None, engine_volume=None):
        self.model = model
        self.year = year
        self.car_color = car_color
        self.automaker = automaker
        self.engine_volume = engine_volume

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


a_car = Car("Mercedes SL350", 2015, "White", "MS", 3500)
b_car = Car("BMW 320D", 2019, "Black", "BMW", 2000)
c_car = Car("Toyota Camry", 1998, "Grey", "Toyota", 2400)
a_car.save_pikle(a_car, "a_car.pkl")
b_car.save_pikle(b_car, "b_car.pkl")
ItemsCollection.save_pikle(c_car, "c_car.pkl")
a2_car = ItemsCollection.load_pikle("a_car.pkl")
b2_car = Car.load_pikle("b_car.pkl")
c2_car = Car.load_pikle("c_car.pkl")
print(a2_car, b2_car, c2_car, sep="\n")
a_car.save_JSON(a_car, "a_car.json")
cars = [a_car, b_car, c_car]
ItemsCollection.save_pikle(cars, "cars.pkl")
pikle_cars = ItemsCollection.load_pikle("cars.pkl")
print("pikle cars")
print(*map(type, pikle_cars), pikle_cars)
ItemsCollection.save_JSON(cars, "cars.json")
cars = ItemsCollection.load_JSON("cars.json")
print("JSON cars")
print(*map(type, cars), cars)
a3_car = ItemsCollection.load_JSON("a_car.json")
print(a3_car, type(a3_car))

# ==============================================================================
print('\n\nЗадание 2. Реализуйте класс «Книга».')


class Book(ItemsCollection):
    def __init__(self, name, author=None, year=None, publisher=None, genre=None):
        self.name = name
        self.author = author
        self.year = year
        self.publisher = publisher
        self.genre = genre

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
        return f"{self.name}, {self.author}, {self.year}, {self.genre}"


a_book = Book('АРХИТЕКТУРА ЭВМ', 'Жмакин А.П.', 2010, genre="компьютерная литература")
b_book = Book('Мини-ЭВМ. Организация и программирование', 'Экхауз Р., Моррис Л.', 1983, genre="компьютерная литература")
c_book = Book('PDP-11. Архитектура и программирование', 'Фрэнк Томас', 1986, 'Радио и связь', "компьютерная литература")
a_book.save_pikle(a_book, "a_book.pkl")
a_2book = Book.load_pikle("a_book.pkl")
print(a_2book, type(a_2book))
print(b_book)
b_book.save_JSON(b_book, "b_book.json")
b2_book = Book.load_JSON("b_book.json")
print(b2_book, type(b2_book))

# ==============================================================================

print('\n\nЗадание 3. Реализуйте класс «Стадион».')


class Stadium(ItemsCollection):
    def __init__(self, name, city=None, country=None, year=None, capacity=None):
        self.name = name
        self.city = city
        self.country = country
        self.year = year
        self.capacity = capacity

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


stad_1 = Stadium("Arena", "Saint-Petersburg", "Russia", 2010, 250000)
stad_1.save_pikle(stad_1, "stad1.pkl")
stad2 = ItemsCollection.load_pikle("stad1.pkl")
stad2.print_info()
print(type(stad2))
