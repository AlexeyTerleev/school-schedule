from typing import Annotated, List

from fastapi import APIRouter, Depends

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
    schools = await schools_service.get_schools(city_id)
    return schools
