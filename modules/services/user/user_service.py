from datetime import datetime, timezone
from typing import List, Any

from flask import Response
from werkzeug.exceptions import BadRequest, NotFound

from modules.helpers.helpers import is_invalid_request
from modules.models.user import User
from modules.repositories.user_repository import UserRepository
from modules.resources.request.user_request import CreateUserRequest
from modules.resources.response.user_response import UserResponse


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user_by_id(self, user_id: int) -> User | None:
        user = self.repository.get_by_id(id=user_id)
        if not user:
            raise NotFound(f'Not found user with id={user_id}.')
        return user

    def create_user(self, body: CreateUserRequest) -> dict[str, Any] | None:
        if is_invalid_request(body):
            raise BadRequest()

        user = self.repository.create(
            User(
                created_at=datetime.now(timezone.utc),
                email=body.email,
                password=body.password,
                username=body.username,
                user_type=body.user_type
            )
        )
        return UserResponse.from_orm(user).model_dump()

    def get_users(self) -> List[dict[str, Any] | None]:
        return [UserResponse.from_orm(user).model_dump() for user in self.repository.get_all()]

    def get_user(self, user_id: int) -> dict[str, Any] | None:
        user = self.get_user_by_id(user_id=user_id)
        return UserResponse.from_orm(user).model_dump()

    def update_user(self, user_id: int, body: CreateUserRequest) -> dict[str, Any] | None:
        user = self.get_user_by_id(user_id=user_id)

        if is_invalid_request(body):
            raise BadRequest()

        user.update(body.__dict__)
        user.updated_at = datetime.now(timezone.utc)

        user = self.repository.update(user)
        return UserResponse.from_orm(user).model_dump()

    def delete_user(self, user_id: int) -> Response | None:
        user = self.get_user_by_id(user_id=user_id)

        self.repository.delete(user)
        return Response(f'User with id={user_id} deleted.', status=200)
