# from model.repository.database_creator import *
import sqlite3

class UserRepository:
    # connect/disconnect to database
    def connect(self):
        self.connection = sqlite3.connect("C:/Users/acer/Desktop/book-store-system/model/repository/bookstore_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self,commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    #buttons
    def save(self,user):
        self.connect()
        self.cursor.execute(
            """
                INSERT INTO USER
                    (user_id,first_name,last_name,username,password,role,locked)
                values
                    (?,?,?,?,?,?,?)
            """,
            [user.user_id, user.first_name, user.last_name, user.username, user.password, user.role, user.locked]
         )
        self.disconnect(commit=True)

    def edit(self, user):
        self.connect()
        self.cursor.execute(
            """
                UPDATE USER SET first_name=?,last_name=?,username=?,password=?,role=?,locked=? where user_id=?
                """,
            [user.first_name, user.last_name, user.username, user.password, user.role, user.locked, user.user_id]
        )
        self.disconnect(commit=True)


    def delete(self, user_id):
        self.connect()
        self.cursor.execute("delete from USER where user_id=?", [user_id])
        self.disconnect(commit=True)


    #search-users
    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM USER")
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list

    def find_by_user_id(self, user_id):
        self.connect()
        self.cursor.execute("SELECT * FROM USER WHERE user_id=?", [user_id])
        user=self.cursor.fetchone()
        self.disconnect()
        return user

    def find_by_first_name_last_name(self, first_name,last_name):
        self.connect()
        self.cursor.execute("select * from USER where first_name like ? and last_name like ?", [first_name+"%",last_name+"%"])
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM USER WHERE username=?", [username])
        user = self.cursor.fetchone()
        self.disconnect()
        return user

    def find_by_username_password(self, username,password):
        self.connect()
        self.cursor.execute("SELECT * FROM USER WHERE username=? and password=?", [username,password])
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list
