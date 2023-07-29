from src.models.schedules import Schedules
from src.models.days import Days
from src.models.periods import Periods
from src.models.subjects import Subjects
from src.models.classrooms import Classrooms
from src.models.groups import Groups
from src.models.teachers import Teachers
from src.utils.repository import SQLAlchemyRepository

from sqlalchemy import insert, select

from src.db.db import async_session_maker


class SchedulesRepository(SQLAlchemyRepository):
    model = Schedules

    async def get_shedule(self, filter: dict):
        async with async_session_maker() as session:
            stmt = \
            select(self.model, Days, Periods, Subjects, Classrooms, Groups, Teachers)\
                .filter_by(**filter)\
                .join(Days).join(Periods).join(Subjects).join(Classrooms).join(Teachers)
            res = await session.execute(stmt)
            headers = ["day", "period", "subject", "classroom", "group", "teacher"]
            res = [dict(zip(headers, [y.to_read_model() for y in x[1::]])) for x in res.all()]
            return res