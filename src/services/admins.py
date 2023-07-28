from src.utils.repository import AbstractRepository
from src.utils.admins import get_hashed_password


class AdminsService:
    def __init__(self, admins_repo: AbstractRepository):
        self.admins_repo: AbstractRepository = admins_repo()

    async def get_admin(self, login: str):
        admin = await self.admins_repo.find_one({"login": login})
        return admin
    
    async def create_admin(self, login: str, password: str, permission: int, school_id: int):
        admin = await self.admins_repo.create_one(
            {
                "login": login, 
                "hashed_password": get_hashed_password(password),
                "permission": permission,
                "school_id": school_id,
            }
        )
        return admin

