from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import days_service
from src.services.days import DaysService

router = APIRouter(
    prefix="/days",
    tags=["days"],
)


@router.get("")
async def get_days(
    days_service: Annotated[DaysService, Depends(days_service)],
):
    days = await days_service.get_days()
    return days