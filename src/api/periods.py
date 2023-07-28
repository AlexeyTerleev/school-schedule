from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import periods_service
from src.services.periods import PeriodsService

router = APIRouter(
    prefix="/periods",
    tags=["periods"],
)


@router.get("")
async def get_periods(
    periods_service: Annotated[PeriodsService, Depends(periods_service)],
):
    periods = await periods_service.get_periods()
    return periods