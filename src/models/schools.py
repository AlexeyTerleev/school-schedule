from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.schools import SchoolSchema


class Schools(Base):
    __tablename__ = "schools"

    id: Mapped[int] = mapped_column(primary_key=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    name: Mapped[str]

    def to_read_model(self) -> SchoolSchema:
        return SchoolSchema(
            id=self.id,
            city_id=self.city_id,
            name=self.name,
        )