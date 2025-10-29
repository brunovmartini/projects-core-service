from datetime import datetime, timezone
from modules.models.user import User
from modules.resources.request.user_request import CreateUserRequest
from modules.repositories.user_repository import UserRepository
from modules.helpers.helpers import is_invalid_request
from flask import Response
from modules.resources.response.user_response import UserResponse


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, body: CreateUserRequest):
        if is_invalid_request(body):
            return Response('Invalid request body.', status=400)

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

    def get_users(self):
        return [UserResponse.from_orm(user).model_dump() for user in self.repository.get_all()]

    def get_user(self, user_id: int):
        user = self.repository.get_by_id(id=user_id)
        if not user:
            return Response(f'Not found user with id={user_id}.', status=404)
        return UserResponse.from_orm(user).model_dump()

    def update_user(self, user_id: int, body: CreateUserRequest):
        user = self.repository.get_by_id(id=user_id)
        if not user:
            return Response(f'Not found user with id={user_id}.', status=404)

        if is_invalid_request(body):
            return Response('Invalid request body.', status=400)

        user.update(body.__dict__)
        user.updated_at = datetime.now(timezone.utc)

        user = self.repository.update(user)
        return UserResponse.from_orm(user).model_dump()

    def delete_user(self, user_id: int):
        user = self.repository.get_by_id(id=user_id)
        if not user:
            return Response(f'Not found user with id={user_id}.', status=404)

        self.repository.delete(user)
        return Response(status=200)
