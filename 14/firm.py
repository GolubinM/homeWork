# Задание 3
# Создайте программу «Фирма». Нужно хранить ин-
# формацию о человеке: ФИО, phone, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поис-
# ка, замены данных. Используйте словарь для хранения
# информации.

def firm():
    MENU_CLR = '\u001b[38;5;' + '106' + 'm'
    DATA_CLR = '\u001b[38;5;' + '176' + 'm'
    DATA_BR_CLR = '\u001b[38;5;' + '178' + 'm'
    RESET_COLOR = '\033[0m'
    employees: dict = {
        "Ленни Пенни Уилкенс": {"phone": "+1-123-45-67", "email": "lenn-penn@firm.com", "job_title": "boss",
                                "cabinet": "101", "skype": "+1-123-75-67"},
        "Бернард Феодор Кинг": {"phone": "+1-523-45-68", "email": "bern-king@firm.com", "job_title": "manager",
                                "cabinet": "102", "skype": "+1-123-75-67"},
        "Гарри Штаерн Галла": {"phone": "+1-122-10-10", "email": "garr-gall@firm.com", "job_title": "driver",
                               "cabinet": "103", "skype": "+1-123-75-67"},
        "Элвин Ист Эрнест": {"phone": "+1-905-45-54", "email": "elv-east@firm.com", "job_title": "accountant",
                             "cabinet": "104", "skype": "+1-123-75-67"}, }

    def check_unit(unit):
        """Проверка наличия ключа в справочнике, возвращает True или False, опционально выводит сообщение
         о результате проверки"""
        if unit in employees:
            return True
        print("Сотрудника с таким именем нет в базе данных.")
        return False

    def print_unit_data(player_prn):
        print(DATA_CLR+player_prn+RESET_COLOR)
        if not employees.get(player_prn, False):
            print(RESET_COLOR, end="")
            return
        for data in employees[player_prn]:
            print("\t"+DATA_CLR + data + ":", DATA_BR_CLR+employees[player_prn][data]+RESET_COLOR)

    def print_unit(prn_data: bool = False):
        if prn_data:
            for player_prn in employees:
                print_unit_data(player_prn)
        else:
            print(DATA_CLR + ", ".join(employees.keys()) + RESET_COLOR)

    def personal(sel, unit=None):
        if sel == "1":
            unit = input("Добавление сотрудника:\n\tВведите ФИО сотрудника: ")
            employees.setdefault(unit, {"phone": ""})  # значение по умолчанию для корректной обработки словаря (п.5)
            personal("5", unit)  # рекурсивно заполняем данные для нового сотрудника
            print_unit()
        elif sel == "2":
            unit = input("Удаление сотрудника:\n\tВведите ФИО сотрудника: ")
            if check_unit(unit):
                employees.pop(unit)  # не использую встроенные возможности проверки, для сокращ. кода, вывода ошиб сообщ
            print_unit()
        elif sel == "3":
            unit = input("\tВведите ФИО чтобы найти сотрудника и вывести данные о нем: ")
            if check_unit(unit):
                print_unit_data(unit)
        elif sel == "4":
            unit = input("\tВведите ФИО сотрудника у которого вы хотите отредактировать ФИО: ")
            if check_unit(unit):
                new_key = input("\tВведите новые ФИО: ")
                replace_old = True
                if check_unit(new_key):
                    print("Новые ФИО уже присутствует в базе! Если продолжить, "
                          f"все данные связанные с {DATA_BR_CLR}{new_key}{RESET_COLOR}\n"
                          f"будут заменены данными {DATA_CLR}{unit}{RESET_COLOR}!!!")
                    replace_old = input("Продолжить - Enter. Отменить - 0: ")
                if new_key != "" and replace_old != "0":
                    employees[new_key] = employees.pop(unit)
                    print_unit()
                else:
                    print("\t\tФИО не были отредактированы.")
        elif sel == "5":
            if not unit:  # Если пункт 5 вызывается непосредственно из меню (не рекурсивно)
                print("\t\tИзменить/добавить данные сотрудника: ")
                unit = input('\t\tВведите ФИО сотрудника, для которого необходимо изменить данные: ')
            if check_unit(unit):
                print_unit_data(unit)
                print("\t\tКакие данные вы бы хотели изменить или добавить: ", end="")
                data_to_update = input()
                if data_to_update != "":
                    if data_to_update not in employees[unit]:
                        print(
                            f"\t\tДля сотрудника {DATA_BR_CLR}{unit}{RESET_COLOR} будет добавлен новый параметр:"
                            f" {DATA_BR_CLR}{data_to_update}{RESET_COLOR}")
                    else:
                        print(f"\t\tДля сотрудника {DATA_BR_CLR}{unit}{RESET_COLOR}"
                              f" будут изменены данные в параметре: {DATA_BR_CLR}{data_to_update}{RESET_COLOR}")
                    employees[unit][data_to_update] = input(
                        f"\t\tВведите значение для параметра {DATA_BR_CLR}{data_to_update}{RESET_COLOR}: ")
                    print_unit_data(unit)
        elif sel == "6":
            print_unit(True)

    print("Сотрудники \"Firm\":", end="\n\t")
    print_unit(False)
    while True:
        sel = input(MENU_CLR +
                    "Что вы желаете сделать:"
                    "\n\t0.Выйти"
                    "\n\t1.Добавить сотрудника"
                    "\n\t2.Удалить сотрудника"
                    "\n\t3.Найти сотрудника и вывести данные"
                    "\n\t4.Откорректировать ФИО сотрудника"
                    "\n\t5.Изменить/добавить данные сотрудника(телефон, должность, e-mail и др.)"
                    "\n\t6.Вывести список всех сотрудников и данные по ним: " + RESET_COLOR)
        if sel == "0":
            print("Good buy!")
            break
        else:
            personal(sel)


firm()
