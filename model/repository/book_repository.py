import sqlite3

class BookRepository:
    #connect/disconnect to database
    def connect(self):
        self.connection = sqlite3.connect("C:/Users/acer/Desktop/book-store-system/model/repository/bookstore_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()
    #buttons
    def save(self,book):
        self.connect()
        self.cursor.execute(
            """
                INSERT INTO BOOK
                    (code,title,author,price,edition,publisher,number)
                values
                    (?,?,?,?,?,?,?)
             """,
              [book.code,book.title,book.author,book.price,book.edition,book.publisher,book.number]
        )
        self.disconnect(commit=True)

    def edit(self, book):
        self.connect()
        self.cursor.execute(
            """
                UPDATE BOOK SET title=?,author=?,price=?,edition=?,publisher=?,number=? where code=?
                """,
            [book.title,book.author,book.price,book.edition,book.publisher,book.number,book.code]
        )
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute("delete from BOOK where code=?", [code])
        self.disconnect(commit=True)


    #search-book
    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOK")
        book_list = self.cursor.fetchall()
        self.disconnect()
        return book_list

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOK WHERE code=?", [code])
        book=self.cursor.fetchone()
        self.disconnect()
        return book

    def find_by_title_author(self, title, author):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOK WHERE title like ? and author like ?" , [title+"%", author+"%"])
        book_list = self.cursor.fetchall()
        self.disconnect()
        return book_list

    def find_by_publisher(self, publisher):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOK WHERE publisher=?", [publisher])
        book = self.cursor.fetchone()
        self.disconnect()
        return book

    def find_by_edition(self, edition):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOK WHERE edition=?", [edition])
        book = self.cursor.fetchone()
        self.disconnect()
        return book

    def find_by_price(self, price):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOK WHERE price=?", [price])
        book = self.cursor.fetchone()
        self.disconnect()
        return book