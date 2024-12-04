import pytest
from src.app import create_app
from src.config.database import db
from src.config.settings.environment import Environment

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Cria um cliente de teste"""
    api_key = Environment.API_KEY
    client = app.test_client()
    client.environ_base["HTTP_API_KEY"] = api_key
    return client
