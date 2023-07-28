from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status    

from src.api.dependencies import admins_service, cities_service, schools_service, get_current_admin
from src.services.admins import AdminsService

from src.services.cities import CitiesService
from src.services.schools import SchoolsService

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

#TMP ------------
@router.get('/get_hashed_password')
async def tmp(password):
    return {"hashed_password" : get_hashed_password(password)}
#TMP ------------

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
        raise PermissionError
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
