from fastapi.testclient import TestClient 
from app.main import app 
from app.database.session import get_db
from app.models.outgroup_calls import OutgroupCall 
from app.schemas.outgroup_call import OutgroupCallSchema

from sqlalchemy.orm import Session 

client = TestClient(app) 

def test_get_communication_details(db: Session): 
    pass 
