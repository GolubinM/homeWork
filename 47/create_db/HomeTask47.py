import os
from sqlalchemy import and_, or_, not_, desc, func, text, select, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, aliased, relationship
# from database import Session, Base
from pprint import pprint
# engine = create_engine(f'sqlite:///{DATABASE_NAME}')

from salesmen import Salesmen
from sales import Sales
from customers import Customers

DATABASE_NAME = 'sales.db'
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
        for row in result:
            print(row)
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
    sales = select(func.sum(Sales.summ).label('total'), Sales.salesman_id.label("id_sm")).group_by(
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


def insert_records():
    # 1. Добавляем запись с продавцом: таблица salesmen класс Salesmen
    rec = Salesmen(firstname="Кирилл", lastname="Серов")
    session.add(rec)
    print(rec)
    print(session.new)
    some_salesman = session.get(Salesmen, 50)
    print(some_salesman)
    session.commit()


def delete_record(model):
    rec_id = get_id_record(model)
    selected_rec = session.get(model, rec_id)
    if selected_rec:
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
            try:
                session.delete(selected_rec)
                session.commit()
                print(f"Запись {selected_rec} успешно удалена.")
                return True
            except Exception as ex:
                print(f"Ошибка при попытке удаления записи {selected_rec}.", ex)
        else:
            print("Удаление не было произведено.")
    else:
        print("Запись с таким Id не найдена. Удаление не было произведено.")


def get_table_fields_names(model):
    fields = [field for field in model.__dict__ if field[0] != "_" and field != "id"]
    return fields


def update_records(model):
    id_rec = get_id_record(model)
    record = session.get(model, id_rec)
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


if __name__ == "__main__":
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
    # insert_records()
    # delete_record(Sales)
    # update_records(Sales)
    # update_records(Salesmen)
    update_records(Customers)
    # print(get_table_fields_names(Sales))

