from sqlalchemy import Column, ForeignKey, Integer, String, Table
from models.database import Base
from sqlalchemy.orm import relationship


class Sales(Base):
    __tablename__ = 'sales'
    # id = Column(Integer, primary_key=True, autoincrement=True) # ??? autoincrement=True проверить необходимость
    id = Column(Integer, primary_key=True)
    date = Column(String(10), nullable=False)
    summ = Column(Integer, nullable=False, default=0)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))


    def __repr__(self):
        return f'Sales(Id: {self.id}, date: {self.date}, summ: {self.summ},\
                customer_id: {self.customer_id},salesman_id: {self.salesman_id})'
