from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import schedules_service
from src.services.schedules import SchedulesService

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"],
)


@router.get("")
async def get_schedules(
    school_id: int,
    schedules_service: Annotated[SchedulesService, Depends(schedules_service)],
):
    schedules = await schedules_service.get_schedules(school_id)
    return schedules
