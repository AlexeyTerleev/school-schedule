from pydantic import BaseModel


class GroupSchema(BaseModel):
    id: int
    school_id: int
    name: str

    class Config:
        from_attributes = True

class GroupRegisterSchema(BaseModel):
    school_id: int
    name: str

    class Config:
        from_attributes = True
