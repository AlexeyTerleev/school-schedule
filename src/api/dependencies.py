from src.repositories.admins import AdminsRepository
from src.repositories.cities import CitiesRepository
from src.repositories.classrooms import ClassroomsRepository
from src.repositories.days import DaysRepository
from src.repositories.groups import GroupsRepository
from src.repositories.periods import PeriodsRepository
from src.repositories.schedules import SchedulesRepository
from src.repositories.schools import SchoolsRepository
from src.repositories.subjects import SubjectsRepository
from src.repositories.teachers import TeachersRepository

from src.services.admins import AdminsService
from src.services.cities import CitiesService
from src.services.classrooms import ClassroomsService
from src.services.days import DaysService
from src.services.groups import GroupsService
from src.services.periods import PeriodsService
from src.services.schedules import SchedulesService
from src.services.schools import SchoolsService
from src.services.subjects import SubjectsService
from src.services.teachers import TeachersService

from src.schemas.admins import AdminSchema, TokenPayload
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt
from pydantic import ValidationError
from datetime import datetime
from typing import Annotated
from src.config import JWT_SECRET_KEY, ALGORITHM


def admins_service():
    return AdminsService(AdminsRepository)

def cities_service():
    return CitiesService(CitiesRepository)

def classrooms_service():
    return ClassroomsService(ClassroomsRepository)

def days_service():
    return DaysService(DaysRepository)

def groups_service():
    return GroupsService(GroupsRepository)

def periods_service():
    return PeriodsService(PeriodsRepository)

def schedules_service():
    return SchedulesService(SchedulesRepository)

def schools_service():
    return SchoolsService(SchoolsRepository)

def subjects_service():
    return SubjectsService(SubjectsRepository)

def teachers_service():
    return TeachersService(TeachersRepository)

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
