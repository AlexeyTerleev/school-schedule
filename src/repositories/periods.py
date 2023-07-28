from src.models.periods import Periods
from src.utils.repository import SQLAlchemyRepository


class PeriodsRepository(SQLAlchemyRepository):
    model = Periods