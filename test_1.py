import pytest
from app import app as flask_app

@pytest_.fixture
def app():
    yield flask_app

@pytest_.fixture
def client(app):
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

def test_post_name(client):
    response = client.post('/', data={'name': 'KUBA'})
    assert response.status_code == 200
    assert b'WITAJ KUBA' in response.data
    