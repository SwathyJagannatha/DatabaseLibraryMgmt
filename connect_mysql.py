import mysql.connector
from mysql.connector import Error # - tells us if there any errors related to our connection

# connect() - collect information about our database through the sql server
# db_name, password, localhost - location or address of the db
# cursor() - allow to run sql statements in python
# exceute() - running the sql statements, fetchall() - grabbing sql information and using it in python

# connecting to the database 


def connect_db():
    # db connection variables
    db_name = "e_library_db"
    user = "root"
    password = "Swa123sweet@" # PLEASE CHANGE YOUR PASSWORD
    host = "localhost"
# attempt to connect to our database
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        # check if the connection is successful
        if conn.is_connected():
            print("Connected to MySQL Database successfully")
            return conn
    except Error as e:
        print(f"Error: {e}")

    # finally: #succesfully tested and closed out
    #     # closing the connection
    #     if conn and conn.is_connected():
    #         conn.close()
    #         print("MySql Connection is closed.")

connect_db()
