from src.utils.repository import AbstractRepository
from datetime import time


class PeriodsService:
    def __init__(self, periods_repo: AbstractRepository):
        self.periods_repo: AbstractRepository = periods_repo()

    async def get_periods(self):
        periods = await self.periods_repo.find_all({})
        return periods
    
    async def create_period(self, start_time: time, end_time: time):
        period_id = await self.periods_repo.create_one(
            {"start_time": start_time, "end_time": end_time}
        )
        return period_id