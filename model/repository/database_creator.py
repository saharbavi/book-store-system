import sqlite3

def create_database():
    # اتصال
    connection = sqlite3.connect("bookstore_db.sqlite")

    # ساخت جدول
    # عملیات ذخیره، ویرایش، حذف و انواع جستجو و گزارش
    cursor = connection.cursor()
    # #
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS USER (
                        user_id integer PRIMARY KEY autoincrement , 
                        first_name text not null , 
                        last_name text not null , 
                        username text not null unique ,
                        password text not null ,
                        role text not null ,
                        locked tinyint default 0 

                    )
                    """)
    # #
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS BOOK (
                        code integer PRIMARY KEY autoincrement ,
                        title text not null ,
                        author text not null ,
                        price integer not null ,
                        edition text not null ,
                        publisher text not null ,
                        number integer not null

                    )
                    """)
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS CUSTOMER (
                        custom_id integer PRIMARY KEY autoincrement , 
                        first_name text not null , 
                        last_name text not null , 
                        phone_number text not null ,
                        address text not null 

                    )
                    """)
    #
    #
    #
    connection.commit()
    #
    # # قطع اتصال
    cursor.close()
    connection.close()
