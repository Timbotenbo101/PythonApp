import re

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
    