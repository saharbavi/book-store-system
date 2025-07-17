import re

def user_id_validation(user_id):
    pass

def first_name_validator(first_name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", first_name):
        raise ValueError("Invalid first name !!!")

def last_name_validator(last_name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", last_name):
        raise ValueError("Invalid last name !!!")

def phone_number_validator(phone_number):
    if not re.match(r"^(09|\+989)\d{9}$", phone_number):
        raise ValueError("Invalid phone number !!!")

def username_validator(username):
    if not re.match(r"^[A-Za-z][A-Za-z0-9_]{7,29}$", username):
        raise ValueError("Invalid username !!!")

def password_validator(password):
    if not re.match(r"^[A-Za-z\d_]{7,29}$", password):
        raise ValueError("Invalid password !!!")

def role_validator(role):
    pass

def title_validator(title):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", title):
        raise ValueError("Invalid title !!!")

def author_validator(author):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", author):
        raise ValueError("Invalid author !!!")

def price_validator(price):
    pass

def edition_validator(edition):
    pass

def publisher_validator(publisher):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", publisher):
        raise ValueError("Invalid publisher !!!")

def number_validator(number):
    pass

def address_validator(address):
    #smaple:tehran-iran
    if not re.match(r"^[\w\s\-]{10,100}$", address):
        raise ValueError("Invalid address !!!")




