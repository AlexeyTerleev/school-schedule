from src.models.schools import Schools
from src.utils.repository import SQLAlchemyRepository


class SchoolsRepository(SQLAlchemyRepository):
    model = Schools
