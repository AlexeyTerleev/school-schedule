from src.models.cities import Cities
from src.utils.repository import SQLAlchemyRepository


class CitiesRepository(SQLAlchemyRepository):
    model = Cities
