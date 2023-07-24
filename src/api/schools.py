from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import schools_service
from src.services.schools import SchoolsService

router = APIRouter(
    prefix="/schools",
    tags=["schools"],
)


@router.get("")
async def get_schools(
    city_id: int,
    schools_service: Annotated[SchoolsService, Depends(schools_service)],
):
    schools = await schools_service.get_schools(city_id)
    return schools
