
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.classrooms import ClassroomSchema


class Classrooms(Base):
    __tablename__ = "classrooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id"))
    name: Mapped[str]

    def to_read_model(self) -> ClassroomSchema:
        return ClassroomSchema(
            id=self.id,
            school_id=self.school_id,
            name=self.name,
        )