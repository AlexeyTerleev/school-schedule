from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.api.dependencies import cities_service
from src.services.cities import CitiesService
from src.schemas.cities import CitySchema


router = APIRouter(
    prefix="/cities",
    tags=["cities"],
)


@router.get("", response_model=List[CitySchema])
async def get_cities(
    cities_service: Annotated[CitiesService, Depends(cities_service)],
):
    try: 
        cities = await cities_service.get_cities()
        return cities
    except: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Somthing went wrong"
        )