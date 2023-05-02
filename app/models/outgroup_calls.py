from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from database.base import Base




class OutgroupCall(Base): 
    __tablename__ = 'appels_groupe_out'

    id = Column(Integer, primary_key=True, )
    call_id = Column(Integer, ForeignKey('calls.id')) 
    call_date = Column(DateTime, nullable=False) 
    service_num = Column(String) 
    operator_id = Column(Integer, ForeignKey('operators.id'))
    operator_name = Column(String(255)) 
    operator_mail = Column(String(255)) 
    group_id = Column(Integer, ForeignKey('groups.id')) 
    group_name = Column(String(255)) 
    waiting_duration = Column(Integer) 
    communicaiton_duration = Column(Integer) 
    on_hold_duration = Column(Integer) 
    catchup_duration = Column(Integer) 
    post_call_duration = Column(Integer) 
    ring_duration = Column(Integer)


class OutgroupCallDuration(Base): 
    __tablename__ = 'appels_group_out_durees' 
    id = Column(Integer, ForeignKey('appels_group_out.id')) 
    duration = Column(Integer) 
