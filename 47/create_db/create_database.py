from faker import Faker

from database import create_db, Session
# импортируем модели
from customers import Customers
from salesmen import Salesmen
from sales import Sales

faker = Faker('ru_RU')

def get_first_last_name():
    if faker.random.randint(0, 3):
        return faker.first_name_male(), faker.last_name_male()
    else:
        return faker.first_name_female(), faker.last_name_female()


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    Faker.seed(0)

    # создаем продавцов
    for _ in range(50):
        full_name = get_first_last_name()
        firstname = full_name[0]
        lastname = full_name[1]
        salesman = Salesmen(firstname=firstname, lastname=lastname)
        session.add(salesman)
    session.commit()
    # создаем клиентов
    for _ in range(70):
        full_name = get_first_last_name()
        firstname = full_name[0]
        lastname = full_name[1]
        customer = Customers(firstname=firstname, lastname=lastname)
        session.add(customer)
    session.commit()
    # создаем продажи
    for _ in range(150):
        salesman_id = faker.random.randint(1, 51)
        customer_id = faker.random.randint(1, 71)
        date = faker.date_between(start_date="-2y40d", end_date="-90d")
        summ = faker.random.randint(500, 12500)
        sales = Sales(salesman_id=salesman_id, customer_id=customer_id, date=date, summ=summ)
        session.add(sales)
    session.commit()

    session.close()
