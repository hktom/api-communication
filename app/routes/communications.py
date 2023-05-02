from fastapi import APIRouter, Depends, HTTPException, status , Query 
from sqlalchemy import select 

from auth.authenticate import authenticate
from database.session import Session, get_db
from models.user import User 
from models.outgroup_calls import OutgroupCall
from schemas.outgroup_call import OutgroupCallSchema 

communications_router = APIRouter() 

def get_current_user() -> User: 
    pass 

@communications_router.get("/communications/", response_model=OutgroupCallSchema) 
async def retrieve_communication_details(db: Session = Depends(get_db), current_user=Depends(get_current_user), page : int = Query(1, gt=0), 
                                         per_page : int= Query(10, gt=0, le=100)) -> dict: 
    
    offset = (page - 1) * per_page 
    query2 = select(OutgroupCall)
    query = db.query(OutgroupCall).offset(offset).limit(per_page)
    communications = query.all()
    return communications 
    