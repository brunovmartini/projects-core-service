from flask import Blueprint, request, Response
from flask_login import logout_user, login_required

from repositories.user_repository import UserRepository
from services.user.user_service import UserService
from settings.database import db

auth_apis = Blueprint('auth_apis', __name__)


@auth_apis.route("/login", methods=["POST"])
def login():
    return UserService(repository=UserRepository(db_session=db.session)).login(data=request.get_json())


@auth_apis.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return Response('Logged out successfully.', status=200)
