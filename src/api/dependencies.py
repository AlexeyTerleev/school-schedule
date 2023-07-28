from src.repositories.schedules import SchedulesRepository
from src.services.schedules import SchedulesService

from src.repositories.cities import CitiesRepository
from src.services.cities import CitiesService

from src.repositories.schools import SchoolsRepository
from src.services.schools import SchoolsService

from src.repositories.groups import GroupsRepository
from src.services.groups import GroupsService

from src.repositories.teachers import TeachersRepository
from src.services.teachers import TeachersService

from src.repositories.admins import AdminsRepository
from src.services.admins import AdminsService

from src.schemas.admins import AdminSchema, TokenPayload
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt
from pydantic import ValidationError
from datetime import datetime
from typing import Annotated
from src.config import JWT_SECRET_KEY, ALGORITHM


def schedules_service():
    return SchedulesService(SchedulesRepository)

def cities_service():
    return CitiesService(CitiesRepository)

def schools_service():
    return SchoolsService(SchoolsRepository)

def groups_service():
    return GroupsService(GroupsRepository)

def teachers_service():
    return TeachersService(TeachersRepository)

def admins_service():
    return AdminsService(AdminsRepository)


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="./admins/login",
    scheme_name="JWT"
)

async def get_current_admin(
        admins_service: Annotated[AdminsService, Depends(admins_service)],
        token: str = Depends(reuseable_oauth),
        ) -> AdminSchema:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        admin = await admins_service.get_admin(token_data.sub)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    return admin
