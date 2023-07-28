from pydantic import BaseModel


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
