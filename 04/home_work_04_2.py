print("Модуль 4. Циклы. Часть 5")
print("Задание 1. Вывести на экран фигуры, заполненные звездочками."
      "Диалог с пользователем реализовать при помощи меню")

'''Описание решения:
    1. Каждый квадрат условно разделен на 4 блока - 4 квадрата, которые формируют нужный рисунок
        1   2
        3   4
    2. Блоки построчно выводятся функцией out_half()
    3. Функция поочередно заполняет фигуру строками в следующей последовательности:
            строка1.блок1+строка1.блок2
            строка2.блок1+строка2.блок2
            ....
            строка9.блок1+строкаN.блок2
            строка1.блок3+строка1.блок4
            строка2.блок3+строка2.блок4
            ....
            строка8.блок3+строкаN.блок4
    4. Строки формируется f-строкой функции  на  основании параметров определенных функцией prm_quart()
        для каждого блока, в зависимости от условного кодового имени блока "0000", "1100"..."1111". 
        Символы в названии описывают рисунок блока:
        каждый символ это сторона блока в следующем порядке (левая, верхняя, правая, нижняя):
        0 - с этой стороны нет заливки,
        1 - с этой стороны блок заполнен заливкой(" * ")
            пример1: "0000" - пустой блок, без заливки звездочками
            0   0   0
            0   0   0
            0   0   0
            пример2: "1111" - полностью заполненный звездочками блок 
            *   *   *
            *   *   *
            *   *   *
            пример3: "1100" - блок с заполненным звездочками верхним левым углом 
            *   *   *
            *   *   0
            *   0   0
            пример4: "1001" - блок с заполненным звездочками нижним левым углом 
            *   0   0
            *   *   0
            *   *   *
        такое именование функций облегчает сборку рисунка из 4 блоков, минимизирует код, а также позволяет
        определять начертание центральной линии фигуры, когда фигура состоит из нечетного числа линий 

    6. Пример конечного результата квадрат 4(д) из блоков "0110","1100"; "0011","1001"
            *   *   *   *   *
            0   *   *   *   0
            0   0   *   0   0
            0   0   *   0   0
            0   *   *   *   0
            *   *   *   *   *

    7. Размеры выводимой фигуры измеряются в линиях и могут меняться пользователем из меню при вводе символа "w" или "W"
    8. Для удобства реализована возможность вывода всех фигур сразу, вводом ключа "all" из меню
    9. Создание рисунка тремя символами " * "(пробел, звездочка, пробел) реализовано для компенсации межстрочного
     интервала и достижения более близкого соотношения сторон квадрата 1:1

'''

side_size = 11  # размер фигуры (фактически размер в символах равен (side_size * len_fill))
half_size = side_size // 2  # ширина одного из 4 элементов, составляющих фигуру квадрата
centre_line = side_size % 2  # определяем - будет ли выводиться центральная линия фигуры
fill = " * "  # символ заливки не пустого пространства(3 символа для компенсации межстрочных интервалов)
len_fill = len(fill)  # для расчета ширины (half_size) заполнения квадрата относительно кол-ва символов заливки
space = " "  # символ заполнения пустого пространства. Для отладки использовал (space = "·") - более наглядно.
msg_error_input = "Ошибка ввода! Попробуйте еще раз."


def prm_quart(quart_type):
    # определение параметров цикла для отрисовки блоков в зависимости от кодов сторон блока
    # длина строки вычисляется след формулой
    # abs(пробелы-номер_стр(row))*флаг(0||1 на случай пустого блока) + full_str(для полностью заполненного блока)
    blank = half_size + 1 if quart_type[1] == "1" else 0
    # вычисления стороны(лево/право) выравнивания заливки по коду блока, для передачу в f-строки функции out_half()
    side = "<" if quart_type[0] == "1" else ">"
    # вычисление флага полностью пустого/заполненного блока(для них не нужно определять кривую заполнения,
    # а просто залить символами space либо fill
    n_free = 0 if quart_type == "0000" or quart_type == "1111" else 1
    full_str = half_size if quart_type == "1111" else 0
    return blank, side, n_free, full_str


def out_half(lines):
    # в функцию передается объект следующего вида [[1,2],[3,4]], где 1,2,3,4 коды блоков вида "1100".."1111".
    # такая структура выбрана для реализации цикла вывода: сперва отбирается первый список(верхняя половина фигуры,
    # состоящая из двух блоков 1, 2), блоки перебираются следующим циклом, для определения параметров и отрисовки.

    hor_centre_line = centre_line  # надо ли рисовать центральную линию фигуры(если нечетное количество линий - 1)

    # для пустой фигуры центр не заливать(по заданию такой фигуры нет, но предусмотрел возможность)
    centre_point = fill if centre_line and lines != [["0000", "0000"], ["0000", "0000"]] else space

    for line in lines:
        blank1, order1, not_free1, full_str1 = prm_quart(line[0])  # вычисляем параметры для отрисовки блока 1(3)
        blank2, order2, not_free2, full_str2 = prm_quart(line[1])  # вычисляем параметры для отрисовки блока 2(4)
        # если правая сторона блока 1(3) залита, то заливка центральной вертикальной линии будет fill иначе space
        centre_fill = fill if line[0][2] == "1" else space
        for row in range(1, half_size + 1):
            row1 = abs(blank1 - row) * not_free1 + full_str1  # расчет множителя для звездочек в f-строке блока1(3)
            row2 = abs(blank2 - row) * not_free2 + full_str2  # расчет множителя для звездочек в f-строке блока2(4)
            # вывод линий фигуры для обоих блоков и при необходимости символа центральной линии
            print(f"{row1 * fill:{space}{order1}{half_size * len_fill}}",  # линия блока 1(3)
                  f"{centre_line * centre_fill:{space}{order1}{centre_line * len_fill}}",  # точка центр. вертик. линии
                  f"{row2 * fill:{space}{order2}{half_size * len_fill}}",  # линия блока 2(4)
                  sep="")
        # вывод центральной горизонтальной линии при необходимости
        if hor_centre_line:
            fill_cln1 = fill if line[0][3] == "1" else space  # определение символа заливки по коду блоков
            fill_cln2 = fill if line[1][3] == "1" else space  # определение символа заливки по коду блоков
            print(f"{half_size * fill_cln1:{space}{order1}{half_size * len_fill}}",
                  f"{centre_line * centre_point:{space}{order1}{centre_line * len_fill}}",
                  f"{half_size * fill_cln2:{space}{order2}{half_size * len_fill}}", sep="")
            # обнуление флага отрисовки центральной линии во избежание двойной отрисовки
            hor_centre_line = 0


# основной код
# Выбор фигуры (ввод: номер от 1 до 10 или символ от "a" до "и" в любом регистре, Q - выход, W - задать размер фигуры)
while True:
    while True:
        try:
            figure = input('\nВыберите фигуру для отрисовки (число от 1 до 10 или символ от "a" до "и");\n'
                           '"W" - задать размер фигуры;\n'
                           '"all" - вывести все фигуры сразу;\n'
                           'для выхода нажмите "Q": ').lower()
            if figure == "w":  # задать размер фигуры
                while True:
                    try:
                        side_size = int(input("Введите ширину фигуры, число в диапазоне от 3 до 51: "))
                        if 3 > side_size or side_size > 51:
                            raise ValueError(f"Заданное значение размера фигуры {side_size} вне диапазона [3:51]")
                        half_size = side_size // 2  # ширина одного из 4 элементов, составляющих фигуру квадрата
                        centre_line = side_size % 2  # определяем - будет ли выводиться центральная линия фигуры
                        break
                    except ValueError as exc:
                        print(msg_error_input, repr(exc))
                continue  # после задания размера фигуры возврат к меню выбора фигуры или выходу
            # исключаем 0 при выборе фигуры
            if (figure in "q123456789абвгдежзик" or figure == "10" or figure == "all") and figure != "":
                break  # если ошибок ввода нет переходим к выводу фигуры или выходу из программы
            else:
                raise ValueError(f"Значение {figure} вне диапазона [1:10] или [а:и]")
        except ValueError as exc:
            print(msg_error_input, repr(exc))

    if figure == "q":
        print("Good bye!")
        break

    if figure in "1а":
        print("\nSquare 1 'а'")
        out_half([["0110", "1111"], ["0000", "0110"]])
    elif figure in "2б":
        print("\nSquare 2 'б'")
        out_half([["1001", "0000"], ["1111", "1001"]])
    elif figure in "3в":
        print("\nSquare 3 'в'")
        out_half([["0110", "1100"], ["0000", "0000"]])
    elif figure in "4д":
        print("\nSquare 4 'г'")
        out_half([["0000", "0000"], ["0011", "1001"]])
    elif figure in "5е":
        print("\nSquare 5 'д'")
        out_half([["0110", "1100"], ["0011", "1001"]])
    elif figure in "6ж":
        print("\nSquare 6 'е'")
        out_half([["1001", "0011"], ["1100", "0110"]])
    elif figure in "7з":
        print("\nSquare 7 'ж'")
        out_half([["1001", "0000"], ["1100", "0000"]])
    elif figure in "8и":
        print("\nSquare 8 'з'")
        out_half([["0000", "0011"], ["0000", "0110"]])
    elif figure in "9и":
        print("\nSquare 9 'и'")
        out_half([["1111", "1100"], ["1100", "0000"]])
    elif figure == "10" or figure == "к":
        print("\nSquare 10 'к'")
        out_half([["0000", "0011"], ["0011", "1111"]])
    else:  # вывести все фигуры
        print("\nSquare 1 'а'")
        out_half([["0110", "1111"], ["0000", "0110"]])
        print("\nSquare 2 'б'")
        out_half([["1001", "0000"], ["1111", "1001"]])
        print("\nSquare 3 'в'")
        out_half([["0110", "1100"], ["0000", "0000"]])
        print("\nSquare 4 'г'")
        out_half([["0000", "0000"], ["0011", "1001"]])
        print("\nSquare 5 'д'")
        out_half([["0110", "1100"], ["0011", "1001"]])
        print("\nSquare 6 'е'")
        out_half([["1001", "0011"], ["1100", "0110"]])
        print("\nSquare 7 'ж'")
        out_half([["1001", "0000"], ["1100", "0000"]])
        print("\nSquare 8 'з'")
        out_half([["0000", "0011"], ["0000", "0110"]])
        print("\nSquare 9 'и'")
        out_half([["1111", "1100"], ["1100", "0000"]])
        print("\nSquare 10 'к'")
        out_half([["0000", "0011"], ["0011", "1111"]])
