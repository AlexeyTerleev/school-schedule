
from pydantic import BaseModel


class SubjectSchema(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True

class SubjectRegisterSchema(BaseModel):
    name: str
    
    class Config:
        from_attributes = True
