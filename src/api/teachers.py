from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import teachers_service
from src.services.teachers import TeachersService

router = APIRouter(
    prefix="/teachers",
    tags=["teachers"],
)


@router.get("")
async def get_teachers(
    school_id: int,
    teachers_service: Annotated[TeachersService, Depends(teachers_service)],
):
    teachers = await teachers_service.get_teachers(school_id)
    return teachers