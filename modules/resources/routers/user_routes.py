from flask import Blueprint
from flask_pydantic import validate

from modules.repositories.user_repository import UserRepository
from modules.resources.request.user_request import CreateUserRequest, UpdateUserRequest
from modules.services.user.user_service import UserService
from modules.settings.database import db

user_apis = Blueprint('/users', __name__)


@user_apis.route('/', methods=['POST'])
@validate()
def create_user(body: CreateUserRequest):
    return UserService(repository=UserRepository(db_session=db.session)).create_user(body=body)


@user_apis.route('/', methods=['GET'])
def get_users():
    return UserService(repository=UserRepository(db_session=db.session)).get_users()


@user_apis.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    return UserService(repository=UserRepository(db_session=db.session)).get_user(user_id=user_id)


@user_apis.route('/<int:user_id>', methods=['PUT'])
@validate()
def update_user(user_id: int, body: UpdateUserRequest):
    return UserService(repository=UserRepository(db_session=db.session)).update_user(user_id=user_id, body=body)


@user_apis.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    return UserService(repository=UserRepository(db_session=db.session)).delete_user(user_id=user_id)
