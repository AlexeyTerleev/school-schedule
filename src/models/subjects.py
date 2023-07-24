from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.subjects import SubjectSchema


class Subjects(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_read_model(self) -> SubjectSchema:
        return SubjectSchema(
            id=self.id,
            name=self.name,
        )