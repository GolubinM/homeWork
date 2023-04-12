# ==Создать класс дробь=======================================================
class Fraction:
    __slots__ = ("_numerator", "_denominator")
    count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.instance_count()

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if value:
            self._denominator = value
        else:
            raise ValueError("Делитель не может равняться 0")

    @staticmethod
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def __add__(self, other):
        other = self.convert_to_fraction(other)
        if isinstance(other, Fraction):
            x = self.numerator * other.denominator + self.denominator * other.numerator
            y = self.denominator * other.denominator
            return self.__simplification(x, y)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = self.convert_to_fraction(other)
        if isinstance(other, Fraction):
            x = self.numerator * other.denominator - self.denominator * other.numerator
            y = self.denominator * other.denominator
            return self.__simplification(x, y)

    def __rsub__(self, other):
        other = self.convert_to_fraction(other)
        if isinstance(other, Fraction):
            x = other.numerator * self.denominator - other.denominator * self.numerator
            y = self.denominator * other.denominator
            return self.__simplification(x, y)

    def __mul__(self, other):
        other = self.convert_to_fraction(other)
        if isinstance(other, Fraction):
            x = self.numerator * other.numerator
            y = self.denominator * other.denominator
            return self.__simplification(x, y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = self.convert_to_fraction(other)
        if isinstance(other, Fraction):
            x = self.numerator * other.denominator
            y = self.denominator * other.numerator
            return self.__simplification(x, y)

    def __rtruediv__(self, other):
        other = self.convert_to_fraction(other)
        if isinstance(other, Fraction):
            x = other.numerator * self.denominator
            y = other.denominator * self.numerator
            return self.__simplification(x, y)

    @staticmethod
    def convert_to_fraction(other):
        if isinstance(other, int):  # раскладывает int на числитель и знаменатель 1
            other = Fraction(other, 1)
        elif isinstance(other, float):  # раскладывает float на числитель и знаменатель
            denominator = 10 ** (len(str(other)) - str(other).index(".") - 1)
            other = Fraction(int(other * denominator), denominator)
        return other

    @staticmethod
    def __simplification(numerator, denominator):  # упрощает дробь
        z = Fraction.gcd(numerator, denominator)
        return Fraction(int(numerator // z), int(denominator // z))

    def simplification(self):
        return self.__simplification(self.numerator, self.denominator)

    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def instance_count():
        Fraction.count += 1


print('сложение')
fract_1 = Fraction(1, 5) + Fraction(2, 3)
fract_2 = 0.4 + Fraction(2, 3)
fract_3 = Fraction(2, 3) + 1
print(fract_1, fract_2, fract_3)
print('вычитание')
fract_4 = Fraction(3, 5) - Fraction(1, 10)
fract_5 = 0.4 - Fraction(2, 3)
fract_6 = fract_1 - 7
print(fract_4, fract_5, fract_6)
print('умножение')
fract_1 = Fraction(3, 5) * Fraction(1, 7)
fract_2 = 0.4 * Fraction(2, 3)
fract_3 = fract_1 * 2
print(fract_1, fract_2, fract_3)
print('деление')
fract_4 = Fraction(3, 5) / Fraction(7, 10)
fract_5 = 0.4 / Fraction(2, 3)
fract_6 = fract_4 / 2
print(fract_4, fract_5, fract_6)
print('упрощение')
fract_1 = Fraction(12, 192)
print(fract_1, fract_1.simplification(), Fraction(12, 192).simplification())
print('конвертирование в дробное представление')
fract_1 = Fraction.convert_to_fraction(-51.12)
fract_2 = Fraction.convert_to_fraction(51)
fract_3 = Fraction.convert_to_fraction("1")
print(fract_1, type(fract_1), fract_2.__repr__(), type(fract_1), fract_3, type(fract_3))
# вывод данных
print(fract_1.numerator, fract_1.denominator, fract_1.__repr__(), fract_1.__str__())
# ввод данных
fract_1.denominator = 1075
print(fract_1)
# ==Добавить счетчик экземпляров===============================================
#     @staticmethod
#     def instance_count():
#         Fraction.count += 1
print(Fraction.count)

# =============================================================================
