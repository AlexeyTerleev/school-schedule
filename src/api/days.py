from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.api.dependencies import days_service
from src.services.days import DaysService
from src.schemas.days import DaySchema

router = APIRouter(
    prefix="/days",
    tags=["days"],
)


@router.get("", response_model=List[DaySchema])
async def get_days(
    days_service: Annotated[DaysService, Depends(days_service)],
):
    try:
        days = await days_service.get_days()
        return days
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong"
        )