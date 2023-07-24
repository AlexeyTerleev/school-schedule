from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.groups import GroupSchema


class Groups(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id"))
    name: Mapped[str]

    def to_read_model(self) -> GroupSchema:
        return GroupSchema(
            id=self.id,
            school_id=self.school_id,
            name=self.name,
        )