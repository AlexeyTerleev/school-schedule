from pydantic import BaseModel


class ClassroomSchema(BaseModel):
    id: int
    school_id: int
    name: str

    class Config:
        from_attributes = True


class ClassroomRegisterSchema(BaseModel):
    school_id: int
    name: str

    class Config:
        from_attributes = True
