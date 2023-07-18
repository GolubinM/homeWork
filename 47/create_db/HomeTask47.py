import os
from sqlalchemy import and_, or_, not_, desc, func, text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from database import Session, Base
from pprint import pprint
# engine = create_engine(f'sqlite:///{DATABASE_NAME}')

from salesmen import Salesmen
from sales import Sales
from customers import Customers

DATABASE_NAME = 'sales.db'
ECHO = True
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


# print(session.query(Salesmen).all())
# for sman in session.query(Salesmen).all():
#     print(sman.firstname, sman.lastname)


def print_result(result):
    if result:
        pprint(result)
    else:
        print("По заданному условию записей не найдено.")


# функции вывода отчетов
def all_deals(session):
    result = session.query(Sales, Salesmen, Customers).filter(and_(Salesmen.id == Sales.salesman_id,
                                                                   Customers.id == Sales.customer_id)).all()
    print_result(result)
    return result


def max_summ_deals(session):
    max_summ = session.query(func.max(Sales.summ)).first()[0]
    result = session.query(Sales, Salesmen, Customers).filter(and_(Salesmen.id == Sales.salesman_id,
                                                                   Customers.id == Sales.customer_id,
                                                                   Sales.summ == max_summ)).all()
    print_result(result)
    return result


def min_summ_deals(session):
    min_summ = session.query(func.min(Sales.summ)).first()[0]
    result = session.query(Sales, Salesmen, Customers).filter(and_(Salesmen.id == Sales.salesman_id,
                                                                   Customers.id == Sales.customer_id,
                                                                   Sales.summ == min_summ)).all()
    print_result(result)
    return result


def sale_by_salesman(session):
    pprint(session.query(Salesmen.id, Salesmen).all())
    selected_id = input("Введите Id продавца, по которому будет сформирован отчет о продажах: ")
    try:
        result = session.query(Sales, Salesmen, Customers).filter(and_(Salesmen.id == Sales.salesman_id,
                                                                       Customers.id == Sales.customer_id,
                                                                       Salesmen.id == selected_id)).all()
        print_result(result)
        return result
    except Exception as ex:
        print("Ошибка", ex)
        return False


def max_sale_by_salesman(session):
    pprint(session.query(Salesmen.id, Salesmen).all())
    selected_id = input("Введите Id продавца, по которому будет сформирован отчет о продажах: ")
    try:
        result = session.query(Salesmen.id, Salesmen, func.max(Sales.summ)).join(Salesmen).group_by(Salesmen.id).filter(
            Salesmen.id == selected_id).all()
        print_result(result)
        return result
    except Exception as ex:
        print("Ошибка", ex)
        return False


def min_sale_by_salesman(session):
    pprint(session.query(Salesmen.id, Salesmen).all())
    selected_id = input("Введите Id продавца, по которому будет сформирован отчет о продажах: ")
    try:
        result = session.query(Salesmen.id, Salesmen, func.min(Sales.summ)).join(Salesmen).group_by(Salesmen.id).filter(
            Salesmen.id == selected_id).all()
        print_result(result)
        return result
    except Exception as ex:
        print("Ошибка", ex)
        return False


def max_sale_by_customers(session):
    pprint(session.query(Customers.id, Customers).all())
    selected_id = input("Введите Id клиента, по которому будет сформирован отчет: ")
    try:
        result = session.query(Customers.id, Customers, func.max(Sales.summ)).join(Customers).group_by(
            Customers.id).filter(
            Customers.id == selected_id).all()
        print_result(result)
        return result
    except Exception as ex:
        print("Ошибка", ex)
        return False


def min_sale_by_customers(session):
    pprint(session.query(Customers.id, Customers).all())
    selected_id = input("Введите Id контрагента, по которому будет сформирован отчет: ")
    try:
        result = session.query(Customers.id, Customers, func.min(Sales.summ)).join(Customers).group_by(
            Customers.id).filter(
            Customers.id == selected_id).all()
        print_result(result)
        return result
    except Exception as ex:
        print("Ошибка", ex)
        return False


def salesman_with_max_sales(session):
    try:
        total_sales = session.query(Salesmen.id, Salesmen, func.sum(Sales.summ).label("total_sales")).join(
            Salesmen).group_by(Salesmen.id).all()
        print_result(total_sales)
        # result = session.query(Salesmen.id, Salesmen, func.max(Sales.summ)).join(Salesmen).group_by(Salesmen.id).filter(
        #     Salesmen.id == selected_id).all()
        # print_result(result)
        return total_sales
    except Exception as ex:
        print("Ошибка", ex)
        return False


# def max_sales_for_sman(session):
#     for it in session.query(Salesmen.id, func.max(Sales.summ)).join(Salesmen).group_by(Salesmen.id).filter(
#             Salesmen.id == 2).all():
#         print(it)


# def mx_2(session):
#     for it in session.query(Salesmen.id, func.max(Sales.summ)).join(Salesmen).group_by(Salesmen.id).all():
#         print(it)
#
#
# def min_2(session):
#     for it in session.query(Salesmen.id, func.min(Sales.summ)).join(Salesmen).group_by(Salesmen.id).all():
#         print(it)
#
#
# def all_by_sman_2(session):
#     for it in session.query(Salesmen.id, Sales.summ).join(Salesmen).filter(Salesmen.id == 3).all():
#         print(it)


if __name__ == "__main__":
    # all_deals(session)
    # sale_by_salesman(session)
    # max_summ_deals(session)
    # min_summ_deals(session)
    # max_sale_by_salesman(session)
    # min_sale_by_salesman(session)
    # max_sale_by_customers(session)
    # min_sale_by_customers(session)
    salesman_with_max_sales(session)
