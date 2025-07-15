from model.tools.validation import *

class Customer:
    def __init__(self, custom_id, first_name, last_name, phone_number,address):
        self.custom_id = custom_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address


    def __repr__(self):
        return f"{self.__dict__}"

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
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        phone_number_validator(value)
        self._phone_number = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        address_validator(value)
        self._address = value