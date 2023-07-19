from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    _sales = relationship("Sales", cascade="all, delete, delete-orphan", back_populates="_salesman")

    def __repr__(self):
        return f'Продавец: {self.firstname} {self.lastname}'

    def _get_info(self):
        return {'id': self.id, 'firstname': self.firstname, 'lastname': self.lastname}
