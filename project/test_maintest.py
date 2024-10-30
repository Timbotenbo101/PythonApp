import pytest
from flask import url_for
from project import app
from project.models import User, Contacts
from werkzeug.security import generate_password_hash
from flask_login import login_user

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def login_admin(client):
    client.post('/login', data=dict(email="admin@admin.com", password="Admin123"), follow_redirects=True)

@pytest.fixture
def login_user(client):
    client.post('/login', data=dict(email="test@test.com", password="Testing123"), follow_redirects=True)

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Contacts App' in response.data 

def test_profile_logged_in(client, login_user):
    response = client.get('/profile')
    assert response.status_code == 200
    assert b'Your Profile' in response.data 
    assert b'test@test.com' in response.data 

def test_profile_not_logged_in(client):
    response = client.get('/profile')
    assert response.status_code == 302
    assert b'Your Profile' not in response.data  
