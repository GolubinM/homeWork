import os
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from sales import Sales
from customers import Customers
from salesmen import Salesmen

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()