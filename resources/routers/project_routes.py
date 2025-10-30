from flask import Blueprint
from flask_pydantic import validate

from repositories.project_repository import ProjectRepository
from repositories.task_repository import TaskRepository
from resources.request.project_request import ProjectRequest
from resources.request.task_request import TaskRequest
from services.project.project_service import ProjectService
from services.task.task_service import TaskService
from settings.database import db
from werkzeug.exceptions import NotFound

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


@project_apis.route('/<int:project_id>/tasks', methods=['POST'])
@validate()
def create_task(project_id: int, body: TaskRequest):
    if not ProjectService(repository=ProjectRepository(db_session=db.session)).get_project(project_id=project_id):
        raise NotFound(f'Not found project with id={project_id}.')
    return TaskService(repository=TaskRepository(db_session=db.session)).create_task(project_id=project_id, body=body)


@project_apis.route('/<int:project_id>/tasks', methods=['GET'])
def get_tasks_by_project(project_id: int):
    if not ProjectService(repository=ProjectRepository(db_session=db.session)).get_project(project_id=project_id):
        raise NotFound(f'Not found project with id={project_id}.')
    return TaskService(repository=TaskRepository(db_session=db.session)).get_tasks_by_project(project_id=project_id)
