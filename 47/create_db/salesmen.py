from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lastname = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    sales = relationship("Sales", back_populates="sales_man")

    def __repr__(self):
        return f'Продавец: {self.firstname} {self.lastname}'
