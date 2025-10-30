from flask import Blueprint
from flask_pydantic import validate

from repositories.project_repository import ProjectRepository
from resources.request.project_request import ProjectRequest
from services.project.project_service import ProjectService
from settings.database import db

project_apis = Blueprint('/projects', __name__)


@project_apis.route('/', methods=['POST'])
@validate()
def create_project(body: ProjectRequest):
    return ProjectService(repository=ProjectRepository(db_session=db.session)).create_project(body=body)


@project_apis.route('/', methods=['GET'])
def get_projects():
    return ProjectService(repository=ProjectRepository(db_session=db.session)).get_projects()


@project_apis.route('/<int:project_id>', methods=['GET'])
def get_project(project_id: int):
    return ProjectService(repository=ProjectRepository(db_session=db.session)).get_project(project_id=project_id)


@project_apis.route('/<int:project_id>', methods=['PUT'])
@validate()
def update_project(project_id: int, body: ProjectRequest):
    return ProjectService(repository=ProjectRepository(db_session=db.session)).update_project(project_id=project_id, body=body)


@project_apis.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id: int):
    return ProjectService(repository=ProjectRepository(db_session=db.session)).delete_project(project_id=project_id)
