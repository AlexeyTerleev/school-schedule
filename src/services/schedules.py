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

    async def create_schedule(
            self, school_id: int, day_id: int, 
            period_id: int, subject_id: int, 
            classroom_id: int, teacher_id: int, group_id: int
        ):
        schedule_id = await self.schedules_repo.create_one(
            {
                "school_id": school_id, 
                "day_id": day_id,
                "period_id": period_id,
                "subject_id": subject_id,
                "classroom_id": classroom_id,
                "teacher_id": teacher_id,
                "group_id": group_id,
            }
        )
        return schedule_id