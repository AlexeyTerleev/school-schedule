from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.teachers import TeacherSchema


class Teachers(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True)
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id"))
    name: Mapped[str]

    def to_read_model(self) -> TeacherSchema:
        return TeacherSchema(
            id=self.id,
            name=self.name,
        )