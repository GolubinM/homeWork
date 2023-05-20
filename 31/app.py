import os.path
from controller import Controller


def main():
    try:
        if os.path.exists("shoesDB.xlsx"):
            app = Controller("shoesDB.xlsx", 'Лист1')
            app.run()
        else:
            raise FileExistsError
    except FileExistsError:
        print("Ошибка инициализации БД")
        return


if __name__ == '__main__':
    main()
