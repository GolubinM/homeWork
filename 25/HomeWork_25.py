# ==Создать класс Окружность=======================================================
class Circle:
    def __init__(self, radius, precious=2):
        self.radius = radius
        self.circ_length = radius * 6.28
        self.out_precious = precious

    # предчувствую, что если радиусы равны, то и длины окружностей (+/-)равны
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.circ_length == other.circ_length

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circ_length < other.circ_length

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circ_length > other.circ_length

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circ_length >= other.circ_length

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circ_length <= other.circ_length

    def __add__(self, other):
        self.__init__(self.radius + other)
        return self

    def __radd__(self, other):
        self.__init__(self.radius + other)
        return self

    def __iadd__(self, other):
        self.__init__(self.radius + other)
        return self

    def __sub__(self, other):
        self.__init__(self.radius - other)
        return self

    def __isub__(self, other):
        self.__init__(self.radius - other)
        return self

    def __str__(self):
        return f"Circle R:{self.radius}, L:{self.circ_length:.{self.out_precious}f}"

    def __repr__(self):
        return {self.radius}, {self.circ_length}


c1 = Circle(10)
c2 = Circle(6)
print(c2 == c1)
print(c2 + 4)
print(c2 == c1)
c2 -= 1
print(c2)

print("\n\n==Создать класс Complex==========================================================")


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        divisor = other.re ** 2 + other.im ** 2
        return Complex((self.re * other.re + self.im * other.im) / divisor,
                       (other.re * self.im - self.re * other.im) / divisor)

    def __str__(self):
        return f"({self.re}{self.im:+}i)"


i1 = Complex(5, 2)
i2 = Complex(2, 8)
print(i1 + i2, i1 - i2, i1 / i2, i1 * i2)

print("\n\n==Создать класс Airplane==========================================================")


class Airplane:
    def __init__(self, plane_type, max_pass):
        self.plane_type = plane_type
        self.max_passengers = max_pass
        self.load_passengers = 0

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, other):
        self.load_passengers += other
        return self

    def __iadd__(self, other):
        self.load_passengers += other
        return self

    def __sub__(self, other):
        self.load_passengers -= other
        return self

    def __isub__(self, other):
        self.load_passengers -= other
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __str__(self):
        return f"(Airplane {self.plane_type} capacity {self.max_passengers} is loaded for {self.load_passengers} pass.)"


plane1 = Airplane("Boing-737", 750)
plane2 = Airplane("Airbus-300", 850)
print(plane1 == plane2)
print(plane1.max_passengers, plane2.max_passengers)
plane1 += 150
plane2 += 160
print(plane1, plane2)
print(plane1 < plane2)
print(plane2.load_passengers)
plane2 -= 10
plane2 = plane2 + 5
print(plane2.load_passengers)
print(plane1 <= plane2)

print("\n\n==Создать класс Flat==========================================================")


class Flat:
    def __init__(self, area: int | float, cost: int | float):
        self.area = area
        self.cost = cost

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __ge__(self, other):
        return self.cost >= other.cost


flat1 = Flat(150, 10_000_000)
flat2 = Flat(160, 11_000_000)
print("Сравнение площади", flat1 == flat2, flat1 != flat2)
print("Сравнение цен:", flat1 > flat2, flat1 < flat2, flat1 >= flat2, flat1 <= flat2)
