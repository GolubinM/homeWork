from random import randint
from math import sqrt, pi

# =====================================================================================================
print("Задание 1.1 Количество простых чисел в списке.")
# очень хотелось использовать map с функциями:)
test_list_num = [randint(0, 7) for _ in range(10)]


def is_simple(num: int) -> int:
    """возвращает 0 если число не является простым, или 1 если является"""
    if num < 2:
        return 0
    for div in range(2, num // 2 + 1):
        if num % div == 0:
            return 0
    return 1


def count_simple_number(lst_num: list[int]) -> int:
    count = sum(map(is_simple, [elm for elm in lst_num]))
    return count


# список случайных чисел с подкрашенными простыми
[print(is_simple(x) * '\033[94m' + f"{x}" + '\033[0m', end=", ") for x in test_list_num]
print('\b' * 2)  # последнюю запятую убираем backspace-ом
print("простых чисел:", count_simple_number(test_list_num))
# =====================================================================================================
# решение в одну строку оказалось медленнее в ~4 раза, чем решение с прерывающим условием. Вот оно
# count = sum([all([x % divider for divider in range(2, x // 2 + 1)]) for x in lst_num if x > 1])
# =====================================================================================================
# print("Задание 1.2 Количество простых чисел в списке.")
# # в одну функцию, как в задании
# test_list_num = [randint(0, 7) for _ in range(10)]
#
#
# def prime_number(lst_num):
#     count = 0
#     for number in lst_num:
#         if number < 2:
#             continue  # числа меньше 2 не являются простыми числами, исключаем их из диапазона проверки
#         prime_atr = 1
#         for divider in range(2, number // 2 + 1):
#             if number % divider == 0:
#                 prime_atr = 0
#                 break
#         count += prime_atr
#     return count
#
#
# =====================================================================================================


print("\n\nЗадание 2. Удалить из списка целых некоторое заданное число. Вернуть количество удаленных элементов списка.")
# Формируем список случайных целых чисел длинной 50 эл-ов, диапазон значения эл-ов 0-7
# Генерируем случайное число в диапазоне 0-7, которое будет удалено, присваиваем его переменной todel
rand_list = [randint(0, 7) for _ in range(50)]
todel = randint(0, 7)


def delete_from_list(num: int) -> int:
    global rand_list
    count = rand_list.count(num)
    if count:
        rand_list = [elm for elm in rand_list if elm != num]
    return count


print("Список целых чисел:", rand_list)
print("Удалить число:", todel)
print("Удалено чисел:", delete_from_list(todel))
print("Список чисел после удаления:", rand_list)

# =================================================================================================================
print("Задание 2.1. Удалить из списка целых некоторое заданное число. Вернуть количество удаленных элементов списка.")
# с помощью remove без объявления глобальной переменной

def remove_from_list(rnd_list: list[int], num: int) -> int:
    count = rnd_list.count(num)
    for i in range(count):
        rnd_list.remove(num)
    return count


rand_list = [randint(0, 7) for _ in range(50)]
todel = randint(0, 7)

print("Список целых чисел:", rand_list)
print("Удалить число:", todel)
print("Удалено чисел:", remove_from_list(rand_list, todel))
print("Список чисел после удаления:", rand_list)

# =================================================================================================================
print("\n\nЗадание 3. Счетчик отрицательных чисел в матрице 4*4.")


def minus_num_in_matrix() -> int:
    cols = range(4)
    rows = range(4)
    matrix = [[randint(-20, 10) for _ in cols] for _ in rows]
    count_minus = sum([1 for row in matrix for elm in row if elm < 0])
    return count_minus


print("Количество отрицательных числе в матрице:", minus_num_in_matrix())
# =================================================================================================================
print("\n\nЗадание 4. Функция расчета площади фигур: треугольник, прямоугольник, круг.")


# Ввод и проверка значений вынесена в отдельную функцию check_input().

def check_input(invite_str: str, check: callable(bool)):
    """
    Функция принимает строку с приглашением ввода переменной - invite, и условие валидности переменной
    определенное в функции, передаваемой через параметр check (check = lambda x: 0 < x)
    """
    while True:
        try:
            inp_value = float(input(invite_str))
            if check(inp_value):  # проверка соответствия введенного значения условию валидности
                break
            else:
                print("Не корректный выбор, попробуйте еще раз.")
        except Exception as exc:
            print("Ошибка ввода, попробуйте еще раз:", repr(exc))
    return inp_value


def calculate_square() -> float:
    """
    Расчет площади выбранной фигуры. Возвращает площадь с точностью до сотых.
    Возвращает -1 в случае невозможности расчета площади фигуры по заданным параметрам.
    """
    check = lambda x: x in [1, 2, 3]  # функция как условие проверки ввода, передаваемая параметром в check_input()
    selector = check_input("<<< Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг\n<<< ", check)
    check = lambda x: 0 < x  # функция как условие проверки ввода, передаваемая параметром в check_input()
    invite = "Введите сторону "
    if selector == 1:
        # рассчитываем площадь треугольника
        a = check_input(invite + "a = ", check)
        b = check_input(invite + "b = ", check)
        c = check_input(invite + "c = ", check)
        sum_sides = a + b + c
        if 2 * max(a, b, c) >= sum_sides:  # проверка треугольника на валидность(гипотенуза < суммы катетов)
            return -1  # в случае не валидности треугольника возвращаем -1
        semi_perimetr = sum_sides / 2  # полу-периметр треугольника
        area = sqrt(semi_perimetr * (semi_perimetr - a) * (semi_perimetr - b) * (semi_perimetr - c))
    elif selector == 2:
        # рассчитываем площадь прямоугольника
        a = check_input(invite + "a = ", check)
        b = check_input(invite + "b = ", check)
        area = a * b
    else:
        # рассчитываем площадь круга
        invite = "Введите радиус круга r = "
        r = check_input(invite, check)
        area = pi * r ** 2
    return round(area, 2)


print(calculate_square())
