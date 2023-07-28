from main import menu, connect_db
from database import DataBase

# смотрим что имеем
# print(DataBase)
# print(menu)
# print(app.config)

db_con = connect_db()
db = DataBase(db_con)

for elm in menu:
    print(elm)
    res = db.add_menu_item(**elm)
    if not res:
        print('Ошибка добавления проекта!')
