import pytest
import json
from flask import Flask
from app import create_app
from app.models.user import User
from app.models import db


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_post_user_service(client):
    valid_user_data = {
        "username": "usuario000002",
        "email": "000002@gmail.com"
    }

    response = client.post('/users', json=valid_user_data)

    # Should return 201
    assert response.status_code == 201

    # should check if the response is align with the request
    data = json.loads(response.data)
    responseId = data["id"]
    assert data["email"] == valid_user_data["email"]
    assert data["username"] == valid_user_data["username"]

    # should check if it was saved
    user = User.query.filter_by(id=responseId).first()
    assert user is not None
    assert user.email == valid_user_data["email"]
