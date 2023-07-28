from src.utils.repository import AbstractRepository
from src.schemas.periods import PeriodRegisterSchema


class PeriodsService:
    def __init__(self, periods_repo: AbstractRepository):
        self.periods_repo: AbstractRepository = periods_repo()

    async def get_periods(self):
        periods = await self.periods_repo.find_all({})
        return periods
    
    async def create_period(self, period: PeriodRegisterSchema):
        period_id = await self.periods_repo.create_one(dict(period))
        return period_id