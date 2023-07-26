from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.admins import AdminOutSchema


class Admins(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self) -> AdminOutSchema:
        return AdminOutSchema(
            id=self.id,
            login=self.login,
            hashed_password=self.hashed_password
        )