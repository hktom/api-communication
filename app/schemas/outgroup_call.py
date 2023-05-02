from pydantic import BaseModel 

class OutgroupCallSchema(BaseModel): 
    id : int 
    call_id : int 
    call_date : str 
    service_num : str 
    operator_id : int 
    operator_name: str 
    operator_mail: str 
    group_id : int 
    group_name : str 
    waiting_duration: int 
    communication_duration: int 
    on_hold_duration : int 
    catchup_duration : int 
    post_call_duration: int  

    class Config: 
        orm_mode = True 