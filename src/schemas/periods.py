from datetime import time
from pydantic import BaseModel


class PeriodSchema(BaseModel):
    id: int
    start_time: time
    end_time: time

    class Config:
        from_attributes = True


class PeriodRegisterSchema(BaseModel):
    start_time: time
    end_time: time

    class Config:
        from_attributes = True
