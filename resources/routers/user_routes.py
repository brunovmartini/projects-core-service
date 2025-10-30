from flask import Blueprint
from flask_pydantic import validate

from decorators.decorators import manager_required
from repositories.user_repository import UserRepository
from resources.request.user_request import CreateUserRequest, UpdateUserRequest
from services.user.user_service import UserService
from settings.database import db

user_apis = Blueprint('user_apis', __name__)


@user_apis.route('/', methods=['POST'])
@validate()
@manager_required
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
@manager_required
def update_user(user_id: int, body: UpdateUserRequest):
    return UserService(repository=UserRepository(db_session=db.session)).update_user(user_id=user_id, body=body)


@user_apis.route('/<int:user_id>', methods=['DELETE'])
@manager_required
def delete_user(user_id: int):
    return UserService(repository=UserRepository(db_session=db.session)).delete_user(user_id=user_id)
