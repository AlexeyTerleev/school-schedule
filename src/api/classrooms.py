from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

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
    try:
        classrooms = await classrooms_service.get_classrooms(school_id)
        return classrooms
    except:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Something went wrong"
            )
