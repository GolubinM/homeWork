from abc import ABC, abstractmethod

print('==Создать базовый класс Фигура=======================================================')


class Figure(ABC):
    def __init__(self, *other):
        self.other = other

    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)

    def area(self):
        return self.other[1] * self.other[0]


class Circle(Figure):
    def __init__(self, r):
        super().__init__(r)

    def area(self):
        return self.other[0] ** 2 * 3.14


class RcTriangle(Figure):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)

    def area(self):
        return self.other[0] * self.other[1] / 2


rc1 = Rectangle(5, 10)
cr1 = Circle(5)
rcTr1 = RcTriangle(5, 10)
print(rc1.area(), cr1.area(), rcTr1.area())
print(rc1, cr1, rcTr1)

print('=Задание 2=Переопределить методы классов Задания 1=======================================================')


class Figure:
    def __init__(self, side1, side2=0):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def __str__(self):
        return f"Фигура класса {self.__class__.__name__} площадь: {self.area()}."

    def __int__(self):
        return self.area()


class Rectangle(Figure):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)

    def area(self):
        return self.side1 * self.side2


class Circle(Figure):
    def __init__(self, r):
        super().__init__(r)

    def area(self):
        return self.side1 ** 2 * 3.14


class RcTriangle(Figure):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)

    def area(self):
        return self.side1 * self.side2 / 2


rc1 = Rectangle(5, 10)
cr1 = Circle(5)
rcTr1 = RcTriangle(5, 10)
print(rc1.area(), cr1.area(), rcTr1.area(), sep="; ")

print(rc1, cr1, rcTr1,sep="\n")
print(rc1.__int__(), cr1.__int__(), rcTr1.__int__(), sep="; ")
