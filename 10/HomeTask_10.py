from random import randint, seed

seed(5)  # для упрощения контроля расчетов


def print_grid(grid: list[[]], cell_width=5):
    """
    вывод матрицы с форматированием, cell_width - ширина поля одного элемента матрицы
    :param grid:
    :param cell_width:
    :return:
    """
    [[print(f"{el:>{cell_width}}", end="") for el in row + ["\n"]] for row in grid]


# =====================================================================================================
print("Задание 1. Сумма отсортированных значений столбцов матрицы.")
# 1. определяем количество итераций = начальное кол-во "колонок" матрицы
# 2. для каждой строки в матрице определяем индекс макс эл-та
# 3. находим и извлекаем его (pop())  во "временный" список
# 4. макс эл-т из "временного" списка, добавляем в сумму sum_max, переходим к след итерации (п.2)

# подготовка матрицы
cols = range(randint(3, 4))  # ширина
rows = range(randint(2, 3))  # высота
matrix = [[randint(0, 10) for _ in cols] for _ in rows]
print_grid(matrix)
# решение
sum_max = sum([max([row.pop(row.index(max(row))) for row in matrix]) for _ in cols])
print("сумма максимальных чисел = ", sum_max)
print("матрица после просчета", matrix)


# ======То же самое через функцию========================


def sum_max_matrix(matrix: list[[int]]) -> int:
    cols_rng = range(len(matrix[0]))
    return sum([max([row.pop(row.index(max(row))) for row in matrix]) for _ in cols_rng])


# подготовка матрицы
matrix = [[randint(0, 10) for _ in cols] for _ in rows]
print_grid(matrix)
# выполняем функцию
print("сумма максимальных чисел = ", sum_max_matrix(matrix))
print("матрица после просчета", matrix)


# ======С уточнением что удалять эл-ты не обязательно, а только вывести сумму===============
def sum_max_matrix2(matrix: list[[int]]) -> int:
    columns_rng = range(len(matrix[0]))  # в отдельную переменную, чтобы не пересчитывалось при каждой итерации генер.
    matrix = [sorted(row) for row in matrix]
    sum_max = sum([max([rw[cln] for rw in matrix]) for cln in columns_rng])  # максимум по каждой колонке
    return sum_max


# подготовка матрицы
matrix = [[randint(0, 10) for _ in cols] for _ in rows]
print_grid(matrix)
# выполняем функцию
print("сумма максимальных чисел = ", sum_max_matrix2(matrix))
print("матрица после просчета", matrix)

# =====================================================================================================

print("\n\nЗадание 2. Определить периметр острова.")


# решение:
# Необходимо посчитать периметр острова. Периметр острова это сумма всех переходов
# с "воды" на "землю" и с "земли" на "воду". Иными словами сравнение соседних ячеек карты.
# Если соседние ячейки не равны, значит тут часть периметра, которую нужно добавить в общую сумму.
# Сначала считаем по строкам "вертикальные" границы "острова", затем по столбцам сверху вниз
# сосчитаем "горизонтальные" границы "острова". Чтобы посчитать возможные
# границы по краям сетки из каждой строки/столбца просуммируем крайние элементы списка в общую сумму, если они равны 1
# значит эти ячейки имеют внешние границы(границы по краю сетки).


def island_perimeter(grid: list[[int]]) -> int:
    def line_perimetr(line: list[int]) -> int:
        line_border = 0
        for i in range(len(line) - 1):
            line_border += line[i] != line[i + 1]
        line_border += line[0] + line[-1]
        return line_border

    print_grid(grid, 2)
    perimetr = 0
    perimetr += sum(map(line_perimetr, [row for row in grid]))
    columns_rng = range(len(grid[0]))
    perimetr += sum(map(line_perimetr, [[rw[cln] for rw in grid] for cln in columns_rng]))

    return perimetr


def test_islands_perimeter():
    test_grid = [[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 1, 0, 1, 0]]
    test_grid_perim = island_perimeter(test_grid)
    print("Периметр равен:", test_grid_perim, "// Test passed is", test_grid_perim == 22)
    test_grid = [[0, 0, 1, 0, 0], [0, 0, 1, 1, 1]]
    test_grid_perim = island_perimeter(test_grid)
    print("Периметр равен:", test_grid_perim, "// Test passed is", test_grid_perim == 10)
    test_grid = [[0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    test_grid_perim = island_perimeter(test_grid)
    print("Периметр равен:", test_grid_perim, "// Test passed is", test_grid_perim == 12)
    test_grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    test_grid_perim = island_perimeter(test_grid)
    print("Периметр равен:", test_grid_perim, "// Test passed is", test_grid_perim == 18)
    test_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1]]
    test_grid_perim = island_perimeter(test_grid)
    print("Периметр равен:", test_grid_perim, "// Test passed is", test_grid_perim == 4)
    test_grid = [[1, 1, 1, 0, 1, 0], [1, 1, 1, 0, 1, 1], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1]]
    test_grid_perim = island_perimeter(test_grid)
    print("Периметр равен:", test_grid_perim, "// Test passed is", test_grid_perim == 32)


test_islands_perimeter()

# =====================================================================================================

print("\n\nЗадание 3. Сдвинуть сетку(матрицу).")


# решение:
# 1. Считываем количество строк матрицы
# 2. Выпрямляем матрицу
# 3. С помощью среза сдвигаем сетку
# 4. Разбиваем список по строкам (п.1)

def move_grids_elements(grid: list[[int]], k: int) -> list[[int]]:
    print_grid(grid)
    rows_grid = range(len(grid))
    elms_in_row = len(grid[0])
    flat_list = [elm for row in grid for elm in row]
    flat_list = flat_list[-k:] + flat_list[:-k]
    grid = [flat_list[row * elms_in_row:row * elms_in_row + elms_in_row] for row in rows_grid]
    return grid


def test_move_grids_elements():
    test_grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    await_grid = [[16, 17, 18, 19, 20], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    k = 5
    result = move_grids_elements(test_grid, k)
    print("Результат сдвига на", k)
    print_grid(result)
    print("// Test passed is", result == await_grid, "\n")

    k = 6
    result = move_grids_elements(test_grid, k)
    await_grid = [[15, 16, 17, 18, 19], [20, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
    print("Результат сдвига на", k)
    print_grid(result)
    print("// Test passed is", result == await_grid, "\n")

    k = -11
    result = move_grids_elements(test_grid, k)
    await_grid = [[12, 13, 14, 15, 16], [17, 18, 19, 20, 1], [2, 3, 4, 5, 6], [7, 8, 9, 10, 11]]
    print("Результат сдвига на", k)
    print_grid(result)
    print("// Test passed is", result == await_grid, "\n")

    k = 0
    result = move_grids_elements(test_grid, k)
    await_grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    print("Результат сдвига на", k)
    print_grid(result)
    print("// Test passed is", result == await_grid, "\n")


test_move_grids_elements()
