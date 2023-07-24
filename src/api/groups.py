from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import groups_service
from src.services.groups import GroupsService

router = APIRouter(
    prefix="/groups",
    tags=["groups"],
)


@router.get("")
async def get_groups(
    school_id: int,
    groups_service: Annotated[GroupsService, Depends(groups_service)],
):
    groups = await groups_service.get_groups(school_id)
    return groups
