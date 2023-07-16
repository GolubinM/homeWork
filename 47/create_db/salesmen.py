from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    sales = relationship('Sales')


    def __init__(self, fullname):
        self.surname = fullname[0]
        self.name = fullname[1]

    def __repr__(self):
        return f'Salesman: {self.surname} {self.name} '
