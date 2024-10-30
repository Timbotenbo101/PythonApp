from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SECRET_KEY'] = 'contactsflaskapplication123'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from . import models

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

with app.app_context():
    db.create_all()
    if not User.query.filter(User.email == 'admin@admin.com').first():
        admin = User(
            email='admin@admin.com',
            password=generate_password_hash('Admin123'),
            name='Admin User',
            userType='Admin'
        )
        user = User(
            email='test@test.com',
            password=generate_password_hash('Testing123'),
            name='Test User',
            userType='User'
        )
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()