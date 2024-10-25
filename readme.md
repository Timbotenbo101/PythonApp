# Contacts App

The contacts app has been built to provide you with a way of managing all of your contacts in one place.


# Developer set up

##  Requirements

A list of packages that are required to run the contacts app locally has been included in **requirements.txt**

## Database

Although an existing database file has been included with the code, the database will also be set up from scratch upon running the application if it does not yet exist.

## Admin User

As it should not be possible for an unauthorised user to sign up as admin, an admin user is instead seeded on initial database creation with the following credentials:
  
- **Email:** admin@admin.com
- **Password:** CONTACT ADMIN FOR DETAILS


# System

## Sign Up

Using the **Sign Up** button at the top of the page, you can fill out your credentials to create a basic user.
The email address entered must be unique, otherwise you will not be allowed to create the account

## Log in

After signing up, click the **Log in** button to enter your credentials and gain access to the system


## Profile

The **Profile** button will provide you with a view of the currently logged in user's details

## Contacts

### View Contacts

Clicking **Contacts** will display a table containing all of the existing contacts in the database.

### Add Contacts

Both admins and regular users will be able to see an **Add Contact** button above the contacts table. This will take you to a form where you can enter details for a new contact. These fields are validated and will return errors if left empty/formatted incorrectly

### Edit Contacts

Both admins and regular users will be able to see an **Edit** button in the **Actions** column of the contacts table. This takes you to a form where you can review and update the details for an existing contact. This page uses the same validation rules as the add contact form.

### Delete Contacts

*Only* admin users  will be able to see a **Delete** button in the **Actions** column of the contacts table. This takes you to a confirmation page where you can review the contacts details and either confirm the deletion, or cancel and return to the main contacts view.

