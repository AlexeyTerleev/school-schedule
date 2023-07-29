from src.utils.repository import AbstractRepository
from src.schemas.schedules import ScheduleRegisterSchema


class SchedulesService:
    def __init__(self, schedules_repo: AbstractRepository):
        self.schedules_repo: AbstractRepository = schedules_repo()

    async def get_schedules_group(self, group_id: int):
        schedules = await self.schedules_repo.get_shedule({"group_id": group_id})
        return schedules    

    async def get_schedules_teacher(self, teacher_id: int):
        schedules = await self.schedules_repo.get_shedule({"teacher_id": teacher_id})
        return schedules

    async def create_schedule(self, schedule: ScheduleRegisterSchema):
        schedule_id = await self.schedules_repo.create_one(dict(schedule))
        return schedule_id