from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    date = Column(String(10), nullable=False)
    summ = Column(Integer, nullable=False, default=0)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))


    def __repr__(self):
        return f'Продажа(Id: {self.id}) от: {self.date}, на сумму: {self.summ}'
        # return f'Sales(Id: {self.id}, date: {self.date}, summ: {self.summ},\
        #         customer_id: {self.customer_id},salesman_id: {self.salesman_id})'
