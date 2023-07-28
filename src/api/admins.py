from typing import Annotated, Optional
from datetime import datetime
import re

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status    

from src.api.dependencies import (
    admins_service, 
    cities_service, 
    classrooms_service,
    groups_service,
    periods_service,
    schedules_service,
    schools_service, 
    subjects_service,
    teachers_service,
    get_current_admin,
)

from src.services.admins import AdminsService
from src.services.cities import CitiesService
from src.services.classrooms import ClassroomsService
from src.services.groups import GroupsService
from src.services.periods import PeriodsService
from src.services.schedules import SchedulesService
from src.services.schools import SchoolsService
from src.services.subjects import SubjectsService
from src.services.teachers import TeachersService

from src.schemas.admins import TokenSchema, AdminSchema

from src.utils.admins import verify_password, create_access_token, create_refresh_token, get_hashed_password


router = APIRouter(
    prefix="/admins",
    tags=["admins"],
)

@router.post('/login', summary="Create access tokens for admin", response_model=TokenSchema)
async def login(
    admins_service: Annotated[AdminsService, Depends(admins_service)],
    form_data: OAuth2PasswordRequestForm = Depends(), 
):
    try:
        admin = await admins_service.get_admin(form_data.username)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect login"
        )
    if not verify_password(form_data.password, admin.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )

    return {
        "access_token": create_access_token(admin.login),
        "refresh_token": create_refresh_token(admin.login),
    }

@router.post("/register/admin")
async def create_admin(
    login: str,
    password: str,
    permission: int,
    school_id: Optional[int],
    admins_service: Annotated[AdminsService, Depends(admins_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    if admin.permission != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Permission denied"
        )
    if permission != 1 and school_id is None:
        raise ValueError
    admin_id = await admins_service.create_admin(login, password, permission, school_id)
    return admin_id

@router.post("/register/city")
async def register_city(
    city_name: str,
    cities_service: Annotated[CitiesService, Depends(cities_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    if admin.permission != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Permission denied"
        )
    city_id = await cities_service.create_city(city_name)
    return city_id

@router.post("/register/school")
async def register_school(
    school_name: str,
    city_id: int,
    schools_service: Annotated[SchoolsService, Depends(schools_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    if admin.permission != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Permission denied"
        )   
    school_id = await schools_service.create_school(school_name, city_id)
    return school_id

@router.post("/register/subject")
async def register_subject(
    subject_name: str,
    subjects_service: Annotated[SubjectsService, Depends(subjects_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    if admin.permission != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Permission denied"
        )   
    subject_id = await subjects_service.create_subject(subject_name)
    return subject_id

@router.post("/register/period")
async def register_period(
    start_time_str: str,
    end_time_str: str,
    periods_service: Annotated[PeriodsService, Depends(periods_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    if admin.permission != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Permission denied"
        )   
    
    if not re.match(r"^\d\d\:\d\d$", start_time_str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {start_time_str}"
        )  
    if not re.match(r"^\d\d\:\d\d$", end_time_str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {end_time_str}"
        ) 
    
    start_time_obj = datetime.strptime(start_time_str, "%H:%M").time()
    end_time_obj = datetime.strptime(end_time_str, "%H:%M").time()

    period_id = await periods_service.create_period(start_time_obj, end_time_obj)
    return period_id

@router.post("/register/classroom")
async def register_classroom(
    classrooms_service: Annotated[ClassroomsService, Depends(classrooms_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    classroom_name: str,
    school_id: Optional[int] = None,
    ):
    if admin.permission != 1:
        school_id = admin.school_id
    classroom_id = await classrooms_service.create_classroom(classroom_name, school_id)
    return classroom_id

@router.post("/register/group")
async def register_group(
    groups_service: Annotated[GroupsService, Depends(groups_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    group_name: str,
    school_id: Optional[int] = None,
    ):
    if admin.permission != 1:
        school_id = admin.school_id
    group_id = await groups_service.create_group(group_name, school_id)
    return group_id

@router.post("/register/teacher")
async def register_teacher(
    teachers_service: Annotated[TeachersService, Depends(teachers_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    teacher_name: str,
    school_id: Optional[int] = None,
    ):
    if admin.permission != 1:
        school_id = admin.school_id
    teacher_id = await teachers_service.create_teacher(teacher_name, school_id)
    return teacher_id

@router.post("/register/schedule")
async def register_schedule(
    schedule_service: Annotated[SchedulesService, Depends(schedules_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    day_id: int, 
    period_id: int, 
    subject_id: int, 
    classroom_id: int, 
    teacher_id: int, 
    group_id: int,
    school_id: Optional[int] = None, 
    ):
    if admin.permission != 1:
        school_id = admin.school_id
    schedule_id = await schedule_service.create_schedule(
        school_id, day_id, period_id, subject_id, classroom_id, teacher_id, group_id,
    )
    return schedule_id