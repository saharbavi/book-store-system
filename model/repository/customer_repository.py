import sqlite3


class CustomerRepository:
    # connect/disconnect to database
    def connect(self):
        self.connection = sqlite3.connect("C:/Users/acer/Desktop/book-store-system/model/repository/bookstore_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    # buttons
    def save(self, customer):
        self.connect()
        self.cursor.execute(
            """
                INSERT INTO CUSTOMER
                    (custom_id,first_name,last_name,phone_number,address)
                values
                    (?,?,?,?,?)
             """,
            [customer.custom_id, customer.first_name, customer.last_name, customer.phone_number, customer.address]
        )
        self.disconnect(commit=True)

    def edit(self, customer):
        self.connect()
        self.cursor.execute(
            """
                UPDATE CUSTOMER SET first_name=?,last_name=?,phone_number=?,address=? where custom_id=?
                """,
            [customer.first_name, customer.last_name, customer.phone_number, customer.address,customer.custom_id]
        )
        self.disconnect(commit=True)

    def delete(self, custom_id):
        self.connect()
        self.cursor.execute("delete from CUSTOMER where custom_id=?", [custom_id])
        self.disconnect(commit=True)


    # search
    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMER")
        self.disconnect()


    def find_by_custom_id(self, custom_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMER WHERE custom_id=?", [custom_id])
        self.disconnect()
