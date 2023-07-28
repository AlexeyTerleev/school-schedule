from src.utils.repository import AbstractRepository


class SchoolsService:
    def __init__(self, schools_repo: AbstractRepository):
        self.schools_repo: AbstractRepository = schools_repo()

    async def get_schools(self, city_id: int):
        schools = await self.schools_repo.find_all({"city_id": city_id})
        return schools
    
    async def create_school(self, school_name: str, city_id: int):
        school_id = await self.schools_repo.create_one(
            {"name": school_name, "city_id": city_id}
        )
        return school_id
