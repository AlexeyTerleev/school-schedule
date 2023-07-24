from src.models.groups import Groups
from src.utils.repository import SQLAlchemyRepository


class GroupsRepository(SQLAlchemyRepository):
    model = Groups