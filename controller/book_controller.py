from model.entity.book import Book
from model.repository.book_repository import BookRepository

class BookController:
    def save(self, code,title,author,price,edition,publisher,number):
        try:
            book = Book(code,title,author,price,edition,publisher,number)
            book_repo = BookRepository()
            book_repo.save(book)
            return True, f"book saved successfully {book}"
        except Exception as e:
            return False, f"error saving book : {e}"

    def edit(self, code,title,author,price,edition,publisher,number):
        try:
            book = Book(code, title, author, price, edition, publisher, number)
            book_repo = BookRepository()
            book_repo.edit(book)
            return True, f"book edited successfully {book}"
        except Exception as e:
            return False, f"error editing book : {e}"

    def delete(self, code):
        try:
            book_repo = BookRepository()
            book_repo.delete(code)
            return True, f"book removed successfully {code}"
        except Exception as e:
            return False, f"error removing book : {e}"

    # search-book

    def find_all(self):
        try:
            book_repo = BookRepository()
            return True, book_repo.find_all()
        except Exception as e:
            return False, f"error find all books : {e}"

    def find_by_code(self, code):
        try:
            book_repo = BookRepository()
            book = book_repo.find_by_code(code)
            if book is None:
                return True, []
            else:
                return True, [book]
        except Exception as e:
            return False, f"error find code : {code} error : {e}"

    def find_by_title_author(self, title,author):
        try:
            book_repo = BookRepository()
            return True, book_repo.find_by_title_author(title, author)
        except Exception as e:
            return False, f"error find title : {title} author : {author} error : {e}"


    def find_by_publisher(self, publisher):
        try:
            book_repo = BookRepository()
            book = book_repo.find_by_code(publisher)
            if book is None:
                return True, []
            else:
                return True, [book]
        except Exception as e:
            return False, f"error find publisher : {publisher} error : {e}"

    def find_by_edition(self, edition):
        try:
            book_repo = BookRepository()
            book = book_repo.find_by_code(edition)
            if book is None:
                return True, []
            else:
                return True, [book]
        except Exception as e:
            return False, f"error find edition : {edition} error : {e}"

    def find_by_price(self, price):
        try:
            book_repo = BookRepository()
            book = book_repo.find_by_code(price)
            if book is None:
                return True, []
            else:
                return True, [book]
        except Exception as e:
            return False, f"error find price : {price} error : {e}"