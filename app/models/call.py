from sqlalchemy import Column, Integer, String, ForeignKey

from database.base import Base 

class Call(Base): 
    __tablename__ = 'appels' 
    id = Column(Integer, primary_key=True) 
    operator_1_id = Column(Integer, ForeignKey('operators.id'))
    operator_2_id = Column(Integer, ForeignKey('operators.id'))
    caller_number = Column(String(255)) 
    receiver_number = Column(String(255)) 
    service_id = Column(Integer, ForeignKey('services.id')) 
    service_number = Column(String(255)) 