import sqlite3 as sq
import os.path


# AUTOINCREMENT - не указываем, если не нужно ограничить использование удаленных индексов

def create_sql_script(script_filename):
    script_content = """CREATE TABLE IF NOT EXISTS contracts (
                        contr_id INTEGER PRIMARY KEY,
                        count_id INTEGER,
                        contr_date text NOT NULL,
                        summ real,
                        subject text NOT NULL,
                        FOREIGN KEY (count_id)  REFERENCES counterparty (count_id)
                        );
                    CREATE TABLE IF NOT EXISTS payments (
                        paym_id INTEGER PRIMARY KEY,
                        contr_id INTEGER,
                        paym_date text NOT NULL,
                        summ real NOT NULL CHECK(summ >=0) DEFAULT 0,
                        rem text NOT NULL,
                        FOREIGN KEY (contr_id)  REFERENCES contracts (contr_id)
                        );"""

    with open(script_filename, "w", encoding="UTF-8") as f:
        f.write(script_content)


def db_create():
    with sq.connect('contracts.db') as con:
        try:
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS counterparty (
                                    count_id INTEGER PRIMARY KEY,
                                    title text NOT NULL,
                                    inn text UNIQUE,
                                    address text,
                                    supervisor text,
                                    phone text);'''
            cursor = con.cursor()
            cursor.execute(sqlite_create_table_query)
            if not os.path.isfile('create_contracts_payments_tables.sql'):
                create_sql_script('create_contracts_payments_tables.sql')
            with open('create_contracts_payments_tables.sql') as sqlite_f:
                sql_script = sqlite_f.read()
                cursor.executescript(sql_script)
            # print("Скрипт SQLite успешно выполнен")
            # cursor.close()
            con.commit()
        except sq.Error as error:
            print("Ошибка при подключении к sqlite", error)


db_create()
import pandas as pd


class DB_Filler:
    def __init__(self, db_filename):
        self.db = db_filename

    def get_rec_from_csv(self, filename, table_name=None, if_exists='fail'):
        df = pd.read_csv(filename, encoding='utf-8', delimiter=';', index_col=0)
        pd.set_option('display.max_colwidth', 30)
        print(df)
        print(df.info())
        if table_name:
            with sq.connect('contracts.db') as con:
                try:
                    df.to_sql(table_name, con, if_exists=if_exists, index=True)
                except Exception as error:
                    print("Ошибка при экспорте sqlite", error)

    # сознание дико сопротивлялось реализовывать ввод данных через input (без форм), сделал с подсказкой имен полей,
    # получаемых с помощью pandas
    def input_rec(self, table_name, data=None):
        """table_name - имя таблицы БД, data - кортеж данных, для заполнения строк таблицы в порядке следования полей
        за исключением поля с ключами"""
        with sq.connect(self.db) as con:
            try:
                # Определяем имена полей
                sql_query = pd.read_sql_query(f'SELECT * FROM {table_name} limit 1', con)
                df = pd.DataFrame(sql_query)
                # print(df.info())
                # если данные полей не переданы параметром, предлагается заполнить вручную
                columns = df.columns.values.tolist()
                if not data:
                    print(f'Введите через запятую значения для полей таблицы [{table_name}]: ')
                    print(columns[1:])
                    fields = input("").split(',')
                    data = tuple(fields)  # формируем кортеж с данными(за исключением key-поля, по срезу columns[1:])
                fields_name = ", ".join(columns[1:])  # поля таблицы без первого key-поля
                # формируем f-строку с командой вставки значений в поля таблицы(за исключением key-поля)
                sql_str = f'INSERT INTO {table_name} ({fields_name}) VALUES {data}'
                cur = con.cursor()
                cur.execute(sql_str)
            except Exception as error:
                print("Ошибка при чтении sqlite", error)

    def get_report_total_payments(self):
        sql_query = '''SELECT sum(summ) FROM payments;'''
        self.get_sql_report(sql_query)

    def get_report_with_req(self, sql_request):
        self.get_sql_report(sql_request)

    def get_sql_report(self, sql_query):
        with sq.connect(self.db) as con:
            try:
                cur = con.cursor()
                cur.execute(sql_query)
                for elm in cur:
                    print(*elm)
            except Exception as error:
                print("Ошибка при выполнении запроса sqlite", error)


db_fill = DB_Filler('contracts.db')
db_fill.get_rec_from_csv('contracts.csv', 'contracts', if_exists='append')
db_fill.get_rec_from_csv('counterparty.csv', 'counterparty', if_exists='append')
db_fill.get_rec_from_csv('payments.csv', 'payments', if_exists='append')
db_fill.input_rec("payments", (20, '2022-05-01', 100500.01, "Аванс по договору б/н от ..."))
db_fill.input_rec("payments", (100, '2022-07-04', 500100.22, "Оплата за работы по договору б/н от ..."))
db_fill.input_rec("payments", (120, '2022-07-04', 1600900.33, "Оплата за работы"))
db_fill.input_rec("payments")
db_fill.input_rec("contracts", (49, "2022-12-08", 10000001, "Текущий ремонт мостового эл. г/п 20/5 пр 10,5 №2094"))
db_fill.input_rec("contracts")
db_fill.get_report_total_payments()
db_fill.get_report_with_req(sql_request="select * from payments where summ<5000")
db_fill.get_report_with_req(sql_request="select * from payments where summ<5000")
sql_requst_2 = """SELECT cpt.title,
       cpt.inn,
       cts.contr_date,
       cts.summ
  FROM contracts cts
       JOIN
       counterparty cpt ON cpt.count_id = cts.count_id
order by summ 
LIMIT 10 offset 20;
"""
sql_requst_3 = """
SELECT cpt.title name,
       cts.contr_date contract_date,
       cts.summ contract_summ,
       sum(pm.summ) total_pyaments
  FROM contracts cts
       JOIN
       counterparty cpt ON cpt.count_id = cts.count_id
       JOIN
       payments pm ON cts.contr_id = pm.contr_id
 WHERE cts.contr_date > date("2022-04-01")
 GROUP BY cpt.count_id
HAVING sum(pm.summ) > 1000000;"""
db_fill.get_report_with_req(sql_requst_3)
