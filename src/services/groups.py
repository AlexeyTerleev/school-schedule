from src.utils.repository import AbstractRepository


class GroupsService:
    def __init__(self, groups_repo: AbstractRepository):
        self.groups_repo: AbstractRepository = groups_repo()

    async def get_groups(self, school_id: int):
        groups = await self.groups_repo.find_all({"school_id": school_id})
        return groups
