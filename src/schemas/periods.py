from datetime import datetime
from pydantic import BaseModel


class PeriodSchema(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime

    class Config:
        from_attributes = True
