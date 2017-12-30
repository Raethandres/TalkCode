from ..app.extensions import db as _db
from ..app import create_app
from ..app.config import TestConfig

from factories import UserFactory

import pytest

@pytest.fixture
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture
def user(db):
    """A user for the tests."""
    class User():
        def get(self):
            user = UserFactory(password='myprecious')
            db.session.commit()
            return user
    return User()