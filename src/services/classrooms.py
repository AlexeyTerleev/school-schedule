from src.utils.repository import AbstractRepository


class ClassroomsService:
    def __init__(self, classrooms_repo: AbstractRepository):
        self.classrooms_repo: AbstractRepository = classrooms_repo()

    async def get_classrooms(self, school_id: int):
        classrooms = await self.classrooms_repo.find_all({"school_id": school_id})
        return classrooms
    
    async def create_classroom(self, classroom_name: str, school_id: int):
        classroom_id = await self.classrooms_repo.create_one(
            {"name": classroom_name, "school_id": school_id}
        )
        return classroom_id