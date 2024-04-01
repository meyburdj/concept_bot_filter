import pytest
import os

from src import create_app


@pytest.fixture(scope="function")
def test_app():
    os.environ["APP_SETTINGS"] = "src.config.TestingConfig"
    app = create_app()

    with app.app_context():
        yield app

@pytest.fixture(scope="function")
def test_client(test_app):
    return test_app.test_client()

