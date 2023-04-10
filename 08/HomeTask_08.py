from random import randint

print("\n\nЗадача 1. Матрицу 10*10 заполнить случайными числами в диапазоне от 10 до 1000.\n"
      "Сосчитать количество трехзначных чисел матрицы, сумма цифр которых кратна 5.")

rows = 10  # задаем высоту матрицы
cols = 10  # задаем ширину матрицы
matrix = list(list(randint(10, 1000) for i in range(cols)) for n in range(rows))  # заполняем матрицу int-ами
for row in range(rows):
    for col in range(cols):
        print(f"{matrix[row][col]:>5}", end="")  # формат и вывод матрицы
    print()
print(f"{'-':-^5}" * cols + "--")

# "Выпрямляем" матрицу, отбираем 3х-значные числа, генерируем список
list_str = list(elm for group in matrix for elm in group if 99 < elm < 1000)
# Отделяем значение разрядов каждого числа определением остатка от целочисленного деления, суммируем цифры,
# проверяем на кратность 5-ке, генерируем список)
list_num5 = list(num for num in list_str if not (num % 10 + num // 10 % 10 + num // 100 % 10) % 5)

count = len(list_num5)  # количество элементов кратное 5
print("Количество трехзначных чисел, сумма цифр которых кратна 5: ", count)
print("Список этих чисел:", list_num5)

# =====================================================================
print("\n\nЗадача 2. Задать размеры матрицы. Заполнить от верхнего левого угла")
while True:
    try:
        cols = range(int(input("Введите ширину матрицы: ")))
        rows = range(int(input("Введите высоту матрицы: ")))
        break
    except ValueError:
        print("Неверное значение попробуйте еще раз")
matrix = list(list(col + row for col in cols) for row in rows)
for row in rows:
    for col in cols:
        print(f"{matrix[row][col]:^5}", end="")
    print()

# =====================================================================
print("\n\nЗадача 3. Матрица 5x5 заполнена случайными числами 0-10."
      "Вывести строку или колонку с минимальной суммой элементов.")
# Решенеие 1:
# 1. Подсчитываем суммы по каждой строке и колонке и помещаем в списки rows_sums, cols_sums
# 2. Определяем минимальное значение сумм по строкам и по столбцам min_val_row, min_val_col
# 3. Определяем индекс выводимой строки/колонки, задаем условия форматирования для корректного вывода
# 4. Выводим макет матрицы с нужной строкой/колонкой

cols = range(5)  # ширина
rows = range(5)  # высота
matrix = list(list(randint(0, 10) for _ in cols) for _ in rows)
for row in rows:
    for col in cols:
        print(f"{matrix[row][col]:^5}", end="")
    print()
rows_sums = list(sum(row) for row in matrix)
cols_sums = list(sum(row[col] for row in matrix) for col in cols)
print("суммы по строкам:", rows_sums, ", суммы по колонкам:", cols_sums, sep="")
min_val_row = min(rows_sums)
min_val_col = min(cols_sums)
print("Вывод линии с минимальной суммой")
if min_val_row < min_val_col:
    # инициализация вывода мин строки
    show_row = rows_sums.index(min_val_row)
    show_col = -1
    print("строка с индексом: ", show_row, ", сумма элементов строки = ", min_val_row, sep="")
else:
    # инициализация вывода мин колонки
    show_row = -1
    show_col = cols_sums.index(min_val_col)
    print("колонка с индексом: ", show_col, ", сумма элементов колонки = ", min_val_col, sep="")

for row in rows:
    for col in cols:
        out = matrix[row][col] if (show_row == row) or (show_col == col) else "·"
        print(f"{out:^5}", end="")
    print()

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Решенеие 2: (короче но вывод не такой красивый)
row_col = matrix + [[r[c] for r in matrix] for c in cols]  # 1. Формируем список строк колонок
row_col_sum = [sum(l) for l in (row_col)]  # 2. Формируем список сумм строк колонок
min_line_ind = row_col_sum.index(min(row_col_sum))  # 3. Находим индекс минимальной строки в списке
min_line = row_col[min_line_ind]  # 4. Выводим "линию" с минимальной суммой по найденному индексу
print("\nРезультат программы: ")
print(*min_line, sep=" " if min_line_ind < 5 else "\n")  # вывод линии в строку или колонку
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# в "одну" строку ))(отвратительно, ничего не понятно, но...)
min_line = (matrix + [[r[c] for r in matrix] for c in cols])[
    ([sum(l) for l in (matrix + [[r[c] for r in matrix] for c in cols])]).index(
        min([sum(l) for l in (matrix + [[r[c] for r in matrix] for c in cols])]))]
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-