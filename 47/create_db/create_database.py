from faker import Faker, providers as fp

from database import create_db, Session
# импортируем модели
from customers import Customers
from salesmen import Salesmen
from sales import Sales


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    faker = Faker('ru_RU')
    Faker.seed(0)

    # создаем продавцов
    for _ in range(50):
        salesman_full_name = faker.name().split()
        customer_full_name = faker.name().split()
        salesman = Salesmen(salesman_full_name)
        customer = Customers(customer_full_name)
        session.add(salesman)
        session.add(customer)
    session.commit()

    # создаем продажи
    for _ in range(150):
        salesman_id = faker.random.randint(0, 50)
        customer_id = faker.random.randint(0, 50)
        date = faker.date_between(start_date="-2y40d", end_date="-90d")
        summ = faker.random.randint(500, 2500)
        sales = Sales(salesman_id=salesman_id, customer_id=customer_id, date=date, summ=summ)
        session.add(sales)
    session.commit()

    session.close()
