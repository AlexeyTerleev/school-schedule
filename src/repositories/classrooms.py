from src.models.classrooms import Classrooms
from src.utils.repository import SQLAlchemyRepository


class ClassroomsRepository(SQLAlchemyRepository):
    model = Classrooms