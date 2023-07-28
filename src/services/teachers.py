from src.utils.repository import AbstractRepository


class TeachersService:
    def __init__(self, teachers_repo: AbstractRepository):
        self.teachers_repo: AbstractRepository = teachers_repo()

    async def get_teachers(self, school_id: int):
        teachers = await self.teachers_repo.find_all({"school_id": school_id})
        return teachers
    
    async def create_teacher(self, teacher_name: str, school_id: int):
        teacher_id = await self.teachers_repo.create_one(
            {"name": teacher_name, "school_id": school_id}
        )
        return teacher_id