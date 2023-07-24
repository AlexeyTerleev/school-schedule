from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import cities_service
from src.services.cities import CitiesService

router = APIRouter(
    prefix="/cities",
    tags=["cities"],
)


@router.get("")
async def get_cities(
    cities_service: Annotated[CitiesService, Depends(cities_service)],
):
    cities = await cities_service.get_cities()
    return cities
