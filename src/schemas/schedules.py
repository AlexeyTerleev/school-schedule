from pydantic import BaseModel

from src.schemas.days import DaySchema
from src.schemas.periods import PeriodSchema
from src.schemas.subjects import SubjectSchema
from src.schemas.classrooms import ClassroomSchema
from src.schemas.groups import GroupSchema
from src.schemas.teachers import TeacherSchema


class ScheduleSchema(BaseModel):
    id: int
    school_id: int
    day_id: int
    period_id: int
    subject_id: int
    classroom_id: int
    teacher_id: int
    group_id: int
    
    class Config:
        from_attributes = True


class ScheduleOutSchema(BaseModel):
    day: DaySchema
    period: PeriodSchema
    subject: SubjectSchema
    classroom: ClassroomSchema
    group: GroupSchema
    teacher: TeacherSchema
    
    class Config:
        from_attributes = True


class ScheduleRegisterSchema(BaseModel):
    school_id: int
    day_id: int
    period_id: int
    subject_id: int
    classroom_id: int
    teacher_id: int
    group_id: int
    
    class Config:
        from_attributes = True
