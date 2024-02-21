from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import Contacts

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, isAdmin=(current_user.userType == "Admin"))

@main.route('/contacts')
@login_required
def contacts():
    contacts = Contacts.query.all()
    contactsCount = len(contacts)
    return render_template('contacts.html', isAdmin=(current_user.userType == "Admin"), contacts=contacts, contactsCount=contactsCount)