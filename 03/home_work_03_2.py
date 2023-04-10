# -------------------------------------------------------------------------------
print("Модуль 3. Циклы. Часть 2")
print("\nЗадание 1. Отдельно сумма четных, нечетных, и чисел, кратных 9 в указанном диапазоне,"
      " а также среднеарифметическое каждой группы")
collect_aliquot_9 = []  # Список чисел кратных 9
collect_odd = []  # Список нечетных чисел
collect_even = []  # Список четных чисел

# Интерактивное задание диапазона
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
numbers = []
for i in range(2):
    while True:
        try:
            numbers.append(int(input(f"Введите {i + 1}-ю границу диапазона: ")))
            break
        except ValueError:
            print(msg_error_input)
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]
# обработка диапазона
for number in range(numbers[0], numbers[1] + 1):
    if number % 2:
        collect_odd.append(number)
    else:
        collect_even.append(number)
    if not number % 9:
        collect_aliquot_9.append(number)
print(
    f"Нечетные числа диапазона:\n\t"
    f"сумма:{sum(collect_odd)}; среднеарифметическое:{sum(collect_odd) / len(collect_odd)};")
print(
    f"Четные числа диапазона:\n\t"
    f"сумма:{sum(collect_even)}; среднеарифметическое:{sum(collect_even) / len(collect_even)};")
print(
    f"Числа диапазона кратные 9:\n\t"
    f"сумма:{sum(collect_aliquot_9)}; среднеарифметическое:{sum(collect_aliquot_9) / len(collect_aliquot_9)};")
# -------------------------------------------------------------------------------
print("\nЗадание 2. Вертикальная линия из введенного символа, указанной длины")
while True:
    try:
        length = int(input("Введите число символов - длину линии: "))
        symbol = input("Введите символ, из которого рисуем вертикальную линию: ")
        break
    except ValueError:
        print(msg_error_input)
for i in range(length):
    print(symbol)
# -------------------------------------------------------------------------------
print("\nЗадание 3. Positive, negative, equal to zero, 7 to stop and print «Good bye!»")
while True:
    while True:
        try:
            num = int(input("Введите число: "))
            break
        except ValueError:
            print(msg_error_input)
    if num == 7:
        print("Good bye!")
        break
    elif num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")
# -------------------------------------------------------------------------------
print("\nЗадание 4. Сумму, максимум и минимум введенных чисел на каждом вводе, 7 выход и вывод «Good bye!»")
numbers = []
while True:
    while True:
        try:
            num = int(input("Введите число: "))
            break
        except ValueError:
            print(msg_error_input)
    if num == 7:
        print("Good bye!")
        break
    numbers.append(num)
    print(f"Сумма введённых чисел:{sum(numbers)}; максимальное число: {max(numbers)}; минимально число:{min(numbers)}")
# -------------------------------------------------------------------------------
print("\nЗадание 4.1 С ПЕРЕМЕННЫМИ в цикле, как упоминалось на уроке\n"
      " Сумму, максимум и минимум введенных чисел на каждом вводе, 7 выход и вывод «Good bye!»")
sum_num = 0
min_num = float("inf")  # максимально большое начальное значение минимума
max_num = float("-inf")  # минимальное начальное значение максимума
while True:
    while True:
        try:
            num = int(input("Введите число: "))
            break
        except ValueError:
            print(msg_error_input)
    if num == 7:
        print("Good bye!")
        break
    else:
        sum_num += num
        min_num = num if min_num > num else min_num
        max_num = num if max_num < num else max_num
    print(f"Сумма введённых чисел:{sum_num}; максимальное число: {max_num}; минимально число:{min_num}")
# -------------------------------------------------------------------------------
