from model.tools.validation import *

class User:
    def __init__(self, user_id, first_name, last_name, username,password,role,locked=False):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.role = role
        self.locked = locked


    def __repr__(self):
        return f"{self.__dict__}"

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        user_id_validation(value)
        self._user_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        first_name_validator(value)
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        last_name_validator(value)
        self._last_name = value


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        username_validator(value)
        self._username = value


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        password_validator(value)
        self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        role_validator(value)
        self._role = value