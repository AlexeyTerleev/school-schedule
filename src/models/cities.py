from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.cities import CitySchema


class Cities(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_read_model(self) -> CitySchema:
        return CitySchema(
            id=self.id,
            name=self.name,
        )