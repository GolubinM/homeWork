import math

print("Модуль 2. Операторы ветвлений. Часть 3")
print("Задание 1. Fizz Buzz.")
number = int(input("Введите число от 1 до 100(включительно): "))
string = ""
if 0 < number < 101:
    if not number % 3:
        string = "Fizz"
    if not number % 5:
        # Если кратно и 3 и 5 объединяем, результат "Fizz Buzz", если только 5 удаляем ведущий пробел, результат "Buzz"
        # позволяет избежать дополнительной проверки на кратность 15(3 и 5)
        string = (string + " Buzz").lstrip()
    if not string:  # если string остается пустой строкой выводим число
        string = number
    print(string)
else:
    print("Ошибка!")
# ------------------------------------------------------------------------
print("\nЗадание 2.1. число в степень от нулевой до седьмой включительно(контроль ввода - try/except)")
# используем try/except для контроля значения степени
try:
    base = float(input("Введите число(основание), которое возводим в степень: "))
    power = float(input("Выберете степень числа от 0 до 7(включительно): "))
    if not 0 <= power <= 7:
        raise Exception
    print(f"Результат возведения в степень: {base ** power}")
except Exception:
    print("Ошибка ввода: степень должна иметь значение от 0 до 7(включительно).")

# ------------------------------------------------------------------------
print("\nЗадание 2.2. число в степень от нулевой до седьмой включительно(контроль ввода - while).")
power2 = -1  # инициализация начального значение степени вне значений допустимых условием
base = float(input("Введите число(основание), которое возводим в степень: "))
# используем while для контроля значения степени
while not 0 <= power2 <= 7:
    power2 = float(input("Выберете степень числа от 0 до 7(включительно): "))
print(f"Результат возведения в степень: {base ** power2}")

# ------------------------------------------------------------------------
#
print("\nЗадание 3. Стоимость разговора.")
price_Megafon = 8.99
price_MTS = 8.78
price_Beeline = 8.92
price_Tele2 = 0.01
during_call = 0
while not during_call:
    during_call = int(input("Введите длительность разговора в минутах: "))
operator = 0
while not 0 < operator < 5:
    try:
        operator = int(input("Введите номер оператора от 1 до 4, абоненту которого был осуществлен звонок:"
                             "\n1) Megafon(тариф - 8.99 руб/мин)\n2) MTS(тариф - 8.78 руб/мин)"
                             "\n3) Tele2(тариф - 0.01 руб/мин)\n4) Beeline(тариф - 8.92 руб/мин)\n"))
    except ValueError:
        print("Ошибка ввода! Попробуйте еще раз")
if operator == 1:
    call_price = price_Megafon
elif operator == 2:
    call_price = price_MTS
elif operator == 3:
    call_price = price_Tele2
else:
    call_price = price_Beeline
ring_cost = during_call * call_price
print(f"Стоимость звонка абоненту выбранного оператора составила: {ring_cost} руб.")

# -------------------------------------------------------------------------------
#
print("\nЗадание 4. Зарплата менеджера.")

total_managers = 3  # количество менеджеров
min_salary = 200  # фиксированная минимальная выплата, независящая от уровня продаж
best_manager_prize = 200  # установка размера премии лучшему менеджеру
salary = []  # инициализация массива для хранения сумм выплат
best_manager_index = 0  # для определения количества менеджеров с лучшими продажами, вывода информации о лучшем
highest_salary = 0  # для определения единственного лучшего менеджера
sales_level = -1  # для контроля вводимых пользователем значений продаж

for i in range(total_managers):
    # контроль входящих данных
    while sales_level < 0:
        try:
            sales_level = int(input(f"Введите уровень продаж для менеджера {i + 1}: "))
        except ValueError:
            print("Ошибка ввода! Попробуйте еще раз")
    # выбор процента от продаж и вычисление размера вознаграждения
    if sales_level < 500:
        personal_prize = 0.03
    elif sales_level < 1000:
        personal_prize = 0.05
    else:
        personal_prize = 0.08
    # добавление в список суммы выплаты менеджеру без учета премии лучшему менеджеру
    salary.append(sales_level * personal_prize + min_salary)
    # сброс контрольного значения продаж, подготовка к следующему вводу
    sales_level = -1
    # поиск максимальной выплаты
    if salary[i] > highest_salary:
        highest_salary = salary[i]

# проверка сколько менеджеров выполнило максимальное количество продаж:
# если больше одного, значит лучшего нет, премию не начисляем
best_manager_count = 0
for i in range(total_managers):
    if highest_salary == salary[i]:
        best_manager_count += 1
        best_manager_index = i
if best_manager_count > 1:
    best_manager_index = -1  # сброс индекса лучшего менеджера(для строки итогов)
else:
    # иначе лучший менеджер один - начисляем ему премию
    salary[best_manager_index] = salary[best_manager_index] + best_manager_prize

# Вывод итогов на экран
for i in range(total_managers):
    its_best_manager = " - этот менеджер лучший!" if i == best_manager_index else ""
    print(f"Выплата менеджеру {i + 1} составит: {salary[i]}", its_best_manager)

# -------------------------------------------------------------------------------
# Дополнительное задание---------------------------------------------------------
# -------------------------------------------------------------------------------
print("\nМодуль 2. Операторы ветвлений. Часть 1")
print("Задание 1. Сумма или произведение трёх чисел.")
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
total_numbers = 3  # Количество обрабатываемых элементов
numbers = []
# Ввод операндов
for i in range(total_numbers):
    # контроль входящих данных
    ready = False
    while not ready:
        try:
            operand = float(input(f"Введите {i + 1}-e число: "))
            numbers.append(operand)
            ready = True
        except ValueError:
            print(msg_error_input)
# Выбор операции
number_func = 0
while number_func not in range(1, 3):
    try:
        number_func = int(input(f"Выберете номер операции, которую желаете произвести с введенным числами:"
                                f"\n1) Сложение:\n2) Умножение:\n"))
    except ValueError:
        print(msg_error_input)
if number_func == 1:
    result = sum(numbers)
else:
    result = math.prod(numbers)
print(f"Результат вычислений: {result}")
# -------------------------------------------------------------------------------
# Модуль 2. Операторы ветвлений. Часть 1
print("\nЗадание 2. Максимум, минимум, среднеарифметическое трёх чисел.")
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
total_numbers = 3  # Количество обрабатываемых элементов
numbers = []
# Ввод операндов
for i in range(total_numbers):
    # контроль входящих данных
    ready = False
    while not ready:
        try:
            operand = float(input(f"Введите {i + 1}-e число: "))
            numbers.append(operand)
            ready = True
        except ValueError:
            print(msg_error_input)
# Выбор операции
number_func = 0
while number_func not in range(1, 4):
    try:
        number_func = int(input(f"Выберете номер операции, которую желаете произвести с введенным числами:"
                                f"\n1) Максимум:\n2) Минимум:\n3) Среднеарифметическое\n"))
    except ValueError:
        print(msg_error_input)
if number_func == 1:
    result = max(numbers)
elif number_func == 2:
    result = min(numbers)
else:
    result = sum(numbers) / len(numbers)

print(f"Результат вычислений: {result}")

# -------------------------------------------------------------------------------
# Модуль 2. Операторы ветвлений. Часть 1
print("\nЗадание 3. Метры в мили, дюймы или ярды.")
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
# контроль входящих данных
ready = False
while not ready:
    try:
        operand = float(input(f"Введите количество метров: "))
        ready = True
    except ValueError:
        print(msg_error_input)
# Выбор операции
number_func = 0
while number_func not in range(1, 4):
    try:
        number_func = int(input(f"Выберете номер единицы измерения, в которую следует перевести метры:"
                                f"\n1) мили:\n2) дюймы:\n3) ярды\n"))
    except ValueError:
        print(msg_error_input)
# print(f"numbers {numbers}")
# print(f"number_func {number_func}")
if number_func == 1:
    print(f"Результат конвертации в мили: {operand / 1609}")
elif number_func == 2:
    print(f"Результат конвертации в дюймы: {operand * 39.37}")
else:
    print(f"Результат конвертации в ярды: {operand * 1.094}")
# -------------------------------------------------------------------------------
print("\nМодуль 2. Операторы ветвлений. Часть 2")
print("Задание 1. Дни недели.")
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
# контроль входящих данных
day_number = 0
while day_number not in range(1, 8):
    try:
        day_number = int(input(f"Введите номер дня недели 1-7: "))
    except ValueError:
        print(msg_error_input)
if day_number == 1:
    print("Понедельник")
elif day_number == 2:
    print("Вторник")
elif day_number == 3:
    print("Среда")
elif day_number == 4:
    print("Четверг")
elif day_number == 5:
    print("Пятница")
elif day_number == 6:
    print("Суббота")
else:
    print("Воскресенье")

# day_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# print(day_list[day_number - 1])
# -------------------------------------------------------------------------------
# Модуль 2. Операторы ветвлений. Часть 2
print("\nЗадание 2. Месяцы.")
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
# контроль входящих данных
month_number = 0
while month_number not in range(1, 13):
    try:
        month_number = int(input(f"Введите номер месяца 1-12: "))
    except ValueError:
        print(msg_error_input)
if month_number == 1:
    print("Январь")
elif month_number == 2:
    print("Февраль")
elif month_number == 3:
    print("Март")
elif month_number == 4:
    print("Апрель")
elif month_number == 5:
    print("Май")
elif month_number == 6:
    print("Июнь")
elif month_number == 7:
    print("Июль")
elif month_number == 8:
    print("Август")
elif month_number == 9:
    print("Сентябрь")
elif month_number == 10:
    print("Октябрь")
elif month_number == 11:
    print("Ноябрь")
else:
    print("Декабрь")
# -------------------------------------------------------------------------------
# Модуль 2. Операторы ветвлений. Часть 2
print("\nЗадание 3. negativ/zero/positiv.")
msg_error_input = "Ошибка ввода! Попробуйте еще раз"
# контроль входящих данных
ready = False
while not ready:
    try:
        num = float(input("Введите число: "))
        ready = True
    except ValueError:
        print(msg_error_input)
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

# -------------------------------------------------------------------------------
# Модуль 2. Операторы ветвлений. Часть 2
print("\nЗадание 4. Определить равны ли числа. Если нет, вывести их на экран в порядке возрастания.")

msg_error_input = "Ошибка ввода! Попробуйте еще раз"
total_numbers = 2  # Количество обрабатываемых элементов
numbers = []
# Ввод операндов
for i in range(total_numbers):
    # контроль входящих данных
    ready = False
    while not ready:
        try:
            operand = float(input(f"Введите {i + 1}-e число: "))
            numbers.append(operand)
            ready = True
        except ValueError:
            print(msg_error_input)
# сравнение чисел
if numbers[0] != numbers[1]:
    if numbers[0] > numbers[1]:
        (numbers[0], numbers[1]) = (numbers[1], numbers[0])
    print(numbers[0], numbers[1])  # print(numbers) или списком.
