import pickle
import random
import uuid
from datetime import date, datetime

from faker import Faker

Faker.seed(0)
fake = Faker('ru-Ru')


def rand_date(start_date: str = "1972-01-01", end_date: str = "1998-01-01"):
    start_date = datetime.fromisoformat(start_date)
    end_date = datetime.fromisoformat(end_date)
    rnd_date = start_date + (end_date - start_date) * random.random()
    return rnd_date


def rand_name():
    if random.randint(0, 1):
        return f"{fake.last_name_male()} {fake.first_name_male()} {fake.middle_name_male()}"
    else:
        return f"{fake.last_name_female()} {fake.first_name_female()} {fake.middle_name_female()}"


def generate_persons(count, bd_name):
    employees = {uuid.uuid4().hex: {"name": rand_name(), "birth_day": rand_date(),
                                    "phone": fake.phone_number(),
                                    "email": fake.ascii_free_email(),
                                    "job_title": str(fake.job()).lower(),
                                    "cabinet": str(random.randint(100, 400)),
                                    "skype": fake.phone_number()} for _ in range(count)}
    with open(bd_name, 'wb') as mydb:
        pickle.dump(employees, mydb)


generate_persons(200, "bd_employs.pkl")
