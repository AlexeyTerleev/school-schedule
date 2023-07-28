from src.utils.repository import AbstractRepository
from src.schemas.schools import SchoolRegisterSchema


class SchoolsService:
    def __init__(self, schools_repo: AbstractRepository):
        self.schools_repo: AbstractRepository = schools_repo()

    async def get_schools(self, city_id: int):
        schools = await self.schools_repo.find_all({"city_id": city_id})
        return schools
    
    async def create_school(self, school: SchoolRegisterSchema):
        school_id = await self.schools_repo.create_one(dict(school))
        return school_id
