from src.utils.repository import AbstractRepository
from src.utils.admins import get_hashed_password
from src.schemas.admins import AdminRegisterSchema


class AdminsService:
    def __init__(self, admins_repo: AbstractRepository):
        self.admins_repo: AbstractRepository = admins_repo()

    async def get_admin(self, login: str):
        admin = await self.admins_repo.find_one({"login": login})
        return admin
    
    async def create_admin(self, new_admin: AdminRegisterSchema):
        admin = await self.admins_repo.create_one(
            {
                "login": new_admin.login, 
                "hashed_password": get_hashed_password(new_admin.password),
                "permission": new_admin.permission,
                "school_id": new_admin.school_id,
            }
        )
        return admin

