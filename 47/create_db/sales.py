from sqlalchemy import Column, ForeignKey, Integer, String, CheckConstraint
from database import Base
from sqlalchemy.orm import relationship


class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    date = Column(String(10), CheckConstraint('date is not Null AND date !=""'), nullable=False)
    summ = Column(Integer, CheckConstraint('summ > 0'), nullable=False, default=0)
    salesman_id = Column(Integer, CheckConstraint('salesman_id is not Null AND salesman_id !=""'),
                         ForeignKey('salesmen.id'))
    customer_id = Column(Integer, CheckConstraint('customer_id is not Null AND customer_id !=""'),
                         ForeignKey('customers.id'))
    _salesman = relationship('Salesmen', back_populates="_sales")
    _customer = relationship('Customers', back_populates="_sales")

    def __repr__(self):
        return f'Продажа(Id: {self.id}) от: {self.date}, на сумму: {self.summ}'
        # return f'Sales(Id: {self.id}, date: {self.date}, summ: {self.summ},\
        #         customer_id: {self.customer_id},salesman_id: {self.salesman_id})'

    def _get_info(self):
        return {'id': self.id, 'date': self.date, 'summ': self.summ, 'salesman_id': self.salesman_id,
                'customer_id': self.customer_id}
