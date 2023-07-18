from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_NAME = 'sales.db'
ECHO = False
engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=ECHO)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
