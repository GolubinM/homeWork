from sqlalchemy import and_, func, select, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pprint import pprint

from salesmen import Salesmen
from sales import Sales
from customers import Customers

DATABASE_NAME = 'sales.db'
LAST_REPORT_FILE_NAME = 'last_report.txt'
LAST_REPORT_CONTENT = [""]
ECHO = False
engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=ECHO)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Создайте трёхтабличную базу данных Sales (продажи).
# В этой базе данных должны быть следующие таблицы
# Sales (информация о конкретных продажах), Salesmen
# (информация о продавцах), Customers (информация о
# покупателях)

# МЕНЮ
# ■ Отображение всех сделок;
# ■ Отображение сделок конкретного продавца;
# ■ Отображение максимальной по сумме сделки;
# ■ Отображение минимальной по сумме сделки;
# ■ Отображение максимальной по сумме сделки для конкретного продавца;
# ■ Отображение минимальной по сумме сделки для конкретного продавца;
# ■ Отображение максимальной по сумме сделки для конкретного покупателя;
# ■ Отображение минимальной по сумме сделки для конкретного покупателя;
# ■ Отображение продавца, у которого максимальная сумма продаж по всем сделкам;
# ■ Отображение продавца, у которого минимальная сумма продаж по всем сделкам;
# ■ Отображение покупателя, у которого максимальная сумма покупок по всем сделкам;
# ■ Отображение покупателя, у которого минимальная сумма покупок по всем сделкам;
# ■ Отображение средней суммы покупки для конкретного покупателя;
# ■ Отображение средней суммы покупки для конкретного продавца.

# план
# создаем соединение с БД
# выводим меню
# Меню содержит следующие основные пункты:
# Отчеты
# -перечень всех отчетов по заданию (после вывода отчета предоставить возможность сохранить результат
# в CSV, имя файла - 'timestamp_имя_отчета.csv')
# реализация отчетов методами SQLAlchemy

#
# Работа с данными
# -Добавление данных
# -Изменение данных
# -Удаление данных
#
#
session = Session()


def home_task_47():
    def select_model():
        print("1. Sales\n2. Salesmen\n3. Customers")
        sel = input("Выберете таблицу, 0 - отмена: ")
        while True:
            if sel == "1":
                return Sales
            elif sel == "2":
                return Salesmen
            elif sel == "2":
                return Customers
            elif sel == "0":
                return False

    def save_last_report():
        with open(LAST_REPORT_FILE_NAME, 'a', encoding="utf-8") as f:
            f.writelines(LAST_REPORT_CONTENT[0])
        LAST_REPORT_CONTENT[0] = ""

    def get_id_record(model):
        while True:
            selected_id = input("Введите Id записи, для совершения операции(i - показать доступные Id): ")
            if selected_id == 'i':
                pprint(session.query(model.id, model).all())
            else:
                break
        return selected_id

    def print_result(query, is_stmt=True):
        if is_stmt:
            result = session.execute(query)
        else:
            result = query
        if result:
            report_content = ''
            for row in result:
                print(row)
                report_content += row.__repr__() + "\n"
            LAST_REPORT_CONTENT[0] = report_content
        else:
            print("По заданному условию записей не найдено.")
        return result

    def all_deals():
        stmt = select(Sales, Salesmen, Customers).filter(and_(Salesmen.id == Sales.salesman_id,
                                                              Customers.id == Sales.customer_id))
        print_result(stmt)

    def max_summ_deals():
        max_summ = session.query(func.max(Sales.summ)).scalar()
        stmt = select(Sales, Salesmen, Customers).filter(and_(Salesmen.id == Sales.salesman_id,
                                                              Customers.id == Sales.customer_id,
                                                              Sales.summ == max_summ))
        print_result(stmt)

    def min_summ_deals():
        min_summ = session.query(func.min(Sales.summ)).scalar()
        stmt = select(Sales, Salesmen, Customers).where(and_(Salesmen.id == Sales.salesman_id,
                                                             Customers.id == Sales.customer_id,
                                                             Sales.summ == min_summ))
        print_result(stmt)

    def sales_by_salesman(selected_id=None):
        if selected_id is None:
            selected_id = get_id_record(Salesmen)
        stmt = select(Sales, Salesmen, Customers).filter(and_(Salesmen.id == Sales.salesman_id,
                                                              Customers.id == Sales.customer_id,
                                                              Salesmen.id == selected_id))
        result = print_result(stmt)
        return result

    def sales_by_customer(selected_id=None):
        if selected_id is None:
            selected_id = get_id_record(Customers)
        stmt = select(Sales, Salesmen, Customers).filter(and_(Salesmen.id == Sales.salesman_id,
                                                              Customers.id == Sales.customer_id,
                                                              Customers.id == selected_id))
        result = print_result(stmt)
        return result

    def max_sale_by_salesman():
        selected_id = get_id_record(Salesmen)
        stmt = select(Salesmen.id, Salesmen, func.max(Sales.summ)).join(Salesmen).group_by(Salesmen.id).filter(
            Salesmen.id == selected_id)
        print_result(stmt)

    def min_sale_by_salesman():
        selected_id = get_id_record(Salesmen)
        stmt = select(Salesmen.id, Salesmen, func.min(Sales.summ)).join(Salesmen).group_by(Salesmen.id).filter(
            Salesmen.id == selected_id)
        print_result(stmt)

    def max_sale_by_customers():
        selected_id = get_id_record(Customers)
        stmt = select(Customers.id, Customers, func.max(Sales.summ)).join(Customers).group_by(
            Customers.id).filter(Customers.id == selected_id)
        print_result(stmt)

    def min_sale_by_customers():
        selected_id = get_id_record(Customers)
        stmt = select(Customers.id, Customers, func.min(Sales.summ)).join(Customers).group_by(
            Customers.id).filter(Customers.id == selected_id)
        print_result(stmt)

    def salesman_with_max_sales():
        # -------ВАРИАНТ 1----- с вложенным запросом
        comb_sales = select(func.sum(Sales.summ).label('total'), Sales.salesman_id.label("id_sm")).group_by(
            Sales.salesman_id).alias("total_sales_q")
        res = session.query(func.max(comb_sales.c.total.label('max_sum_total')), Salesmen).join(Salesmen).where(
            Salesmen.id == comb_sales.c.id_sm).all()
        print_result(res, is_stmt=False)
        # -------ВАРИАНТ 2--не учитывает варианты, когда несколько записей с максимальными равными продажами
        # first_max = session.query(func.sum(Sales.summ).label("sum_total"), Salesmen).join(Salesmen).group_by(
        #     Salesmen.id).order_by(desc("sum_total")).first()
        # print(first_max)

    def salesman_with_min_sales():
        # -------ВАРИАНТ 1-----с вложенным запросом
        comb_sales = select(func.sum(Sales.summ).label('total'), Sales.salesman_id.label("id_sm")).group_by(
            Sales.salesman_id).alias("total_sales_q")
        res = session.query(func.min(comb_sales.c.total.label('min_sum_total')), Salesmen).join(Salesmen).where(
            Salesmen.id == comb_sales.c.id_sm).all()
        print_result(res, is_stmt=False)
        # -------ВАРИАНТ 2--не учитывает варианты, когда несколько записей с минимальными равными продажами
        # first_min = session.query(func.sum(Sales.summ).label("sum_total"), Salesmen).join(Salesmen).group_by(
        #     Salesmen.id).order_by("sum_total").first()
        # print(first_max)

    def customer_with_max_sales():
        comb_sales = select(func.sum(Sales.summ).label('total'), Sales.customer_id.label("id_cs")).group_by(
            Sales.customer_id).alias("total_sales_q")
        res = session.query(func.max(comb_sales.c.total.label('max_sum_total')), Customers).join(Customers).where(
            Customers.id == comb_sales.c.id_cs).all()
        print_result(res, is_stmt=False)

    def customer_with_min_sales():
        comb_sales = select(func.sum(Sales.summ).label('total'), Sales.customer_id.label("id_cs")).group_by(
            Sales.customer_id).alias("total_sales_q")
        res = session.query(func.min(comb_sales.c.total.label('min_sum_total')), Customers).join(Customers).where(
            Customers.id == comb_sales.c.id_cs).all()
        print_result(res, is_stmt=False)

    def avg_sale_by_customer():
        selected_id = get_id_record(Customers)
        stmt = select(Customers.id, Customers, func.round(func.avg(Sales.summ), 2)).join(Customers).group_by(
            Customers.id).filter(Customers.id == selected_id)
        print_result(stmt)

    def avg_sale_by_salesman():
        selected_id = get_id_record(Salesmen)
        stmt = select(Salesmen.id, Salesmen, func.round(func.avg(Sales.summ), 2)).join(Salesmen).group_by(
            Salesmen.id).filter(Salesmen.id == selected_id)
        print_result(stmt)

    def insert_records_salesmen_customers(model):
        rec = model(firstname=input("Введите имя: "), lastname=input("Введите фамилию: "))
        session.add(rec)
        session.commit()

    def insert_records_sales():
        rec = Sales(date=input("Введите дату(yyyy-mm-dd): "), summ=input("Введите сумму: "),
                    salesman_id=input("Введите Id продавца: "), customer_id=input("Введите Id клиента: "))
        session.add(rec)
        session.commit()

    def delete_record(model):
        rec_id = get_id_record(model)
        selected_rec = session.get(model, rec_id)
        try:
            delete_rec = True
            if model == Customers and sales_by_customer(selected_id=rec_id):
                print(f"{selected_rec} имеет дочерние записи!!!")
                if input("Все дочерние записи будут удалены! Нажмите 1 для подтверждения: ") != "1":
                    delete_rec = False
            elif model == Salesmen and sales_by_salesman(selected_id=rec_id):
                print(f"{selected_rec} имеет дочерние записи!!!")
                if input("Все дочерние записи будут удалены! Нажмите 1 для подтверждения: ") != "1":
                    delete_rec = False
            if delete_rec:
                session.delete(selected_rec)
                session.commit()
                print(f"Запись {selected_rec} успешно удалена.")
                return True
            else:
                print("Удаление не было произведено.")
                return False
        except Exception as ex:
            print("Удаление не было произведено.", ex)
            return False

    def get_table_fields_names(model):
        fields = [field for field in model.__dict__ if field[0] != "_" and field != "id"]
        return fields

    def update_records(model):
        id_rec = get_id_record(model)
        record = session.get(model, id_rec)
        try:
            fields = get_table_fields_names(model)
            print(record._get_info())
            for en, field in enumerate(fields, 1):
                print(en, field)
            selected_field = int(input("Выберете номер поля для редактирования: ")) - 1
            field_name = fields[selected_field]
            new_value = input(f"Введите новое значение для поля {field_name}: ")
            update_query = {"id": id_rec, field_name: new_value}
            session.execute(update(model), [update_query])
            session.commit()
            print("Запись обновлена.")
            return True
        except Exception as ex:
            print("Изменение записи не произведено.", ex)
            return False

    menu_reports = "1  ■ Отображение всех сделок;\n" \
                   "2  ■ Отображение сделок конкретного продавца;\n" \
                   "3  ■ Отображение максимальной по сумме сделки;\n" \
                   "4  ■ Отображение минимальной по сумме сделки;\n" \
                   "5  ■ Отображение максимальной по сумме сделки для конкретного продавца;\n" \
                   "6  ■ Отображение минимальной по сумме сделки для конкретного продавца;\n" \
                   "7  ■ Отображение максимальной по сумме сделки для конкретного покупателя;\n" \
                   "8  ■ Отображение минимальной по сумме сделки для конкретного покупателя;\n" \
                   "9  ■ Отображение продавца, у которого максимальная сумма продаж по всем сделкам;\n" \
                   "10 ■ Отображение продавца, у которого минимальная сумма продаж по всем сделкам;\n" \
                   "11 ■ Отображение покупателя, у которого максимальная сумма покупок по всем сделкам;\n" \
                   "12 ■ Отображение покупателя, у которого минимальная сумма покупок по всем сделкам;\n" \
                   "13 ■ Отображение средней суммы покупки для конкретного покупателя;\n" \
                   "14 ■ Отображение средней суммы покупки для конкретного продавца." \
                   "0  ■ Вернуться в основное меню;\n"
    menu_changes = "1  ■ Добавление записи;\n" \
                   "2  ■ Обновление записи;\n" \
                   "3  ■ Удаление записи;\n" \
                   "0  ■ Вернуться в основное меню;\n"
    menu_main = "1  ■ Отчеты;\n" \
                "2  ■ Действия с данными(добавить,удалить, обновить);\n" \
                "3  ■ Сохранить последний отчет в файл;\n" \
                "q  ■ Выход из программы;\n"

    invite = "Выберете номер действия, q - выход из программы:"

    def reports(menu=menu_reports):
        sel = ""
        while sel != "0":
            print(menu)
            sel = input(invite)
            if sel == "1":
                all_deals()
            elif sel == "2":
                sales_by_salesman()
            elif sel == "3":
                max_summ_deals()
            elif sel == "4":
                min_summ_deals()
            elif sel == "5":
                max_sale_by_salesman()
            elif sel == "6":
                min_sale_by_salesman()
            elif sel == "7":
                max_sale_by_customers()
            elif sel == "8":
                min_sale_by_customers()
            elif sel == "9":
                salesman_with_max_sales()
            elif sel == "10":
                salesman_with_min_sales()
            elif sel == "11":
                customer_with_max_sales()
            elif sel == "12":
                customer_with_min_sales()
            elif sel == "13":
                avg_sale_by_customer()
            elif sel == "14":
                avg_sale_by_salesman()

    def db_changes(menu=menu_changes):
        sel = ""
        while sel != "0":
            print(menu)
            sel = input(invite)
            model = select_model()
            if model:
                if sel == "1":
                    if model == Sales:
                        insert_records_sales()
                    else:
                        insert_records_salesmen_customers(model)
                elif sel == "2":
                    update_records(model)
                elif sel == "3":
                    delete_record(model)

    sel = ""
    while sel != "q":
        print("БАЗА ДАННЫХ SALES.")
        print(menu_main)
        sel = input(invite)
        if sel == "1":
            reports()
        elif sel == "2":
            db_changes()
        elif sel == "3":
            save_last_report()


if __name__ == "__main__":
    pass
    # all_deals()
    # sales_by_salesman()
    # max_summ_deals()
    # min_summ_deals()
    # max_sale_by_salesman()
    # min_sale_by_salesman()
    # max_sale_by_customers()
    # min_sale_by_customers()
    # salesman_with_max_sales()
    # salesman_with_min_sales()
    # customer_with_max_sales()
    # customer_with_min_sales()
    # avg_sale_by_customer()
    # avg_sale_by_salesman()
    # save_last_report()
    # insert_records()
    # delete_record(Sales)
    # update_records(Sales)
    # update_records(Salesmen)
    # update_records(Customers)
    # print(get_table_fields_names(Sales))
    home_task_47()
