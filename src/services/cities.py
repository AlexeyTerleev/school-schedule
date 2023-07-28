from src.utils.repository import AbstractRepository


class CitiesService:
    def __init__(self, cities_repo: AbstractRepository):
        self.cities_repo: AbstractRepository = cities_repo()

    async def get_cities(self):
        cities = await self.cities_repo.find_all({})
        return cities
    
    async def create_city(self, city_name: str):
        city_id = await self.cities_repo.create_one(
            {"name": city_name}
        )
        return city_id

