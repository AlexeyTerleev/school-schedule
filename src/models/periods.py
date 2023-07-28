from datetime import time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.periods import PeriodSchema


class Periods(Base):
    __tablename__ = "periods"

    id: Mapped[int] = mapped_column(primary_key=True)
    start_time: Mapped[time]
    end_time: Mapped[time]

    def to_read_model(self) -> PeriodSchema:
        return PeriodSchema(
            id=self.id,
            start_time=self.start_time,
            end_time=self.end_time,
        )