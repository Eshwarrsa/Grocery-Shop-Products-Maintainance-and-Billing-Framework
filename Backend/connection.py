import mysql.connector as sql
from mysql.connector import Error
def connection():
    try:
        connect = sql.connect(
            username = "root",
            password = "Eshwarrsa@2001",
            database = "grocery",
            host     = "127.0.0.1"
        )

    except Error as e:
        print("Connection failed due to {e}")

    else:
        return connect