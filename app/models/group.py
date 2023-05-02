from sqlalchemy import Column, Integer, String 

from database.base import Base 

class Group(Base): 
    __tablename__ = 'groupes' 
    id = Column(Integer, primary_key=True) 
    group_name = Column(String(255)) 