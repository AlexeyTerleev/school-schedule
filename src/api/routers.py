from src.api.schedules import router as router_schedules
from src.api.cities import router as router_cities
from src.api.schools import router as router_schools
from src.api.groups import router as router_groups

all_routers = [
    router_schedules,
    router_cities,
    router_schools,
    router_groups,
]
