from src.models.subjects import Subjects
from src.utils.repository import SQLAlchemyRepository


class SubjectsRepository(SQLAlchemyRepository):
    model = Subjects