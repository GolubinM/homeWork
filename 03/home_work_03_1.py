# -------------------------------------------------------------------------------
print("Модуль 3. Циклы. Часть 1")
print("\nЗадание 1. Если число из заданного диапазона кратно 7, выводить на экран.")
collect_7 = []  # Список чисел кратных 7
# Интерактивное задание диапазона
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
numbers = []
for i in range(2):
    # контроль входящих данных
    while True:
        try:
            numbers.append(int(input(f"Введите {i + 1}-ю границу диапазона: ")))
            break
        except ValueError:
            print(msg_error_input)
# располагаем введенные числа по возрастанию
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]

# вывод чисел кратных 7
print("Числа кратные 7: ", end="")
for number in range(numbers[0], numbers[1] + 1):
    if not number % 7:
        collect_7.append(number)
print(*collect_7, sep=", ")

# -------------------------------------------------------------------------------
print("\nЗадание 2. Нужно вывести на экран:\n" + 2 * "\t" +
      "1. Все числа диапазона;\n" + 2 * "\t" +
      "2. Все числа диапазона в убывающем порядке;\n" + 2 * "\t" +
      "3. Все числа, кратные 7;\n" + 2 * "\t" +
      "4. Количество чисел, кратных 5.")

collect_between = []
collect_7 = []  # Список чисел кратных 7
count_collect_5 = 0  # Количество чисел кратных 5
# Интерактивное задание диапазона
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
numbers = []
for i in range(2):
    # контроль входящих данных
    while True:
        try:
            numbers.append(int(input(f"Введите {i + 1}-ю границу диапазона: ")))
            break
        except ValueError:
            print(msg_error_input)
# располагаем введенные числа по возрастанию
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]

msg_warning = ""  # Предупреждениe для слишком большого диапазона значений >70.000


# Определение собственного исключения - RangeIsTooWidth (для закрепления материала по исключениям)
class RangeIsTooWidth(ValueError):
    msg = "Слишком большой диапазон значений!!!\n" \
          "Для отображения в консоли Pycharm всех значений, возможно, придется увеличить значение буфера консоли:\n" \
          "Pycharm:File->Settings->Editor->Console->Override console cycle buffer size"


# предупреждение для слишком широкого диапазона(при котором результат возможно не будет выведен в консоль полностью)
# (только с целью закрепления материала по исключениям) (При ширине диапазона ~75000 начальные  строки пропадают)
try:
    if numbers[1] - numbers[0] > 70000:
        raise RangeIsTooWidth(numbers)
except RangeIsTooWidth as exc:
    msg_warning = [repr(exc), exc.msg]  # Подготовка предупреждения "слишком широкого диапазона", для вывода в конце

# обработка диапазона

for number in range(numbers[0], numbers[1] + 1):
    collect_between.append(number)
    if not (numbers[0]) % 7:
        collect_7.append(numbers[0])
    if not numbers[0] % 5:
        count_collect_5 += 1
    numbers[0] += 1
print("1. Все числа диапазона: ", end="")
print(*collect_between, sep=", ")
print("2. Все числа диапазона в убывающем порядке: ", end="")
print(*collect_between[::-1], sep=", ")
print("3. Все числа, кратные 7: ", end="")
print(*collect_7, sep=", ")
print("4. Количество чисел, кратных 5: ", end="")
print(count_collect_5, sep=", ")
# Вывод предупреждения, если обрабатываемый диапазон содержал более 70.000 значений
if msg_warning:
    print(*msg_warning, sep="\n")

# -------------------------------------------------------------------------------
print("\nЗадание 3. Fizz Buzz (внутри диапазона")
# Интерактивное задание диапазона
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
numbers = []
results = []
for i in range(2):
    # контроль входящих данных
    while True:
        try:
            numbers.append(int(input(f"Введите {i + 1}-ю границу диапазона: ")))
            break
        except ValueError:
            print(msg_error_input)
# располагаем введенные числа по возрастанию
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]
# Обработка диапазона
for number in range(numbers[0], numbers[1] + 1):
    if not number % 15:
        results.append("Fizz Buzz")
    elif not number % 3:
        results.append("Fizz")
    elif not number % 5:
        results.append("Buzz")
    else:
        results.append(number)
print(*results, sep=", ")
# ------------------------------------------------------------------------
