import sqlite3

class UserRepository:
    def save(self,user):
        connection = sqlite3.connect("bookstore_db.sqlite")
        cursor = connection.cursor()
        cursor.execute(
            """
                INSERT INTO USER
                    (user_id,first_name,last_name,username,password,role,locked)
                values
                    (%S,%S,%S,%S,%S,%S,%S)
            """,
            [user.user_id, user.first_name, user.last_name, user.username, user.password, user.role, user.locked]
         )
        connection.commit()
        cursor.close()
        connection.close()

    def edit(self, user):
        connection = sqlite3.connect("bookstore_db.sqlite")
        cursor = connection.cursor()
        cursor.execute(
            """
                UPDATE USER SET first_name=?,last_name=?,username=?,password=?,role=?,locked=? where user_id=?
                """,
            [user.first_name, user.last_name, user.username, user.password, user.role, user.locked, user.user_id]
        )
        connection.commit()
        cursor.close()
        connection.close()


    def delete(self, user_id):
        connection = sqlite3.connect("bookstore_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("delete from USER where user_id=?", [user_id])
        connection.commit()
        cursor.close()
        connection.close()



    def find_all(self):
        connection = sqlite3.connect("bookstore_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM USER")
        cursor.close()
        connection.close()

    def find_by_user_id(self, user_id):
        connection = sqlite3.connect("bookstore_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM USER WHERE user_id=?", [user_id])
        cursor.close()
        connection.close()

    def find_by_first_name_last_name(self, first_name,last_name):
        connection = sqlite3.connect("bookstore_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM USER WHERE first_name=? and last_name=?", [first_name,last_name])
        cursor.close()
        connection.close()

    def find_by_username(self, username):
        connection = sqlite3.connect("bookstore_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM USER WHERE username=?", [username])
        cursor.close()
        connection.close()

    def find_by_username_password(self, username,password):
        connection = sqlite3.connect("bookstore_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM USER WHERE username=? and password=?", [username,password])
        cursor.close()
        connection.close()
