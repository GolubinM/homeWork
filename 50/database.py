import sqlite3
from time import time


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_objects(self, table):
        try:
            self.__cur.execute(f'SELECT * from {table}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError as ex:
            print('Ошибка чтения данных', ex)
        return []

    def get_menu(self):
        return self.get_objects('menu')

    def get_projects(self):
        return self.get_objects('projects')

    def add_projects(self, title, text, url):
        try:
            self.__cur.execute(f'SELECT COUNT() as "count" FROM projects WHERE url =="{url}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Проект с таким именем уже существует!')
                return False
            tm = time()
            self.__cur.execute('INSERT INTO projects VALUES(NULL, ?,?,?,?)', (title, text, url, tm)), 401
            self.__db.commit()
        except sqlite3.Error as ex:
            print('Ошибка добавление описания проекта в базу данных', ex)
            return False
        return True

    def add_menu_item(self, title, url):
        try:
            self.__cur.execute(f'SELECT COUNT() as "count" FROM menu WHERE url =="{url}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Такой пункт меню уже существует!')
                return False
            self.__cur.execute('INSERT INTO menu VALUES(NULL, ?,?)', (title, url)), 401
            self.__db.commit()
        except sqlite3.Error as ex:
            print('Ошибка добавление пункта меню в базу данных', ex)
            return False
        return True

    def get_project(self, project_id):
        try:
            self.__cur.execute(f'SELECT project, text FROM projects WHERE url == "{project_id}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as ex:
            print('Ошибка получения проекта из БД', ex)
        return None, None
