import re

# def user_validator:

def first_name_validator(first_name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", first_name):
        raise ValueError("Invalid name !!!")

def last_name_validator(last_name):
    pass

def phone_number_validator(phone_number):
    pass

def username_validator(username):
    pass

def password_validator(password):
    pass

def role_validator(role):
    pass

# def book_validator(book):

def title_validator(title):
    pass

def author_validator(author):
    pass

def price_validator(price):
    pass

def edition_validator(edition):
    pass

def publisher_validator(publisher):
    pass

def number_validator(number):
    pass



