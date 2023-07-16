from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    customer_id = relationship('Sales')

    def __init__(self, fullname):
        self.surname = fullname[0]
        self.name = fullname[1]

    def __repr__(self):
        return f'Customers: {self.surname} {self.name} '
