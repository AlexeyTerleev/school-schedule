from src.models.admins import Admins
from src.utils.repository import SQLAlchemyRepository


class AdminsRepository(SQLAlchemyRepository):
    model = Admins