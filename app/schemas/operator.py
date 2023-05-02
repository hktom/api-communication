from pydantic import BaseModel, EmailStr

class OperatorSchema(BaseModel):
    id : int 
    operator_name : str  
    operator_email : EmailStr

    class Config: 
        orm_mode = True 