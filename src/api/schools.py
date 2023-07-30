from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.api.dependencies import schools_service
from src.services.schools import SchoolsService
from src.schemas.schools import SchoolSchema


router = APIRouter(
    prefix="/schools",
    tags=["schools"],
)


@router.get("", response_model=List[SchoolSchema])
async def get_schools(
    city_id: int,
    schools_service: Annotated[SchoolsService, Depends(schools_service)],
):
    try:
        schools = await schools_service.get_schools(city_id)
        return schools
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )