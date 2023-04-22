from abc import ABC, abstractmethod

print('==Создать базовый класс Фигура=======================================================')


class Figure(ABC):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @abstractmethod
    def area(self):
        pass

    # к Заданию 2. =Переопределить методы=
    def __repr__(self):
        return f"{self.__class__.__name__}(**{self.__dict__})"

    def __str__(self):
        return f"Фигура класса {self.__class__.__name__} площадь: {self.area()}"

    def __int__(self):
        return self.area()
    # конец Задания 2. =Переопределить методы=


class Rectangle(Figure):
    def __init__(self, side1, side2):
        super().__init__(side1=side1, side2=side2)

    def area(self):
        return self.side1 * self.side2


class Circle(Figure):
    def __init__(self, r):
        super().__init__(radius=r)

    def area(self):
        return self.radius ** 2 * 3.14


class RcTriangle(Figure):
    def __init__(self, leg1, leg2):
        super().__init__(leg1=leg1, leg2=leg2)

    def area(self):
        return self.leg1 * self.leg2 / 2


class Trapezoid(Figure):
    def __init__(self, base1, base2, h):
        super().__init__(base1=base1, base2=base2, h=h)

    def area(self):
        return (self.base1 + self.base2) * self.h / 2


rc1 = Rectangle(5, 10)
cr1 = Circle(5)
rcTr1 = RcTriangle(5, 10)
tr1 = Trapezoid(10, 5, 7)
print(rc1.area(), cr1.area(), rcTr1.area(), tr1.area(), sep="; ")
print(rc1, cr1, rcTr1, tr1, sep="\n")
print(rc1.__int__(), cr1.__int__(), rcTr1.__int__(), tr1.__int__(), sep="; ")
rc10 = eval(repr(rc1))
print("rc10", rc10)

# '=Задание 2=Переопределить методы классов Задания 1===================
# см. строки 14-23


print('=Задание 3=Shape=======================================================')


class Shape:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def show(self):
        print(f"figure of {self.__class__.__name__} class has attributes:",
              *(f"{elm[0]}={elm[1]}" for elm in self.__dict__.items()))

    @staticmethod
    def save(figure, filename):
        with open(filename, 'w') as f:
            if isinstance(figure, list) and any([isinstance(fig, Shape) for fig in figure]):
                with open(filename, 'a') as f:
                    for fig in figure: f.write(f"{fig.__repr__()}\n")
            elif isinstance(figure, Shape):
                f.write(f"{figure.__repr__()}\n")

    @staticmethod
    def load(filename):
        with open(filename) as f:
            file_content = f.readlines()
            if len(file_content) > 1:
                return [eval(fig) for fig in file_content]
            elif len(file_content) == 1:
                return eval(file_content[0])

    def __repr__(self):
        return f"{self.__class__.__name__}(**{self.__dict__})"

    def __str__(self):
        return f"Фигура класса {self.__class__.__name__}, {self.__dict__} "


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x=x, y=y, side=side)


class Rectangle(Shape):
    def __init__(self, x, y, side1, side2):
        super().__init__(x=x, y=y, side1=side1, side2=side2)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x=x, y=y, radius=radius)


class Ellipse(Shape):
    def __init__(self, x, y, side1, side2):
        super().__init__(x=x, y=y, side1=side1, side2=side2)


sq2 = Square(10, 20, 10)
sq2.show()
sq2.save(sq2, "sq2.txt")
sq3 = Shape.load("sq2.txt")
print("sq2", sq3)
print("sq3", sq3)
rc2 = Rectangle(20, 40, 100, 30)
rc2.save(rc2, "rc2.txt")
rc3 = Shape.load("rc2.txt")
print("rc2", rc2)
print("rc3", rc3)
cr2 = Circle(20, 40, 22)
cr2.save(cr2, "cr2.txt")
cr3 = Shape.load("cr2.txt")
print("cr2", cr2)
print("cr3", cr3)
el1 = Ellipse(101, 101, 41, 21)
el1.save(el1, "el1.txt")
el2 = Shape.load("el1.txt")
print("el1", el1)
print("el2", el2)
print("========Обработка списка фигур========")
figures1 = [sq2, rc3, cr2, el1]
print("Figures1", type(figures1), figures1)
print(f"Вывод объектов списка {figures1} построчно")
for elm in figures1: print(elm)
Shape.save(figures1, "figs1.txt")
figures2 = Shape.load("figs1.txt")
print("Figures2", type(figures2), figures2)
print(f"Вывод объектов списка {figures2} построчно")
for elm in figures2: print(elm)
print("=" * 75)
