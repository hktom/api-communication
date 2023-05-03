import unittest

from fastapi.testclient import TestClient 
from app.main import app 
from app.database.session import get_db
from app.models.outgroup_calls import OutgroupCall 
from app.schemas.outgroup_call import OutgroupCallSchema

from sqlalchemy.orm import Session 

client = TestClient(app) 

class CommunicationEndpointTest(unittest.TestCase): 

    def setUp(self) -> None:
        # setup mock database here
        return super().setUp()
    
    def test_get_communication_details(self): 
        expected_payload = {
            "communication_details_operator" : [
                {
                    "id": 1, 
                    "id_appel": 2, 
                    "date" : "2022-08-01T08:35:28",
                    "service_num": 33, 
                    "operator.id": 25, 
                    "operator.name": "tom", 
                    "operator.email": "thikari@github.com", 
                    "group.id": 123, 
                    "group.name": "SA", 
                    "waiting_duration": 24, 
                    "communication_duration": 587, 
                    "on_hold_duration": 18, 
                    "ringing_duration": 2, 
                    "catchup_duration": 15, 
                    "postcal_duration": 71, 
                    "transfer_id": 4564
                }
            ]
        }
        client.post("/communications", expected_payload)
        response = client.get("/communications") 
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json(), expected_payload)

