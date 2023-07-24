from src.repositories.schedules import SchedulesRepository
from src.services.schedules import SchedulesService

from src.repositories.cities import CitiesRepository
from src.services.cities import CitiesService

from src.repositories.schools import SchoolsRepository
from src.services.schools import SchoolsService

from src.repositories.groups import GroupsRepository
from src.services.groups import GroupsService


def schedules_service():
    return SchedulesService(SchedulesRepository)

def cities_service():
    return CitiesService(CitiesRepository)

def schools_service():
    return SchoolsService(SchoolsRepository)

def groups_service():
    return GroupsService(GroupsRepository)