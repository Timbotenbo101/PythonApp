import pytest
from .validator import validateContact

def test_validateContact_adds_error_if_field_empty():
    name = "ASD"
    email = "ASD@ASD.com"
    company = "ASD"
    phone = "123456779"

    nameEmptyError = 'Name is a required field'
    emailEmptyError = 'Email is a required field'
    companyEmptyError = 'Company is a required field'
    phoneEmptyError = 'Telephone is a required field'

    assert validateContact("", email, company, phone) == [nameEmptyError]
    assert validateContact(name, "", company, phone) == [emailEmptyError]
    assert validateContact(name, email, "", phone) == [companyEmptyError]
    assert validateContact(name, email, company, "") == [phoneEmptyError]

def test_validateContact_adds_error_if_email_invalid():
    name = "Valid Name"
    company = "Valid Company"
    phone = "123456779"

    expected = "Please enter a valid email address"

    assert validateContact(name, "A", company, phone) == [expected]
    assert validateContact(name, "A@A", company, phone) == [expected]
    assert validateContact(name, "A.com", company, phone) == [expected]

def test_validateContact_adds_error_if_invalid_phoneNumber():
    name = "Valid Name"
    company = "Valid Company"
    email = "email@email.com"

    expected = "Phone number must not contain letters or special characters"

    assert validateContact(name, email, company, "A123") == [expected]
    assert validateContact(name, email, company, "123A") == [expected]
    assert validateContact(name, email, company, "ABCD") == [expected]
    assert validateContact(name, email, company, "@!!!???/") == [expected]

def test_validateContact_returns_empty_if_no_errors():
    name = "Valid Name"
    company = "Valid Company"
    email = "email@email.com"
    phone = "123142131"

    assert validateContact(name, email, company, phone) == []