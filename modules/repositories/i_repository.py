from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T', bound='IRepository')
I = TypeVar('I', bound='IRepository')


class IRepository(Generic[T, I], ABC):

    @abstractmethod
    def get_all(self) -> list[T]:
        raise NotImplementedError("Method not implemented.")

    @abstractmethod
    def get_by_id(self, id: I) -> T | None:
        raise NotImplementedError("Method not implemented.")

    @abstractmethod
    def create(self, data: T) -> T:
        raise NotImplementedError("Method not implemented.")

    @abstractmethod
    def update(self, data: T) -> T:
        raise NotImplementedError("Method not implemented.")

    @abstractmethod
    def delete(self, data: T) -> None:
        raise NotImplementedError("Method not implemented.")
