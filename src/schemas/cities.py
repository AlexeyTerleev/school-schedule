from pydantic import BaseModel


class CitySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class CityRegisterSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True