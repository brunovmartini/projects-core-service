from typing_extensions import override

from sqlalchemy.orm import Session, joinedload

from modules.repositories.i_repository import IRepository
from modules.models.user import User


class UserRepository(IRepository[User, int]):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    @override
    def create(self, data: User) -> User:
        self.db_session.add(data)
        self.db_session.commit()
        self.db_session.refresh(data)
        return data

    @override
    def get_all(self) -> list[User]:
        return self.db_session.query(User).all()

    @override
    def get_by_id(self, id: int) -> User | None:
        return self.db_session.query(User).options(joinedload(User.type)).filter(User.id == id).first()

    @override
    def update(self, data: User) -> User | None:
        self.db_session.commit()
        return data

    @override
    def delete(self, data: User) -> None:
        self.db_session.delete(data)
        self.db_session.commit()
