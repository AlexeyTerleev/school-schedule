from typing import Annotated, Optional
from datetime import datetime
import re

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status    

from src.api.dependencies import *
from src.services.admins import AdminsService
from src.services.cities import CitiesService
from src.services.classrooms import ClassroomsService
from src.services.groups import GroupsService
from src.services.periods import PeriodsService
from src.services.schedules import SchedulesService
from src.services.schools import SchoolsService
from src.services.subjects import SubjectsService
from src.services.teachers import TeachersService

from src.schemas.admins import TokenSchema, AdminSchema, AdminRegisterSchema
from src.schemas.cities import CityRegisterSchema
from src.schemas.classrooms import ClassroomRegisterSchema
from src.schemas.groups import GroupRegisterSchema
from src.schemas.periods import PeriodRegisterSchema
from src.schemas.schedules import ScheduleRegisterSchema
from src.schemas.schools import SchoolRegisterSchema
from src.schemas.subjects import SubjectRegisterSchema
from src.schemas.teachers import TeacherRegisterSchema

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
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )
    
@router.post("/register/admin")
async def create_admin(
    new_admin: AdminRegisterSchema,
    admins_service: Annotated[AdminsService, Depends(admins_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < new_admin.permission:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Permission denied"
            )
        try:
            await admins_service.get_admin(new_admin.login)
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="This login is already used"
                )
        except ValueError:
            ...
        if new_admin.permission < 2 and new_admin.school_id is None:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Admin with permission < 2, must also be linked to the school"
                )
        admin_id = await admins_service.create_admin(new_admin)
        return admin_id
    except HTTPException as e:
        raise e
    except Exception as e:
        raise e

@router.post("/delete/admin")
async def delete_admin(
    login: str,
    admins_service: Annotated[AdminsService, Depends(admins_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        delete_admin = await admins_service.get_admin(login)
        if admin.permission < delete_admin.permission or admin.id == delete_admin.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Permission denied"
            )
        admin_id = await admins_service.delete_admin(login)
        return admin_id
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with login {login} not found"
        )
    except Exception as e:
        raise e
    
@router.post("/register/city")
async def register_city(
    city: CityRegisterSchema,
    cities_service: Annotated[CitiesService, Depends(cities_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Permission denied"
            )
        city_id = await cities_service.create_city(city)
        return city_id
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )
    
@router.post("/register/school")
async def register_school(
    school: SchoolRegisterSchema,
    schools_service: Annotated[SchoolsService, Depends(schools_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Permission denied"
            )   
        school_id = await schools_service.create_school(school)
        return school_id
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )
    
@router.post("/register/subject")
async def register_subject(
    subject: SubjectRegisterSchema,
    subjects_service: Annotated[SubjectsService, Depends(subjects_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Permission denied"
            )   
        subject_id = await subjects_service.create_subject(subject)
        return subject_id
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )
    
@router.post("/register/period")
async def register_period(
    period: PeriodRegisterSchema,
    periods_service: Annotated[PeriodsService, Depends(periods_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Permission denied"
            )       
        period_id = await periods_service.create_period(period)
        return period_id
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )
    
@router.post("/register/classroom")
async def register_classroom(
    classroom: ClassroomRegisterSchema,
    classrooms_service: Annotated[ClassroomsService, Depends(classrooms_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < 2:
            classroom.school_id = admin.school_id
        classroom_id = await classrooms_service.create_classroom(classroom)
        return classroom_id
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )
    
@router.post("/register/group")
async def register_group(
    group: GroupRegisterSchema,
    groups_service: Annotated[GroupsService, Depends(groups_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < 2:
            group.school_id = admin.school_id
        group_id = await groups_service.create_group(group)
        return group_id
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )
    
@router.post("/register/teacher")
async def register_teacher(
    teacher: TeacherRegisterSchema,
    teachers_service: Annotated[TeachersService, Depends(teachers_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < 2:
            teacher.school_id = admin.school_id
        teacher_id = await teachers_service.create_teacher(teacher)
        return teacher_id
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )
    
@router.post("/register/schedule")
async def register_schedule(
    schedule: ScheduleRegisterSchema,
    schedule_service: Annotated[SchedulesService, Depends(schedules_service)],
    admin: Annotated[AdminSchema, Depends(get_current_admin)],
    ):
    try:
        if admin.permission < 2:
            schedule.school_id = admin.school_id
        schedule_id = await schedule_service.create_schedule(schedule)
        return schedule_id  
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )