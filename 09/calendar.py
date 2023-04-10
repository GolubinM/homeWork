def print_calendar(clnd: list[list[str | int]]):
    '''Выводит календарь понедельно с красными Сб-Вс и синими Пн-Пт'''
    GD = '\033[94m'
    RD = '\033[91m'
    clnd = [["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]] + clnd
    [[print(f"{GD * (d[0] < 5)}{RD * (d[0] > 4)}{d[1]:>5}", end="\n" * (d[0] == 6)) for d in enumerate(r)] for r in
     clnd]
    print('\033[0m')


def create_calendar(frst: int, days: int) -> list[list[str | int]]:
    '''Создает календарь на месяц с дня недели frst, кол-во дней = days '''
    weeks = round((frst + days - 1) / 7 + 0.4)  # +0.4 округляем вверх без math
    day_in_tbl = [""] * (frst - 1) + list(range(1, days + 1))
    tabl_days = len(day_in_tbl)
    calendar = [[day_in_tbl[dw + 7 * w] for dw in range(0, 7) if (dw + 7 * w) < tabl_days] for w in range(weeks)]
    return calendar


def show_week_days(clnd: list[list[str | int]], start_day: int, end_day: int) -> list[list[str | int]]:
    '''замещает дни вне выбранного диапазона пустой строкой, оставляя в массиве только указанный диапазон дней недели'''
    sel_days = [[""] * (start_day - 1) + week[start_day - 1:end_day] + [""] * (7 - end_day) for week in clnd]
    return sel_days


# создаем календарь на 31 день с пятницы(5)
calendar = create_calendar(3, 30)
print("Выводим все дни:")
print_calendar(calendar)
print("Выводим рабочие дни:")
print_calendar(show_week_days(calendar, 1, 5))
print("Выводим все кроме понедельника и вторника:")
print_calendar(show_week_days(calendar, 3, 7))
