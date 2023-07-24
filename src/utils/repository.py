from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from src.db.db import async_session_maker


class AbstractRepository(ABC):
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):

    model = None
    
    async def find_all(self, filter_by):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
