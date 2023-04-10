# Задание 1
# Создайте программу, хранящую информацию о вели-
# ких баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.
print("Задание 1. " + "=" * 55)


def basketball_glory_hall():
    MENU_CLR = '\u001b[38;5;' + '106' + 'm'
    DATA_CLR = '\u001b[38;5;' + '176' + 'm'
    DATA_BR_CLR = '\u001b[38;5;' + '178' + 'm'
    RESET_COLOR = '\033[0m'
    players: dict = {"Ленни Уилкенс": {"height": 185, "games": 1077, "country": "USA"},
                     "Бернард Кинг": {"height": 201, "games": 874, "country": "USA"},
                     "Гарри Галлатин": {"height": 198, "games": 682, "country": "USA"},
                     "Элвин Эрнест Хейз": {"height": 206, "games": 1303, "country": "USA"}, }

    def check_player(player):
        """Проверка наличия ключа в справочнике, возвращает True или False, опционально выводит сообщение
         о результате проверки"""
        if player in players:
            return True
        print("Игрока с таким именем нет в базе данных.")
        return False

    def print_player_data(player_prn):
        print(DATA_CLR + player_prn + RESET_COLOR)
        if not players.get(player_prn, False):
            return
        for data in players[player_prn]:
            print(DATA_CLR + f"{data:>10}:" + DATA_BR_CLR, players[player_prn][data], RESET_COLOR)

    def print_players(prn_data: bool = False):
        if prn_data:
            for player_prn in players:
                print_player_data(player_prn)
        else:
            print(DATA_CLR + ", ".join(players.keys()) + RESET_COLOR)

    def basketball_players(sel, player=None):
        if sel == "1":
            player = input("Добавление игрока:\n\tВведите ФИО игрока: ")
            players.setdefault(player, {"height": ""})  # значение по умолчанию для корректной обработки словаря (п.5)
            basketball_players("5", player)  # рекурсивно заполняем данные для нового игрока
            print_players()
        elif sel == "2":
            player = input("Удаление игрока:\n\tВведите ФИО игрока: ")
            if check_player(player):
                players.pop(player)  # не использую встроенные возможности проверки, для сокращ. кода, вывода ошиб сообщ
            print_players()
        elif sel == "3":
            player = input("\tВведите ФИО чтобы найти игрока и вывести данные о нем: ")
            if check_player(player):
                print_player_data(player)
        elif sel == "4":
            player = input("\tВведите ФИО игрока у которого вы хотите отредактировать ФИО: ")
            if check_player(player):
                new_key = input("\tВведите новые ФИО: ")
                replace_old = True
                if check_player(new_key):
                    print("Новые ФИО уже присутствует в базе! Если продолжить, "
                          f"все данные связанные с {DATA_BR_CLR}{new_key}{RESET_COLOR}\n"
                          f"будут заменены данными {DATA_CLR}{player}{RESET_COLOR}!!!")
                    replace_old = input("Продолжить - Enter. Отменить - 0: ")
                if new_key != "" and replace_old != "0":
                    players[new_key] = players.pop(player)
                    print_players()
                else:
                    print("\t\tИмя не было отредактировано.")
        elif sel == "5":
            if not player:  # Если пункт 5 вызывается непосредственно из меню (а не рекурсивно из п.1)
                print("\t\tИзменить/добавить данные игрока(рост, кол-во игр, страна, другое..): ")
                player = input('\t\tВведите ФИО игрока, для которого необходимо изменить данные: ')
            if check_player(player):
                print_player_data(player)
                print("\t\tКакие данные вы бы хотели изменить или добавить: ", end="")
                data_to_update = input()
                if data_to_update != "":
                    if data_to_update not in players[player]:
                        print(f"\t\tДля игрока {player} будет добавлен новый параметр: {data_to_update}")
                    else:
                        print(f"\t\tДля игрока {player} будут изменены данные в параметре: {data_to_update}")
                    players[player][data_to_update] = input(f"\t\tВведите значение для параметра {data_to_update}: ")
                    print_player_data(player)
        elif sel == "6":
            print_players(True)

    print("Баскетболисты \"Зала славы\":", end="\n\t")
    print_players(False)
    while True:
        sel = input(MENU_CLR +
                    "Что вы желаете сделать:"
                    "\n\t0.Выйти"
                    "\n\t1.Добавить игрока"
                    "\n\t2.Удалить игрока"
                    "\n\t3.Найти игрока и вывести данные"
                    "\n\t4.Откорректировать ФИО игрока"
                    "\n\t5.Изменить/добавить данные игрока(информацию о росте, кол-ве игр, страну и др.)"
                    "\n\t6.Вывести список всех игроков и данные по ним: " + RESET_COLOR)
        if sel == "0":
            print("Good buy!")
            break
        else:
            basketball_players(sel)


basketball_glory_hall()

# ================================================================================================================
# Задание 2
# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность
# добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.
print("Задание 2. " + "=" * 55)


def engl_france_dictionary():
    MENU_CLR = '\u001b[38;5;' + '106' + 'm'
    DATA_CLR = '\u001b[38;5;' + '176' + 'm'
    DATA_BR_CLR = '\u001b[38;5;' + '178' + 'm'
    RESET_COLOR = '\033[0m'
    eng_france_dict = {"apple": "la pome",
                       "world": "le monde, l' univers, le globe",
                       "peace": "la paix, la tranquillité, le calme",
                       "snow": "la neige, las blanche",
                       "school": "l' école, le collège"}

    def check_elm(elm):
        """Проверка наличия ключа в справочнике, возвращает True или False, опционально выводит сообщение
         о результате проверки"""
        if elm in eng_france_dict:
            return True
        print("Такого слова нет в словаре.")
        return False

    def print_words(elm_prn=None):
        if elm_prn is None:
            for word in sorted(eng_france_dict):
                print(DATA_CLR + word, DATA_BR_CLR + eng_france_dict[word], sep=":\t")
        elif check_elm(elm_prn):
            print(DATA_CLR + elm_prn + ":\t", DATA_BR_CLR + eng_france_dict[elm_prn])
        print(RESET_COLOR)

    def operations(sel):
        if sel == "1":
            eng_word = input("Добавление слова и перевода:\n\tВведите английское слово : ")
            fr_word = input("Одной строкой, через запятую, введите возможные переводы слова на французский язык: ")
            eng_france_dict.setdefault(eng_word, fr_word)
            print_words(eng_word)
        elif sel == "2":
            eng_word = input("Удаление слова:\n\tВведите английское слово для удаления из словаря: ")
            if check_elm(eng_word):
                eng_france_dict.pop(eng_word)
                print(f"Слово {DATA_CLR}{eng_word}{RESET_COLOR} удалено из словаря")
        elif sel == "3":
            eng_word = input("\tВведите английское слово для поиска и вывода перевода: ")
            if check_elm(eng_word):
                print_words(eng_word)
        elif sel == "4":
            eng_word = input("\tВведите английское слово, которое необходимо изменить: ")
            if check_elm(eng_word):
                new_key = input("\tВведите измененное слово: ")
                replace_old = True
                if check_elm(new_key):
                    print("Измененное слово уже присутствует в словаре, старое значение будет удалено!!!")
                    replace_old = input("Продолжить - Enter. Отменить - 0: ")
                if new_key != "" and replace_old != "0":
                    eng_france_dict[new_key] = eng_france_dict.pop(eng_word)
                    print_words(new_key)
                else:
                    print("\t\tСлово не было изменено.")
        elif sel == "5":
            print("\t\tИзменить/добавить перевод слова: ")
            eng_word = input('\t\tВведите английское слово, для которого требуется изменить/добавить перевод: ')
            if check_elm(eng_word):
                print_words(eng_word)
                fr_word = input("Одной строкой, через запятую, введите возможные переводы слова на французский язык: ")
                if fr_word != "":
                    eng_france_dict[eng_word] = fr_word
                    print_words(eng_word)
        elif sel == "6":
            print_words()

    print("English - France dictionary")
    while True:
        select_menu = input(MENU_CLR +
                            "Что вы желаете сделать:"
                            "\n\t0.Выйти"
                            "\n\t1.Добавить слово"
                            "\n\t2.Удалить слово"
                            "\n\t3.Найти слово и вывести перевод"
                            "\n\t4.Заменить слово"
                            "\n\t5.Изменить/добавить перевод для слова"
                            "\n\t6.Вывести все слова из словаря с переводом слов >>> " + RESET_COLOR)
        if select_menu == "0":
            print("Good buy!")
            break
        else:
            operations(select_menu)


engl_france_dictionary()

# ==================================================================================================================
# Задание 3
# Создайте программу «Фирма». Нужно хранить ин-
# формацию о человеке: ФИО, phone, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поис-
# ка, замены данных. Используйте словарь для хранения
# информации.
print("Задание 3. " + "=" * 55)


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
        print(DATA_CLR + player_prn + RESET_COLOR)
        if not employees.get(player_prn, False):
            print(RESET_COLOR, end="")
            return
        for data in employees[player_prn]:
            print(DATA_CLR + f"{data:>10}:" + DATA_BR_CLR, employees[player_prn][data], RESET_COLOR)

    def print_unit(prn_data: bool = False):
        if prn_data:
            for player_prn in employees:
                print_unit_data(player_prn)
        else:
            print(DATA_CLR + ", ".join(employees.keys()) + RESET_COLOR)

    def personal(sel, unit=None):
        if sel == "1":
            unit = input("Добавление сотрудника:\n\tВведите ФИО сотрудника: ")
            employees.setdefault(unit, {"phone": ""})
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
            if not unit:  # Если пункт 5 вызывается непосредственно из меню (а не рекурсивно из п.1)
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
