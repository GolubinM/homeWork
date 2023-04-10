print("\n1. Две трети(или треть) списка отсортировать в порядке возрастания, оставшаяся часть - инвертировать порядок")


# 1. Вычисляем границу сортировки p1, в зависимости от среднего значения списка
# 2. Сортируем срез [:p1]
# 4. Располагаем в обратном порядке срез [p1:]

def print_grid_color(lst: list, p: int):
    """Цветная распечатка списка"""
    sorted_CLR = '\u001b[38;5;' + '106' + 'm'
    reversed_CLR = '\u001b[38;5;' + '4' + 'm'
    RESET_COLOR = '\033[0m'
    [print(sorted_CLR * (el[0] < p) + reversed_CLR * (el[0] >= p) + f"{el[1]}", end=", ") for el in enumerate(lst)]
    print("\b\b", RESET_COLOR)


def task1(lst: list):
    lenlst = len(lst)
    p1 = lenlst * (2 if (sum(lst) / lenlst) > 0 else 1) // 3
    lst[:p1] = sorted(lst[:p1])
    lst[p1:] = lst[p1:][::-1]
    print_grid_color(lst, p1)


lst1 = [1, 10, 2, 11, 3, 13, 6, 4, 5, 21, 22, 15]
print("Список 1. Среднее значение =", f"{sum(lst1) / len(lst1):.1f}")
print(*lst1, sep=", ")
task1(lst1)
lst2 = [-1111, 10, 2, 11, 3, 13, 6, 4, 5, 21, 22, 15]
print("\nСписок 2. Среднее значение =", f"{sum(lst2) / len(lst2):.1f}")
print(*lst2, sep=", ")
task1(lst2)

# ==============================================================================
print("\nЗадание 2. Написать программу 'Успеваемость'. 11, 11, 11, 11, 10, 11, 11, 12, 10, 11  - помощь для ввода")


def students_grades():
    RED = '\u001b[38;5;' + '1' + 'm'
    YEL = '\u001b[38;5;' + '228' + 'm'
    GR_PAD = '\u001b[48;5;' + '28' + 'm'
    BR = YEL + GR_PAD
    RST = '\033[0m'
    grades = []

    def check_input(invite_str: str, check: callable):
        """
        Функция принимает строку с приглашением ввода переменной - invite, и условие валидности переменной
        определенное в функции, передаваемой через параметр check (check = lambda x: 0 < x)
        """
        while True:
            try:
                inp_value = input(f"{YEL}{invite_str}{RST}")
                if check(inp_value):  # проверка соответствия введенного значения условию валидности
                    break
                else:
                    print(f"{RED}Не корректный ввод, попробуйте еще раз.{RST}")
            except Exception as exc:
                print(f"{RED}Ошибка ввода, попробуйте еще раз:", repr(exc), RST)
        return inp_value

    def check_grds(x):
        return [int(elm) for elm in x.split(",")]  # функция-аргумент для проверки вводимых списком оценок
        # если эл-ты введенные списком нельзя преобразовать в int выдаст ошибку(заменил lambda на def(PEP8:E731))

    len_grades = len(grades)
    while len_grades < 10:
        print(f"{YEL}Всего оценок в списке {len_grades}. Необходимо добавить еще {10 - len_grades}.{RST}")
        input_str = f"Введите {10 - len_grades} оценок студента, разделенные запятой(оценки от 1 до 12):\n >>>"
        grades.extend(map(int, check_input(input_str, check_grds).split(",")))
        # сокращаем список до 12 оценок, удаляем оценки за пределами допустимого диапазона
        grades = [grade for grade in grades if 13 > grade > 0][:10]
        print(f"{YEL}Список введенных оценок:{RST} {grades}")
        len_grades = len(grades)

    while True:
        print(f"\n{YEL}МЕНЮ ПРОГРАММЫ:")
        select = input("\n1. Вывод оценок"
                       "\n2. Пересдача экзамена"
                       "\n3. Расчет 'выходит ли стипендия'"
                       "\n4. Вывод отсортированного списка оценок"
                       f"\nQ. Выход\n >>> {RST}")
        if select == "Q":
            print(f"{YEL}Good bye!{RST}")
            break
        elif select == "1":
            print(f"\t{YEL}Список оценок:{RST} {grades}")
        elif select == "2":
            print(f"{YEL}Пересдача экзамена, ввод новой оценки по номеру элемента списка")
            print(f"\n\tСписок оценок: {', '.join([f'{BR}({elm[0]}){RST} {elm[1]}' for elm in enumerate(grades)])}")
            num = check_input(f"\t{YEL}Выберете номер элемента {BR}(0){RST}-{BR}(9){RST}{YEL}отмена - Q:\n\t >>> {RST}",
                              lambda x: (x == "Q") or (9 >= int(x) >= 0))
            if num != "Q":
                grades[int(num)] = int(check_input(f"{YEL}Введите новую оценку(от 1 до 12): {RST}",
                                                   lambda x: 12 >= int(x) >= 0))
        elif select == "3":
            middle_grade = sum(grades) / len(grades)
            answer = f"не " if middle_grade < 10.7 else ""
            print(f"\t{YEL}Средний бал студента = {RST}{middle_grade:.1f}")
            print(f"\t{YEL}По результату расчета среднего балла студент {answer}имеет право получать стипендию.{RST}")
        elif select == "4":
            print(f"{YEL}Вывод оценок по возрастанию или убыванию.{RST}")
            rev = bool(int(check_input(f"\t{YEL}сортировать оценки: 0 - по возрастанию, 1 - по убыванию:\n >>> {RST}",
                                       lambda x: x in ["0", "1"])))
            print(sorted(grades, reverse=rev))


students_grades()
# ==============================================================================
print("\nЗадание 3. Усовершенствованная сортировка пузырьковым методом.")
from random import randint


def sort_buble(lst: list):
    swap = True
    itr1 = 0
    len_lst = len(lst) - 1  # вынос в переменную дал небольшой прирост в производительности
    while swap:
        swap = False
        for j in range(len_lst - itr1):
            if lst[j] > lst[j + 1]:  # вынос [j + 1] в переменную, к удивлению, ухудшил производительность...
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
        itr1 += 1
    return f"\niterations value ={itr1}"


lst1 = [randint(0, 50000) for _ in range(1000)]
# print(lst1)
print(f"{lst1[:10]}...{lst1[-10:]}")  # ради удобства чтения
print(sort_buble(lst1))
print(f"{lst1[:10]}...{lst1[-10:]}")
print("lst1==sorted(lst1) is", lst1 == sorted(lst1))  # дополнительная проверка сортировки
# ==============================================================================
