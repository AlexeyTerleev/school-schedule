from src.utils.repository import AbstractRepository
from src.schemas.teachers import TeacherRegisterSchema


class TeachersService:
    def __init__(self, teachers_repo: AbstractRepository):
        self.teachers_repo: AbstractRepository = teachers_repo()

    async def get_teachers(self, school_id: int):
        teachers = await self.teachers_repo.find_all({"school_id": school_id})
        return teachers
    
    async def create_teacher(self, teacher: TeacherRegisterSchema):
        teacher_id = await self.teachers_repo.create_one(dict(teacher))
        return teacher_id