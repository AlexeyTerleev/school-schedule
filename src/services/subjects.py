from src.utils.repository import AbstractRepository


class SubjectsService:
    def __init__(self, subjects_repo: AbstractRepository):
        self.subjects_repo: AbstractRepository = subjects_repo()

    async def get_subjects(self):
        subjects = await self.subjects_repo.find_all({})
        return subjects
    
    async def create_subject(self, subject_name: str):
        subject_id = await self.subjects_repo.create_one(
            {"name": subject_name}
        )
        return subject_id