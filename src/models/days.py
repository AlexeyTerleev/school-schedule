from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.days import DaySchema


class Days(Base):
    __tablename__ = "days"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_read_model(self) -> DaySchema:
        return DaySchema(
            id=self.id,
            name=self.name,
        )