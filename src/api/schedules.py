from typing import Annotated, List

from fastapi import APIRouter, Depends

from src.api.dependencies import schedules_service
from src.services.schedules import SchedulesService
from src.schemas.schedules import ScheduleOutSchema, ScheduleSchema

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"],
)


@router.get("/group", response_model=List[ScheduleOutSchema])
async def get_schedules_group(
    group_id: int,
    schedules_service: Annotated[SchedulesService, Depends(schedules_service)],
):
    schedules = await schedules_service.get_schedules_group(group_id)
    return schedules

@router.get("/teacher", response_model=List[ScheduleOutSchema])
async def get_schedules_teacher(
    teacher_id: int,
    schedules_service: Annotated[SchedulesService, Depends(schedules_service)],
):
    schedules = await schedules_service.get_schedules_teacher(teacher_id)
    return schedules
