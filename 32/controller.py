from model import Model
from view import View


class Controller:
    def __init__(self, filename, sheet_name):
        self.view = View()
        self.model = Model(filename, sheet_name)

    def run(self):
        query = None
        while query != 'Q':
            query = self.view.wait_user_answer()
            self.eval_user_answer(query)
        print("Good buy!")

    def create_recipe_obj(self, num_str):
        return self.model.__obj_from_row__(num_str)

    def eval_user_answer(self, query):
        if query == "1":
            self.view.print_tab(self.model.header, self.model.database)
        elif query == "2":
            database = self.model.database
            while True:
                target = self.view.get_target()
                if target == "":
                    break
                data = self.model.get_one_record_by(database, target)
                count_recs = len(data)
                if count_recs == 1:
                    self.view.print_tab(self.model.header, data)
                    break
                elif count_recs > 1:
                    self.view.message_out("Найдено более одной записи! Уточните поиск")
                    self.view.print_tab(self.model.header, data)
                    database = data
                else:
                    self.view.message_out("Запись с такими параметрами не найдена!")
                    break
        elif query == "3":
            num_rec = len(self.model.database) + 1
            new_row = []
            for elm in self.model.header:
                invite_str = f"Введите значение для параметра {elm}: "
                new_row.append(self.view.input_str(invite_str))
            self.model.add_new_obj(num_rec + 1, new_row)

        elif query == "4":
            num_rec = self.view.get_num_records(self.model.header, self.model.database)
            if num_rec:
                self.model.delete_rec(num_rec)
                self.view.message_out(f"Элемент в строке {num_rec} удален!")
            else:
                self.view.message_out("Удаление не выполнено!")
        elif query == "5":
            num_rec = self.view.get_num_records(self.model.header, self.model.database)
            if num_rec:
                new_row = []
                for num, elm in enumerate(self.model.header):
                    invite_str = f"Введите новое значение для параметра {elm}\nEnter - оставить значение поля прежним: "
                    new_value = self.view.input_str(invite_str)
                    if new_value != "":
                        new_row.append(new_value)
                    else:
                        new_row.append(list(self.model.database[num_rec - 1].__dict__.values())[num])
                self.model.change_rec_obj(num_rec, new_row)
            else:
                self.view.message_out("Изменение не выполнено!")
