from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.schedules import ScheduleSchema


class Schedules(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True)
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id"))
    day_id: Mapped[int] = mapped_column(ForeignKey("days.id"))
    period_id: Mapped[int] = mapped_column(ForeignKey("periods.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    classroom_id: Mapped[int] = mapped_column(ForeignKey("classrooms.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))

    def to_read_model(self) -> ScheduleSchema:
        return ScheduleSchema(
            id=self.id,
            school_id=self.school_id,
            day_id=self.day_id,
            period_id=self.period_id,
            subject_id=self.subject_id,
            classroom_id=self.classroom_id,
            teacher_id=self.teacher_id,
            group_id=self.group_id,
        )