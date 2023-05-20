class View:
    @staticmethod
    def print_tab(header: list, tab):
        count_recs = len(tab)
        if count_recs:
            width_tab = 80
            print('-' * width_tab)
            for num, obj in enumerate(tab):
                print(f"{num + 1})")
                [print(f"{header[n]}:\t{elm}") for n, elm in enumerate(obj.__dict__.values())]
        return count_recs

    @staticmethod
    def wait_user_answer():
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

    @staticmethod
    def get_target():
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
                                       "0 - выход: "))
                if number_rec in control_range:
                    break
            except ValueError:
                pass
        return number_rec

    @staticmethod
    def input_str(invite_string):
        return input(invite_string)
