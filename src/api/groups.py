from typing import Annotated, List

from fastapi import APIRouter, Depends

from src.api.dependencies import groups_service
from src.services.groups import GroupsService
from src.schemas.groups import GroupSchema

router = APIRouter(
    prefix="/groups",
    tags=["groups"],
)


@router.get("", response_model=List[GroupSchema])
async def get_groups(
    school_id: int,
    groups_service: Annotated[GroupsService, Depends(groups_service)],
):
    groups = await groups_service.get_groups(school_id)
    return groups
