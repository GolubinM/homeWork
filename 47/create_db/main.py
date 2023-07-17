import os
from database import DATABASE_NAME, Session
import create_database as db_creator

# from salesmen import Salesmen
# from sales import Sales
# from customers import Customers

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
