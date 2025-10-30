from unittest.mock import Mock

import pytest


@pytest.fixture
def mock_repository():
    return Mock()
