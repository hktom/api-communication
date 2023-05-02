from pydantic import BaseModel 

class CallSchema(BaseModel): 
    id : int 
    operator_1_id : int 
    operator_2_id : int 
    caller_number : str 
    receiver_number : str 
    service_id : int 
    service_number: str 

    class Config: 
        orm_mode = True 