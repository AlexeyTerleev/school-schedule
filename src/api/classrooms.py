from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import classrooms_service
from src.services.classrooms import ClassroomsService

router = APIRouter(
    prefix="/classrooms",
    tags=["classrooms"],
)


@router.get("")
async def get_classrooms(
    school_id: int,
    classrooms_service: Annotated[ClassroomsService, Depends(classrooms_service)],
):
    classrooms = await classrooms_service.get_classrooms(school_id)
    return classrooms
