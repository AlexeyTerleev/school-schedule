from src.api.admins import router as router_admin
from src.api.cities import router as router_cities
from src.api.classrooms import router as router_classrooms
from src.api.days import router as router_days
from src.api.groups import router as router_groups
from src.api.periods import router as router_periods
from src.api.schedules import router as router_schedules
from src.api.schools import router as router_schools
from src.api.subjects import router as router_subjects
from src.api.teachers import router as router_teachers


all_routers = [
    router_admin,
    router_cities,
    router_classrooms,
    router_days,
    router_groups,
    router_periods,
    router_schedules,
    router_schools,
    router_subjects,
    router_teachers,
]
