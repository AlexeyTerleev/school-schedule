from src.models.days import Days
from src.utils.repository import SQLAlchemyRepository


class DaysRepository(SQLAlchemyRepository):
    model = Days