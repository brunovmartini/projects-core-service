from datetime import datetime, timezone
from unittest.mock import Mock, patch

import pytest
from flask import Response
from werkzeug.exceptions import BadRequest, NotFound

from models.project import Project
from resources.request.project_request import ProjectRequest
from resources.response.project_response import ProjectResponse
from services.project.project_service import ProjectService


@pytest.fixture
def service(mock_repository):
    return ProjectService(repository=mock_repository)


@pytest.fixture
def fake_project():
    return Project(
        id=1,
        name="Test Project",
        subject="Testing",
        start_date='2025-10-29 14:22:11.949',
        due_date='2026-10-29 14:22:11.949',
        created_at=datetime.now(timezone.utc)
    )


@pytest.fixture
def fake_request():
    return ProjectRequest(
        name="New Project",
        subject="New Subject",
        start_date="2025-10-29 14:22:11.949",
        due_date="2026-10-29 14:22:11.949"
    )


def test_get_project_by_id_success(service, mock_repository, fake_project):
    mock_repository.get_by_id.return_value = fake_project

    result = service.get_project_by_id(1)
    assert result == fake_project
    mock_repository.get_by_id.assert_called_once_with(id=1)


def test_get_project_by_id_not_found(service, mock_repository):
    mock_repository.get_by_id.return_value = None

    with pytest.raises(NotFound):
        service.get_project_by_id(99)


@patch("services.project.project_service.is_invalid_request", return_value=False)
def test_create_project_success(mock_is_invalid, service, mock_repository, fake_project, fake_request):
    mock_repository.create.return_value = fake_project
    with patch("services.project.project_service.ProjectResponse.from_orm",
               return_value=ProjectResponse.model_validate({
                   "id": 1,
                   "name": fake_project.name,
                   "subject": fake_project.subject,
                   "start_date": "2025-10-29 14:22:11.949",
                   "due_date": "2026-10-29 14:22:11.949"
               })) as mock_response:
        result = service.create_project(fake_request)

        assert result["id"] == 1
        mock_repository.create.assert_called_once()
        mock_is_invalid.assert_called_once_with(fake_request)
        mock_response.assert_called_once()


@patch("services.project.project_service.is_invalid_request", return_value=True)
def test_create_project_invalid_request(mock_is_invalid, service, fake_request):
    with pytest.raises(BadRequest):
        service.create_project(fake_request)


def test_get_projects_success(service, mock_repository, fake_project):
    mock_repository.get_all.return_value = [fake_project]
    with patch("services.project.project_service.ProjectResponse.from_orm",
               return_value=ProjectResponse.model_validate({
                   "id": 1,
                   "name": fake_project.name,
                   "subject": fake_project.subject,
                   "start_date": "2025-10-29 14:22:11.949",
                   "due_date": "2026-10-29 14:22:11.949"
               })) as mock_response:
        result = service.get_projects()

        assert len(result) == 1
        assert result[0]["id"] == 1
        mock_repository.get_all.assert_called_once()
        mock_response.assert_called_once()


def test_get_project_success(service, fake_project):
    with patch.object(service, "get_project_by_id", return_value=fake_project), \
            patch("services.project.project_service.ProjectResponse.from_orm",
                  return_value=ProjectResponse.model_validate({
                      "id": 1,
                      "name": fake_project.name,
                      "subject": fake_project.subject,
                      "start_date": "2025-10-29 14:22:11.949",
                      "due_date": "2026-10-29 14:22:11.949"
                  })) as mock_response:
        result = service.get_project(1)

        assert result["id"] == 1
        service.get_project_by_id.assert_called_once_with(project_id=1)
        mock_response.assert_called_once()


@patch("services.project.project_service.is_invalid_request", return_value=False)
def test_update_project_success(mock_is_invalid, service, mock_repository, fake_project, fake_request):
    fake_project.update = Mock()
    mock_repository.update.return_value = fake_project
    with patch.object(service, "get_project_by_id", return_value=fake_project), \
            patch("services.project.project_service.ProjectResponse.from_orm",
                  return_value=ProjectResponse.model_validate({
                      "id": 1,
                      "name": fake_project.name,
                      "subject": fake_project.subject,
                      "start_date": "2025-10-29 14:22:11.949",
                      "due_date": "2026-10-29 14:22:11.949"
                  })) as mock_response:
        result = service.update_project(1, fake_request)

        assert result["id"] == 1
        fake_project.update.assert_called_once_with(fake_request.__dict__)
        mock_repository.update.assert_called_once_with(fake_project)
        mock_response.assert_called_once()


@patch("services.project.project_service.is_invalid_request", return_value=True)
def test_update_project_invalid_request(mock_is_invalid, service, fake_project, fake_request):
    with patch.object(service, "get_project_by_id", return_value=fake_project):
        with pytest.raises(BadRequest):
            service.update_project(1, fake_request)


def test_delete_project_success(service, mock_repository, fake_project):
    with patch.object(service, "get_project_by_id", return_value=fake_project):
        result = service.delete_project(1)

        assert isinstance(result, Response)
        assert result.status_code == 200
        assert "deleted" in result.get_data(as_text=True)
        mock_repository.delete.assert_called_once_with(fake_project)
