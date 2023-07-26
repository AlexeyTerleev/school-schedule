from src.utils.repository import AbstractRepository


class AdminsService:
    def __init__(self, admins_repo: AbstractRepository):
        self.admins_repo: AbstractRepository = admins_repo()

    async def get_admin(self, login: str):
        admin = await self.admins_repo.find_one({"login": login})
        return admin

