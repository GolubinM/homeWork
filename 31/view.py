class View:
    def print_tab(self, header, tab):
        """ выводит таблицу на дисплей, возвращает к-во эл-в таблицы"""
        count_recs = len(tab)
        if count_recs:
            # print([[val for key, val in elm.__dict__.items()] for elm in tab])
            width_field = max([max([len(str(val)) for val in elm.__dict__.values()]) for elm in tab]) + 4
            width_tab = (width_field + 2) * len(tab[0].__dict__.items()) + 3
            print('-' * width_tab)
            str_pr = [f"{elm: <{width_field}}" for elm in header]
            print("№  ", sep="", end="| ")
            print(*str_pr, sep="| ")
            print('-' * width_tab)
            for num, obj in enumerate(tab):
                str_pr = [f"{elm: <{width_field}}" for elm in obj.__dict__.values()]
                print(f"{num + 1: <3}", sep="", end="| ")
                print(*str_pr, sep="| ")
        return count_recs

    def wait_user_answer(self):
        print("Ожидание пользовательского ввода: ".center(100, '='))
        print("Доступные действия:\n"
              "1. Отобразить список элементов\n"
              "2. Найти элемент\n"
              "3. Добавить элемент\n"
              "4. Удалить элемент\n"
              "5. Изменить элемент\n"
              "Q. Завершить")
        print("=" * 100)
        query = input("Введите номер действия: ")
        return query

    def get_target(self):
        word = input("Введите ключевое слово для поиска элемента\n"
                     "Enter - выход из поиска: ")
        return word

    @staticmethod
    def message_out(message: str):
        print(message.center(100, "-"))

    def get_num_records(self, header, tab):
        self.print_tab(header, tab)
        control_range = range(len(tab) + 1)
        while True:
            try:
                number_rec = int(input("Выберете номер записи\n"
                                       "0 - выход без удаления: "))
                if number_rec in control_range:
                    break
            except ValueError:
                pass
        return number_rec

    @staticmethod
    def input_str(invite_string):
        return input(invite_string)

    @staticmethod
    def input_value(invite_string):
        while True:
            try:
                num = int(input(invite_string))
                break
            except ValueError:
                print("Ошибка ввода. Введите числовое значение.")
        return num
