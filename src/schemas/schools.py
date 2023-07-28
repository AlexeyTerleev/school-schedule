from pydantic import BaseModel


class SchoolSchema(BaseModel):
    id: int
    city_id: int
    name: str
    
    class Config:
        from_attributes = True

class SchoolRegisterSchema(BaseModel):
    city_id: int
    name: str
    
    class Config:
        from_attributes = True
