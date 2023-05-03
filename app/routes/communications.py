from typing import List

from fastapi import APIRouter, Depends, HTTPException, status , Query 
from sqlalchemy import select 

from auth.authenticate import authenticate
from database.session import Session, get_db
from models.user import User 
from models.outgroup_calls import OutgroupCall, OutgroupCallDuration
from models.group import Group
from models.call import Call
from models.operator import Operator
from schemas.outgroup_call import OutgroupCallSchema 

communications_router = APIRouter() 

def get_current_user() -> User: 
    # Get current authenticated user here 
    pass 

@communications_router.get("/", response_model=OutgroupCallSchema) 
async def retrieve_communication_details(db: Session = Depends(get_db), current_user=Depends(get_current_user), page : int = Query(1, gt=0), 
                                         per_page : int= Query(10, gt=0, le=100)) -> List[dict]: 
    
    offset = (page - 1) * per_page 
    statement = select(OutgroupCall).join(OutgroupCall.call_id).join(OutgroupCall.call_date).join(OutgroupCall.service_num).join(OutgroupCall.operator_id).\
        join(Operator.operator_name).join(Operator.operator_email).join(OutgroupCall.group_id).join(Group.name).join(OutgroupCall.ring_duration).\
            join(OutgroupCall.waiting_duration).join(OutgroupCall.communication_duration).join(OutgroupCallDuration.duration)
    
    
    query = db.query(OutgroupCall).offset(offset).limit(per_page)
    communications = query.all()
    return communications
    