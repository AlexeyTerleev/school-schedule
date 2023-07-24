from pydantic import BaseModel


class TeacherSchema(BaseModel):
    id: int
    school_id: int
    name: str
    
    class Config:
        from_attributes = True
