from pydantic import BaseModel


class DaySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
