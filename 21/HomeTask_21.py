import uuid, pickle, re, glob
from datetime import date, datetime


def firm2():
    MNU = '\u001b[38;5;' + '245' + 'm'
    DAT = '\u001b[38;5;' + '250' + 'm'
    DBR = '\u001b[38;5;' + '252' + 'm'
    DB2 = '\u001b[38;5;' + '245' + 'm'
    DB3 = '\u001b[38;5;' + '245' + 'm'
    RST = '\033[0m'

    def check_color_menu():
        nonlocal DB2, DB3
        if len(employees):
            DB2 = '\u001b[38;5;' + '252' + 'm'
        else:
            DB2 = '\u001b[38;5;' + '245' + 'm'
        if found:
            DB3 = '\u001b[38;5;' + '252' + 'm'
        else:
            DB3 = '\u001b[38;5;' + '245' + 'm'

    def check_unit(unit):
        """Проверка наличия ключа в словаре, возвращает True или False"""
        if unit in employees:
            return True
        print("Сотрудника с таким ID нет в базе данных.")
        return False

    def save_file(fname: str, data: dict):
        with open(fname, 'wb') as f_name:
            pickle.dump(data, f_name)

    def select_by_value(unit, search_field: str = "name") -> dict | bool:
        """возвращает словарь отобранных записей"""
        found = {elm: employees[elm] for elm in employees if
                 employees[elm][search_field].lower().startswith(unit.lower())}
        if found:
            print(f"\t{DAT}Найдено записей: {len(found)}{RST}")
            return found
        print("Записей с такими значениями не найдено в базе данных.")
        return False

    def print_unit_data(keys_pers, sort_flag=True, as_table=False):
        if sort_flag: keys_pers = sorted(keys_pers, key=lambda key: employees[key]["name"])
        if as_table:
            print(
                f"{'№пп':<5}{'ФИО':<35}{'дата рождения':<20}{'должность':<40}{'ID':<40}")
            for cnt, key in enumerate(keys_pers, start=1):
                print(f"{DBR}{cnt:<5}", end="")
                for field, cw in zip(["name", "birth_day", "job_title"], [35, 20, 40]):
                    print(f"{frmt_field(key, field):<{cw}}", end="")
                print(f"{key:<40}{RST}")
        else:
            for cnt, key in enumerate(keys_pers, start=1):
                print(f"\n\t{DAT}({cnt}) ID: {key}{RST}")
                for data in employees[key]:
                    print(f"\t\t{DAT}{data}:{' ' * (12 - len(str(data)))}{DBR}{frmt_field(key, data)}{RST}")

    def input_data(key: str, field: str, invite: str):
        """ Заполнение поля field элемента key словаря employees значениями """
        while True:
            data = input(f"\tвведите {invite}: ")
            if field == "name" and not data:  # обязательное для заполнения поле
                pass
            elif field == "birth_day":
                try:
                    employees[key][field] = datetime.strptime(data, '%d-%m-%Y')
                    break
                except Exception as ex:
                    print("\t\tОшибка ввода даты. Введите дату в формате ДД-ММ-ГГГГ", ex.__repr__())
            else:
                employees[key][field] = data
                break

    def calculate_age(birth_day) -> int:
        """Возвращает количество полных лет для birth_day на текущую дату"""
        today = date.today()
        return today.year - birth_day.year - ((today.month, today.day) < (birth_day.month, birth_day.day))

    def condition_list(condition: str) -> dict:
        """принимает строку с условием отбора, типа '>25', '<25', '25', '25, 31, 100'.
         Возвращает словарь отобранных согласно условию элементов. """
        cnd = "calculate_age(employees[elm]['birth_day'])"
        if re.match(r"[<>]\d+", condition):
            condition = f"{cnd}{condition}"
        elif re.match(r"=?(\d+)(,\s?\d+)?", condition):
            condition = [int(elm.group()) for elm in re.finditer(r"(\d+)((?<=,\s)(\d+))?", condition)]
            condition = f"{cnd} in {condition}"
        else:
            condition = f"{cnd} > 0"
        return {elm: employees[elm] for elm in employees if
                eval(condition, {'calculate_age': calculate_age, 'employees': employees, 'elm': elm})}

    def frmt_field(key: str, field: str) -> str:
        """Форматированный вывод значения поля field"""
        if field == "birth_day":
            return datetime.strftime(employees[key][field], '%d-%m-%Y')
        else:
            return employees[key][field]

    employees = {}
    found = {}
    file_name = None
    print("Сотрудники:")
    while True:
        check_color_menu()
        selct = input(MNU + f"Что вы желаете сделать:{DBR}\n\t0.Открыть файл\n\t1.Добавить сотрудника{DB2}"
                            "\n\t2.Удалить сотрудника\n\t3.Изменить данные сотрудника(ФИО,"
                            " возраст, телефон, должность, e-mail и др.)\n\t4.Вывести краткий список всех сотрудников"
                            "\n\t5.Найти сотрудников с указанным возрастом"
                            "\n\t6.Найти сотрудников и вывести дополнительные данные"
                            f"{DB3}\n\t7.Сохранить результаты поиска в отдельный файл{DB2}"
                            "\n\t8.Сохранить файл с данными" f"\n\t{DBR}Q.Выйти с сохранением\n\t>>> " + RST)
        if selct == "0":
            print("Файлы доступные для открытия: ")
            print(*glob.glob("*.pkl"), sep=", ")
            file_name = re.sub(r"[/\\:*?<>|]", "_", input("Введите имя файла для открытия: "))
            file_name = file_name if file_name[-4:] == ".pkl" else file_name + ".pkl"
            try:
                with open(file_name, 'rb') as mydb:
                    employees: dict = pickle.load(mydb)
            except FileNotFoundError:
                print("Файл с базой данных отсутствует. Будет создан новый файл.")
                if file_name == ".pkl":
                    file_name = datetime.today().strftime("_%Y%m%d%H%M%S.pkl")
                print(f"Новый файл создан с именем: {file_name}")
                save_file(file_name, employees)
                employees = {}
            print(f"\t Количество сотрудников в базе: {len(employees)}")
            found = {}
        elif selct == "Q":
            print("Good buy!")
            if file_name:
                save_file(file_name, employees)
            break
        elif selct == "1":
            pers_id = uuid.uuid4().hex
            employees.setdefault(pers_id, {"name": "", "birth_day": "", "phone": "", "email": "@firm.com",
                                           "job_title": "", "cabinet": "", "skype": ""})
            input_data(pers_id, "name", "ФИО")
            input_data(pers_id, "birth_day", "дату рождения в формате ДД-ММ-ГГГГ:")
        elif len(employees) < 1:
            print("\t\tДля пустой базы доступны только пункты меню 0,1 и Q.")
            pass
        elif selct == "2":
            unit = input("Удаление сотрудника:\n\tВведите ID сотрудника: ")
            if check_unit(unit):
                employees.pop(unit)
                print(f"\tсотрудник с ID:{unit} был удален")
        elif selct == "3":
            print("\t\tИзменить/добавить данные сотрудника: ")
            unit = input('\t\tВведите ID сотрудника, для которого необходимо изменить данные: ')
            if check_unit(unit):
                print_unit_data([unit])
                while True:
                    sel = input("\tКакие данные вы бы хотели изменить:"
                                "\n\t\t0.Выйти\n\t\t1.ФИО\n\t\t2.Дата рождения\n\t\t3.Телефон\n\t\t4.email"
                                "\n\t\t5.Должность\n\t\t6.Кабинет\n\t\t7.skype\n\t\t>>> ")
                    if sel == "0":
                        break
                    elif sel == "" or len(sel) > 1:
                        pass
                    elif sel in "1234567":
                        field = ["name", "birth_day", "phone", "email", "job_title", "cabinet", "skype"][
                            int(sel) - 1]
                        print(f"\t\tСтарое значение параметра {field}: {frmt_field(unit, field)}")
                        input_data(unit, field, f"новое значение для параметра {field}")
        elif selct == "4":
            print_unit_data(employees, as_table=True)
        elif selct == "5":
            ages_set = sorted(
                set(map(calculate_age, [employees[elm]["birth_day"] for elm in employees])))
            select_age = input(
                f"Выберете возраст сотрудников. Условие отбора можно задать числом, списком значений разделенных"
                f" запятой, или с помощью знаков <>\nДоступные значения [полных лет]\n{ages_set}: ")
            found = condition_list(select_age)
            if found:
                print_unit_data(found, as_table=True)
            else:
                print("Сотрудников такого возраста в базе нет.")
        elif selct == "6":
            unit = input("\tВведите начальные символы фамилии чтобы найти сотрудника и вывести данные о нем"
                         "\n\tEnter - вывод всех сотрудников: ")
            found = select_by_value(unit)
            if found:
                print_unit_data(found)
        elif selct == "7":
            if found:
                new_file_name = datetime.today().strftime("%Y%m%d%H%M%S_") + file_name
                print(f"Результаты поиска были сохранены в файл {new_file_name}")
                save_file(new_file_name, found)
            else:
                print("Результаты поиска не содержат данные, сохранение не выполнено.")
        elif selct == "8":
            if file_name:
                save_file(file_name, employees)


firm2()
