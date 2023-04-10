import os

os.system('')


print("Задание 1. Наибольший общий делитель с помощью алгоритма Евклида(методом рекурсии)")


# Решение:
# 1.Большее число поделить на меньшее.(Если поделить меньшее на большее при след рекурс. вызове они поменяются местами)
# 2.Меньшее число поделить на остаток, который получается после деления.
# 3.Первый остаток поделить на второй остаток.
# 4.Второй остаток поделить на третий и т. д.
# 5.Деление продолжается до тех пор, пока в остатке не получится нуль.
# Последний делитель и есть наибольший общий делитель. if a%b = 0: return b else foo(b,c)

def find_gcd(a, b):
    if a % b == 0:
        return b
    else:
        return find_gcd(b, a % b)


print("НОД =", find_gcd(int(input('Введите а=')), int(input('Введите b='))))

# =======================================================================================================

print("\nЗадание 2. Быки и коровы.")

# Классический вариант: компьютер генерирует тайное 4-значное число с неповторяющимися цифрами.
# Вариант с повторениями значений: компьютер генерирует тайное 4-значное число с повторяющимися цифрами.
# Решение:
# 1. сравниваем оба списка, если равны - выводим "победа пользователя", нет - начинаем сравнение по-элементно
# Проверка: сперва "коров", чтобы исключить дальнейшее возможно ошибочное определение "быков".
# 2. Проверяем "коров":
# идем по элементам списка пользователя, поочередно сравнивая каждый элемент с элементом из списка сгенерированного
# компьютером, с тем же индексом. Если элементы совпадают, заменяем их в списках на символ соответствующий "корове" - "C"
# переходим к проверке следующего элемента. Добавляем 1 к счетчику максимальнго числа проверок (он же становится
# индексом ind выбора элементов при определении остатка от деления на 4), и вызываем функцию проверки снова.
# Проверяем счетчик, если он равен 8 подсчитываем количество коров и быков и выходим из проверки.
# 3. Проверка "быков" начинается при достижении счётиком i значения >3. Сохранять найденных быков достаточно только в
# одном списке, в котором ведется поиск, т.к повторного прохода по сипску пользователя после проверки всех быков не будет.
#
# числа сохраняем в списках для возможности более простого изменения значений(отметки "быков"["B"] и "коров"["C"])

from random import sample, randint


def bulls_cows():
    # ===================ПРОВЕРКА РЕКУРСИЕЙ КОРОВ(C) И БЫКОВ(B)================
    def chek_number(i=0):
        if i == 8:
            return
        ind = i % 4
        if player_num[ind] in copy_mind_number:
            if player_num[ind] == copy_mind_number[ind]:
                player_num[ind] = copy_mind_number[ind] = "C"
                return chek_number(i + 1)
            elif i > 3:
                copy_mind_number[copy_mind_number.index(player_num[ind])] = "B"
                return chek_number(i + 1)
            else:
                chek_number(i + 1)
        else:
            return chek_number(i + 1)

    # =========================================================================
    MENU_CLR = "\u001b[38;5;121m"
    MSG_CLR = "\u001b[38;5;42m"
    HELP_CLR = "\u001b[38;5;240m"
    ALRM_CLR = "\u001b[38;5;162m"
    RES = "\033[0m"

    while True:
        print(f"{MENU_CLR}БЫКИ И КОРОВЫ.\n\t{HELP_CLR}Выход из игры - Q.\n\tПодсказка - S\n{RES}")
        while True:
            game_type = input(
                f"{MENU_CLR}Какой вариант игры Вы желаете сыграть?\n\t1. Классический(загаданные цифры не повторяются)"
                f"\n\t2. Усложненный(загаданные цифры могут повторяться): {RES}")
            if game_type == "1":
                # классический вариант(загаданные цифры уникальны)
                mind_number = list(map(str, sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)))
                break
            elif game_type == "2":
                # усложненный вариант(загаданные цифры могут повторяться)
                mind_number = list(map(str, [randint(0, 9) for _ in range(4)]))
                break
            else:
                print(f"{ALRM_CLR}Сперва нужно выбрать вариант игры.{RES}")
        # Процесс отгадывания и проверки
        while True:
            copy_mind_number = [elm for elm in mind_number]
            # контроль ввода
            while True:
                player_num = input(
                    f"{MENU_CLR}Введите предполагаемый 4х значный номер:{RES} ")
                if player_num == "Q" or (player_num.isdigit() and len(player_num) == 4):
                    break
                elif player_num == "S":
                    print(f"{HELP_CLR}\tподсказка: {' '.join(mind_number)}{RES}")
                else:
                    print(f"{ALRM_CLR}Не верный ввод, попробуйте еще раз.{RES}")
            # контроль победы и выхода
            player_num = [_ for _ in player_num]
            if mind_number == player_num:
                print("Вы отгадали число!!!")
                player_num[0] = input(f"{MENU_CLR}Чтобы продолжить нажмите Enter, выйти из игры - Q: {RES}")
                break
            elif player_num[0] == "Q":
                break
            # Проверка
            chek_number()
            # вывод результата проверки
            print(f"{MSG_CLR}Быков {copy_mind_number.count('B')}, коров {copy_mind_number.count('C')}{RES}")
        # Выход из игры
        if player_num[0] == "Q":
            print(f"{MENU_CLR}Good buy!{RES}")
            break


bulls_cows()

# ================================================================================================================
# ================================================================================================================

print("\nЗадание 4. Ход Конем.\n")
from winsound import Beep


def check_input(invite_str: str, check: callable):
    """
    Функция принимает строку с приглашением ввода переменной - invite, и условие валидности переменной
    определенное в функции, передаваемой через параметр check (check = lambda x: 0 < x)
    """
    while True:
        try:
            inp_value = input(invite_str)
            if check(inp_value):  # проверка соответствия введенного значения условию валидности
                break
            else:
                print("Не корректный ввод, попробуйте еще раз.")
        except Exception as exc:
            print("Ошибка ввода, попробуйте еще раз:", repr(exc))
    return inp_value


def print_grid(matrix: list[[]]):
    DESK_LETTER = '\u001b[38;5;' + '106' + 'm'
    BLACK_CLR_PAD = '\u001b[48;5;' + '237' + 'm'
    WHITE_PAD = '\u001b[48;5;' + '214' + 'm'
    RESET_COLOR = '\033[0m'

    for row in range(len(matrix)):
        print(DESK_LETTER + f"{'87654321'[row]:^3}" + RESET_COLOR, end="")
        for col in range(len(matrix[0])):
            CLR_PAD = BLACK_CLR_PAD if (row * 7 + col) % 2 else WHITE_PAD
            symb = matrix[row][col] if matrix[row][col] > -1 else ""
            # symb = matrix[row][col] if matrix[row][col] > -1 else matrix[row][col]
            print(CLR_PAD + f"{symb:^3}" + RESET_COLOR, end="")
        print()
    print(DESK_LETTER, end="")
    [print(f"{el:^3}", end="") for el in " abcdefgh"]
    print(RESET_COLOR)


def convert_to_chess(cell: tuple):
    return "abcdefgh"[cell[1]] + "87654321"[cell[0]]


def create_chess_desk(desk_size: int = 8) -> list[[]]:
    desk = [[-1 for _ in range(desk_size)] for _ in range(desk_size)]
    return desk


def get_cell_indx(cell_str: str) -> tuple[int, int]:
    row_col_index = ("87654321".index(cell_str[1]), "abcdefgh".index(cell_str[0].lower()))
    return row_col_index


chess_desk = create_chess_desk()


def check_cell(move: tuple[int, int], from_cell: tuple[int, int], desk=None) -> bool:
    """ Проверяет ячейку на возможность хода"""
    if desk is None:
        desk = chess_desk
    to_cell = (from_cell[0] + move[0], from_cell[1] + move[1])
    # проверка: ход в пределах доски и свободна ли ячейка
    if (-1 < to_cell[0] < 8) and (-1 < to_cell[1] < 8) and (desk[to_cell[0]][to_cell[1]] == -1):
        return True
    else:
        return False


# Используем последовательность для перебора возможных ходов
MOVE_SEQUENCE = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
# Старт. Ввод начальных координат пользователем
invite = "Введите начальное положение фигуры, \nс которой начнется обход всех клеток шахматной доски в формате 'e8': "
check = lambda x: len(x) == 2 and x[0] in "abcdefghABCDEFGH" and x[1] in "12345678"

# ДЛЯ РАБОТЫ С ПОЛЬЗОВАТЕЛЕМ
curr_cell = [0, 0]
# curr_cell = get_cell_indx(check_input(invite, check))

attempt = 1
make_move = (0, 0)  # На первом ходу перемещение = 0,0
pass_count = 0  # Счетчик ходов


def count_poosible_move(newcell: tuple[int, int]) -> int:
    # собираем информацию о возможных ходах. Возвращаем список с количеством ходов
    count = 0
    for count_move in MOVE_SEQUENCE:
        if check_cell(count_move, newcell):
            count += 1
    return count


def party_chess(start_pos: tuple = curr_cell):
    next_pass_recurs(start_pos)
    print_grid(chess_desk)
    print()


def next_pass_recurs(cell: tuple, pass_count=0):
    chess_desk[cell[0]][cell[1]] = pass_count + 1  # отметили как пройденную номером хода
    result = False
    if pass_count == 63:
        # записываем последний ход
        chess_desk[cell[0]][cell[1]] = pass_count + 1
        result = True
    # обход возможных ходов и вызов для них функции сбора статистики
    else:
        statistic_moves = []
        for count_move in MOVE_SEQUENCE:
            # проверить возможные ходы
            if check_cell(count_move, cell):
                new_cell = (cell[0] + count_move[0], cell[1] + count_move[1])
                passes_for_new_cell = (count_poosible_move(new_cell), new_cell)
                statistic_moves.append(passes_for_new_cell)
        if statistic_moves:
            choice_list = [x for x in statistic_moves if x[0] == min(statistic_moves)[0]]
            for next_move in choice_list:
                if next_pass_recurs(next_move[1], pass_count + 1):
                    chess_desk[cell[0]][cell[1]] = pass_count + 1  # отметили как пройденную номером хода
                    # Удачная попытка, выход из рекурсии
                    result = True
                    break
                else:
                    # стираем неудачный ход, пытаемся следующей итерацией пройтись по альтернативной ветке
                    chess_desk[next_move[1][0]][next_move[1][1]] = -1
    return result


def test_chess():
    global curr_cell
    global chess_desk
    global attempt
    for col in range(0, 8):
        for row in range(0, 8):
            # curr_cell = (randint(0, 7), randint(0, 7))
            curr_cell = (row, col)
            print(f"========== ИГРА {col * 8 + row + 1} ==========")
            print("\t\t\tСтартовый ход", convert_to_chess(curr_cell), "\n")
            attempt = 1
            chess_desk = create_chess_desk()
            try:
                party_chess(curr_cell)
            except Exception as exc:
                print("Неудача на", curr_cell)
                print_grid(chess_desk)
                Beep(600, 700)


test_chess()

# Для игры с пользователем запустить party_chess() и снять комментарии со строки 86 (input)
# party_chess()

# Потрачено примерно 3 дня(не считая соперничества с Эйлером и Варнсдорфом ~ еще день)
# Тесты обнаружили проблемы с реализацией на ходах a5, b2, d5
# Причина была в реализации выхода из рекурсии и контроле списка потенциальных ходов
# Глобальный список не сохранял промежуточные экземпляры вариантов ходов...
# Проблемы устранены
# Пришлось обратиться за помощью в интернет
# Основная реализация написана самостоятельно, выход из рекурсии позаимствован.

# ================================================================================================================
# ================================================================================================================
