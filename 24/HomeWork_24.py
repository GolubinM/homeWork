# ==Создать класс дробь=======================================================
class Fraction:
    __slots__ = ("_numerator", "_denominator")
    count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

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
# ==Задание 1. Добавить счетчик экземпляров============================================
#         Fraction.count += 1
print("count:", Fraction.count)
# =============================================================================

print("\n==температура из Цельсия в Фаренгейт и наоборот==============================")


class TemperatureConversion:
    count = 0

    @staticmethod
    def celcius_to_fahrenheit(value):
        TemperatureConversion.count += 1
        return round(value * 1.8 + 32, 1)

    @staticmethod
    def fahrenheit_to_celcius(value):
        TemperatureConversion.count += 1
        return round((value - 32) / 1.8, 1)


print(TemperatureConversion.celcius_to_fahrenheit(36.6))
print(TemperatureConversion.fahrenheit_to_celcius(32))
print("count:", TemperatureConversion.count)

print("\n==перевод из метрической системы в английскую и наоборот====================")


class EmpireUnitConverter:
    count = 0
    accuracy = 3

    @staticmethod
    def __convert(value, factor, accuracy=accuracy):
        EmpireUnitConverter.count += 1
        return round(value * factor, accuracy)

    @staticmethod
    def inch_to_mm(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 25.4, accuracy)

    @staticmethod
    def inch_to_cm(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 2.54, accuracy)

    @staticmethod
    def inch_to_m(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 0.0254, accuracy)

    @staticmethod
    def foot_to_mm(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 304.8, accuracy)

    @staticmethod
    def foot_to_cm(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 30.48, accuracy)

    @staticmethod
    def foot_to_m(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 0.3048, accuracy)

    @staticmethod
    def yard_to_m(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 0.9144, accuracy)

    @staticmethod
    def chain_to_m(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 20.117, accuracy)

    @staticmethod
    def furlong_to_m(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 201.17, accuracy)

    @staticmethod
    def miles_to_m(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1609.3, accuracy)

    @staticmethod
    def miles_to_km(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1.6093, accuracy)

    # ==обратно===============================
    @staticmethod
    def mm_to_inch(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 25.4, accuracy)

    @staticmethod
    def cm_to_inch(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 2.54, accuracy)

    @staticmethod
    def m_to_inch(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 0.0254, accuracy)

    @staticmethod
    def mm_to_foot(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 304.8, accuracy)

    @staticmethod
    def cm_to_foot(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 30.48, accuracy)

    @staticmethod
    def m_to_foot(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 0.3048, accuracy)

    @staticmethod
    def m_to_yard(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 0.9144, accuracy)

    @staticmethod
    def m_to_chain(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 20.117, accuracy)

    @staticmethod
    def m_to_furlong(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 201.17, accuracy)

    @staticmethod
    def m_to_miles(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 1609.3, accuracy)

    @staticmethod
    def km_to_miles(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 1.6093, accuracy)

    # ==Volume (UK)=============================
    @staticmethod
    def gallon_to_liter(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 4.54609, accuracy)

    @staticmethod
    def pint_to_liter(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 0.5683, accuracy)

    # ==Volume (UK)=обратно=====================
    @staticmethod
    def liter_to_gallon(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 4.54609, accuracy)

    @staticmethod
    def liter_to_pint(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 0.5683, accuracy)

    # ==Units of mass (UK)======================
    @staticmethod
    def ounce_to_gramms(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 28.35, accuracy)

    @staticmethod
    def troy_ounce_to_gramms(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 31.1, accuracy)

    @staticmethod
    def pound_to_gramms(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 453.6, accuracy)

    @staticmethod
    def stone_to_kg(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 6.35, accuracy)

    # ==Units of mass (UK)==обратно=============
    @staticmethod
    def gramms_to_ounce(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 28.35, accuracy)

    @staticmethod
    def gramms_to_troy_ounce(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 31.1, accuracy)

    @staticmethod
    def gramms_to_pound(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 453.6, accuracy)

    @staticmethod
    def kg_to_stone(value, accuracy=accuracy):
        return EmpireUnitConverter.__convert(value, 1 / 6.35, accuracy)


conv_emp = EmpireUnitConverter()
print(conv_emp.inch_to_mm(65))
print(conv_emp.inch_to_cm(65))
print(conv_emp.inch_to_m(65, 1))
print(conv_emp.km_to_miles(10, 2))
print(conv_emp.gramms_to_troy_ounce(111, 5))
print("count:", conv_emp.count)
