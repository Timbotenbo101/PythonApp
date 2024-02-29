import re
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
    return render_template('profile.html')

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

    errors = validateContact(name,email,company,telephone)

    contact = Contacts.query.filter_by(email=email).first() # if this returns a contact, then the email already exists in database

    if contact: # if a user is found, we want to redirect back to signup page so user can try again
        errors.append('A contact with this email address already exists')
    
    if len(errors) > 0:
        for error in errors:
            # flash all validation messages ready for display when returning to form
            flash(error)
        return redirect(url_for('main.addcontact'))
    
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_contact = Contacts(email=email, name=name, company=company, phoneNumber=telephone)

    # add the new user to the database
    db.session.add(new_contact)
    db.session.commit()
    flash('Successfully added contact')
    return redirect(url_for('main.contacts'))

@main.route('/editcontact/<int:contact_id>')
@login_required
def editcontact(contact_id):
    contact = Contacts.query.filter_by(id=contact_id).first()
    return render_template('editContact.html', contact=contact)

@main.route('/editcontact', methods=['POST'])
@login_required
def editcontact_post():
    id = request.form.get('id')
    email = request.form.get('email')
    name = request.form.get('name')
    company = request.form.get('company')
    telephone = request.form.get('telephone')

    contact = Contacts.query.filter_by(id = id).first()
    
    errors = validateContact(name,email,company,telephone)

    duplicateContact = Contacts.query.filter(id != id, email == email).first() # if this returns a contact, then the email already exists in database

    if duplicateContact: # redirect back if there is a separate contact with matching email address
        errors.append('Another contact with this email address already exists')
    
    if len(errors) > 0:
        for error in errors:
            # flash all validation messages ready for display when returning to form
            flash(error)
        return render_template('editContact.html', contact=contact)

    # update contact data and commit
    contact.email = email
    contact.name = name
    contact.company = company
    contact.phoneNumber = telephone
    db.session.commit()
    flash('Successfully updated contact')
    return redirect(url_for('main.contacts'))

@main.route('/deletecontact/<int:contact_id>')
@login_required
def deletecontact(contact_id):
    contact = Contacts.query.filter_by(id=contact_id).first()
    return render_template('deleteContact.html', contact=contact)

@main.route('/confirmdelete/<int:contact_id>')
@login_required
def confirmdelete(contact_id):
    contact = Contacts.query.filter_by(id=contact_id).first()
    db.session.delete(contact)
    db.session.commit()
    flash('Successfully deleted contact')
    return redirect(url_for('main.contacts'))

def validateContact(name, email, company, telephone):
    errors = []
    # Server side validation to protect against users editing the html before submission
    if (len(str.strip(email)) == 0): 
        errors.append('Email is a required field')
    else:
        email_validate_pattern = r"^\S+@\S+\.\S+$"
        if not re.match(email_validate_pattern, email):
            errors.append("Please enter a valid email address")
            
    if (len(str.strip(name)) == 0):
        errors.append('Name is a required field')
    if (len(str.strip(company)) == 0): 
        errors.append('Company is a required field')

    if (len(str.strip(telephone)) == 0): 
        errors.append('Telephone is a required field')
    else:
        validNumber = telephone.isnumeric()
        if (validNumber == False):
            errors.append('Phone number must not contain letters or special characters')

    return errors
    
    