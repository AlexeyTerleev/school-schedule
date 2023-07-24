from src.utils.repository import AbstractRepository


class SchedulesService:
    def __init__(self, schedules_repo: AbstractRepository):
        self.schedules_repo: AbstractRepository = schedules_repo()

    async def get_schedules_group(self, group_id: int):
        schedules = await self.schedules_repo.find_all({"group_id": group_id})
        return schedules

    async def get_schedules_teacher(self, teacher_id: int):
        schedules = await self.schedules_repo.find_all({"teacher_id": teacher_id})
        return schedules
