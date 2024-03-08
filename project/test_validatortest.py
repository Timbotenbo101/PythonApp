import unittest   # The test framework
from .validator import validateContact

class Test_TestvalidateContact(unittest.TestCase):
    def test_validateContact_adds_error_if_field_empty(self):
        name = "ASD"
        email = "ASD@ASD.com"
        company = "ASD"
        phone = "123456779"

        nameEmptyError = 'Name is a required field'
        emailEmptyError = 'Email is a required field'
        companyEmptyError = 'Company is a required field'
        phoneEmptyError = 'Telephone is a required field'

        
        self.assertEqual(validateContact("", email, company, phone), [nameEmptyError])
        self.assertEqual(validateContact(name, "", company, phone), [emailEmptyError])
        self.assertEqual(validateContact(name, email, "", phone), [companyEmptyError])
        self.assertEqual(validateContact(name, email, company, ""), [phoneEmptyError])

    def test_validateContact_adds_error_if_email_invalid(self):
        name = "Valid Name"
        company = "Valid Company"
        phone = "123456779"

        expected = "Please enter a valid email address"

        self.assertEqual(validateContact(name, "A", company, phone), [expected])
        self.assertEqual(validateContact(name, "A@A", company, phone), [expected])
        self.assertEqual(validateContact(name, "A.com", company, phone), [expected])

    def test_validateContact_adds_error_if_invalid_phoneNumber(self):
        name = "Valid Name"
        company = "Valid Company"
        email = "email@email.com"

        expected = "Phone number must not contain letters or special characters"

        self.assertEqual(validateContact(name, email, company, "A123"), [expected])
        self.assertEqual(validateContact(name, email, company, "123A"), [expected])
        self.assertEqual(validateContact(name, email, company, "ABCD"), [expected])
        self.assertEqual(validateContact(name, email, company, "@!!!???/"), [expected])

    def test_validateContact_returns_empty_if_no_errors(self):
        name = "Valid Name"
        company = "Valid Company"
        email = "email@email.com"
        phone = "123142131"

        self.assertEqual(validateContact(name, email, company, phone), [])


if __name__ == '__main__':
    unittest.main()