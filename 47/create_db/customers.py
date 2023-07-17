from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    sales = relationship('Sales')

    def __repr__(self):
        return f'Customers: {self.surname} {self.name} '
