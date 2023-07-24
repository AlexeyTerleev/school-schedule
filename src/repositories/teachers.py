from src.models.teachers import Teachers
from src.utils.repository import SQLAlchemyRepository


class TeachersRepository(SQLAlchemyRepository):
    model = Teachers