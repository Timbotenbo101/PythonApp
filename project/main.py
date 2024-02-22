from flask import Blueprint, redirect, render_template, request, flash, url_for
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

@main.route('/addcontact')
@login_required
def addcontact():
    return render_template('addContact.html')

@main.route('/addcontact', methods=['POST'])
@login_required
def addcontact_post():
    email = request.form.get('email')
    name = request.form.get('name')
    company = request.form.get('company')
    telephone = request.form.get('telephone')

    contact = Contacts.query.filter_by(email=email).first() # if this returns a contact, then the email already exists in database

    if contact: # if a user is found, we want to redirect back to signup page so user can try again
        flash('A contact with this email address already exists')
        return redirect(url_for('main.addcontact'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_contact = Contacts(email=email, name=name, company=company, phoneNumber=telephone)

    # add the new user to the database
    db.session.add(new_contact)
    db.session.commit()
    return redirect(url_for('main.contacts'))