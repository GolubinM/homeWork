from sqlalchemy import Column, Integer, String, CheckConstraint
from database import Base
from sqlalchemy.orm import relationship


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), CheckConstraint('firstname is not Null AND firstname !=""'), nullable=False)
    lastname = Column(String(100), CheckConstraint('lastname is not Null AND lastname !=""'), nullable=False)
    _sales = relationship('Sales', cascade="all, delete, delete-orphan", back_populates="_customer")

    def __repr__(self):
        return f'Клиент: {self.firstname} {self.lastname}'

    def _get_info(self):
        return {'id': self.id, 'firstname': self.firstname, 'lastname': self.lastname}
