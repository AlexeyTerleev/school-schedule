from src.utils.repository import AbstractRepository


class SchedulesService:
    def __init__(self, schedules_repo: AbstractRepository):
        self.schedules_repo: AbstractRepository = schedules_repo()

    async def get_schedules(self, school_id: int):
        schedules = await self.schedules_repo.find_all({"school_id": school_id})
        return schedules
