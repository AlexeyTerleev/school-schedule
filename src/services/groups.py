from src.utils.repository import AbstractRepository
from src.schemas.groups import GroupRegisterSchema


class GroupsService:
    def __init__(self, groups_repo: AbstractRepository):
        self.groups_repo: AbstractRepository = groups_repo()

    async def get_groups(self, school_id: int):
        groups = await self.groups_repo.find_all({"school_id": school_id})
        return groups

    async def create_group(self, group: GroupRegisterSchema):
        group_id = await self.groups_repo.create_one(dict(group))
        return group_id

