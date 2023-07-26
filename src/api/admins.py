from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status    

from src.api.dependencies import admins_service, get_current_admin
from src.services.admins import AdminsService

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

@router.post("/test")
async def create_user(
    admin: AdminSchema = Depends(get_current_admin)
    ):
    return {'status': 'good'}