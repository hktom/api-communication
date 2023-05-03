from sqlalchemy import Column, Integer, String 

from database.base import Base 

class Operator(Base): 
    __tablename__ = 'operateurs'
    id = Column(Integer, primary_key=True) 
    operator_name = Column(String(255)) 
    operator_email = Column(String(255)) 