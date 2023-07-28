from typing import Annotated, List

from fastapi import APIRouter, Depends

from src.api.dependencies import classrooms_service
from src.services.classrooms import ClassroomsService
from src.schemas.classrooms import ClassroomSchema

router = APIRouter(
    prefix="/classrooms",
    tags=["classrooms"],
)


@router.get("", response_model=List[ClassroomSchema])
async def get_classrooms(
    school_id: int,
    classrooms_service: Annotated[ClassroomsService, Depends(classrooms_service)],
):
    classrooms = await classrooms_service.get_classrooms(school_id)
    return classrooms
