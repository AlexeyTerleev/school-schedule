from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.api.dependencies import subjects_service
from src.services.subjects import SubjectsService
from src.schemas.subjects import SubjectSchema


router = APIRouter(
    prefix="/subjects",
    tags=["subjects"],
)


@router.get("", response_model=List[SubjectSchema])
async def get_subjects(
    subjects_service: Annotated[SubjectsService, Depends(subjects_service)],
):
    try:
        subjects = await subjects_service.get_subjects()
        return subjects
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )