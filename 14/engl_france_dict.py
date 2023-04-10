# Задание 2
# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность
# добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

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

    def check_elm(elm, prn: bool = True):
        """Проверка наличия ключа в справочнике, возвращает True или False, опционально выводит сообщение
         о результате проверки"""
        if elm in eng_france_dict:
            return True
        else:
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
