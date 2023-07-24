from src.models.schedules import Schedules
from src.utils.repository import SQLAlchemyRepository


class SchedulesRepository(SQLAlchemyRepository):
    model = Schedules
