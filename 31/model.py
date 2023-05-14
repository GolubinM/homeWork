from openpyxl import load_workbook


class Shoes:
    def __init__(self, producer, type, kind, color, size, price):
        self.producer = producer
        self.type = type
        self.kind = kind
        self.color = color
        self.size = size
        self.price = price

    def __str__(self):
        return ",".join([f"{key}:{str(value)}" for key, value in self.__dict__.items()])


class ShoesNotFoundError(Exception):
    pass


class Model:
    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname
        self.wb = load_workbook(filename)
        self.ws = self.wb[sheetname]
        ws_values = list(self.ws.values)
        self.header = ws_values[0]
        self.database = ws_values[1:]

    def shoes_from_row(self, row_number):
        return Shoes(*self.database[row_number])

    @staticmethod
    def get_one_record_by(database, word):
        data = []
        for rec in database:
            if word in "".join(str(rec)):
                data.append(rec)
        return data

    def save_db_to_xlsx(self, filename):
        self.wb.save(filename)
        self.__init__(self.filename, self.sheetname)

    def delete_rec(self, num_rec):
        self.ws.delete_rows(num_rec + 1, 1)
        self.save_db_to_xlsx(self.filename)

    def change_rec(self, num_rec, new_row_data):
        for col, elm in enumerate(self.header):
            self.ws.cell(row=num_rec, column=col + 1).value = new_row_data[col]
        self.save_db_to_xlsx(self.filename)

    def add_rec(self):
        pass
