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


colors = ("Black", "White", "Grey")
volumes = (3500, 2000, 2700)

a_car = Car("Mercedes SL350")
b_car = Car("BMW 320D")
c_car = Car("Toyota Camry")
cars = [a_car, b_car, c_car]
for car in cars: print(car.model)
for car, color, volume in zip(cars, colors, volumes): car.car_color = color; car.engine_volume = volume
d_car = Car("")  # Создает экземпляр Car, но не позволяет установить пустое значение полю 'model'
print(d_car, d_car.__dict__)
d_car.model = "BMW 115i"
d_car.car_color = "white"
d_car.year = "2018"
d_car.engine_volume = "1600"
d_car.automaker = "BMW"
d_car.width = 2600  # не позволяет установить значение атрибута, не определенного в 'VALID_KEYS'
print(d_car, d_car.__dict__)
cars.append(d_car)
for car in cars: car.print_info()