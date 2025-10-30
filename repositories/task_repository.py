from sqlalchemy.orm import Session
from typing_extensions import override

from models.task import Task
from repositories.i_repository import IRepository


class TaskRepository(IRepository[Task, int]):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_tasks_by_project(self, project_id: int) -> list[Task]:
        return self.db_session.query(Task).filter(Task.project_id == project_id).all()

    @override
    def create(self, data: Task) -> Task:
        self.db_session.add(data)
        self.db_session.commit()
        self.db_session.refresh(data)
        return data

    @override
    def get_all(self) -> list[Task]:
        raise NotImplementedError("Method not implemented.")

    @override
    def get_by_id(self, id: int) -> Task | None:
        raise NotImplementedError("Method not implemented.")

    @override
    def update(self, data: Task) -> Task | None:
        raise NotImplementedError("Method not implemented.")

    @override
    def delete(self, data: Task) -> None:
        raise NotImplementedError("Method not implemented.")
