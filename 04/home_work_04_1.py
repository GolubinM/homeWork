# -------------------------------------------------------------------------------
print("Модуль 3. Циклы. Часть 4")
print("Задание 1. простые числа в диапазоне, указанном пользователем")
prime_numbers = []  # Список простых чисел

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

for number in range(numbers[0], numbers[1] + 1):
    if number < 2:
        continue  # числа меньше 2 не являются простыми числами, исключаем их из диапазона проверки
    prime_atr = True
    for divider in range(2, number // 2 + 1):
        if not number % divider:
            prime_atr = False
            break
    if prime_atr:
        prime_numbers.append(number)
print("Простые числа из заданного диапазона: ")
print(*prime_numbers, sep=", ")
# -------------------------------------------------------------------------------

print("\nЗадание 3. Таблица умножения в диапазоне заданном пользователем от 1 до 9")
# Интерактивное задание диапазона
msg_error_input = "Ошибка ввода! Попробуйте еще раз:"
numbers = []
for i in range(2):
    while True:
        # контроль ввода значений диапазона, вывод сообщения при выходе из заданного диапазона
        try:
            num = int(input(f"Введите {i + 1}-ю границу диапазона: "))
            if num < 1 or num > 9:
                raise ValueError(f"Значение {num} вне диапазона 1:9")
            numbers.append(num)
            break
        except ValueError as exc:
            print(msg_error_input, repr(exc))
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]

for i in range(numbers[0], numbers[1] + 1):
    for factor in range(1, 10):
        # Если результат длиной один символ и между знаком равно пробелы нужно корректировать выравнивание столбцов
        # дополнительным символом табуляции. tab_count решает эту задачу.
        tab_count = 3 if i * factor < 10 else 2  # выбор множителя для табуляции
        print(f"{i}*{factor} = {i * factor}", end=tab_count * "\t")
    print()
# -------------------------------------------------------------------------------

