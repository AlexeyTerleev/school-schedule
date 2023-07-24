from src.api.schedules import router as router_schedules
from src.api.cities import router as router_cities
from src.api.schools import router as router_schools
from src.api.groups import router as router_groups
from src.api.teachers import router as router_teachers

all_routers = [
    router_schedules,
    router_cities,
    router_schools,
    router_groups,
    router_teachers,
]
