from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.api.dependencies import periods_service
from src.services.periods import PeriodsService
from src.schemas.periods import PeriodSchema

router = APIRouter(
    prefix="/periods",
    tags=["periods"],
)


@router.get("", response_model=List[PeriodSchema])
async def get_periods(
    periods_service: Annotated[PeriodsService, Depends(periods_service)],
):
    try:
        periods = await periods_service.get_periods()
        return periods
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )