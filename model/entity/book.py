from model.tools.validation import *


class Book:
    def __init__(self, code, title, author, price, edition, publisher, number):
        self.code = code
        self.title = title
        self.author = author
        self.price = price
        self.edition = edition
        self.publisher = publisher
        self.number = number

    def __repr__(self):
        return f"{self.__dict__}"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        title_validator(value)
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        author_validator(value)
        self._author = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        price_validator(value)
        self._price = value

    @property
    def edition(self):
        return self._edition

    @edition.setter
    def edition(self, value):
        edition_validator(value)
        self._edition = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        publisher_validator(value)
        self._publisher = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        number_validator(value)
        self._number = value
