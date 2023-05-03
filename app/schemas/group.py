from pydantic import BaseModel 

class GroupSchema(BaseModel): 
    id : int 
    group_name : str 

    class Config: 
        orm_mode = True 