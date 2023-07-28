from src.utils.repository import AbstractRepository


class DaysService:
    def __init__(self, days_repo: AbstractRepository):
        self.days_repo: AbstractRepository = days_repo()

    async def get_days(self):
        days = await self.days_repo.find_all({})
        return days