from connect_mysql import connect_db
from mysql.connector import Error
from colorama import Fore,Back
import re

def add_users(conn):
    try:
        cursor = conn.cursor()

        # collect customer information to add to the database
        name = input("Please enter the user name: ")
        if not re.fullmatch(r"[\w\s]+", name):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        
        library_id = input("Please enter your library id")
        if not re.fullmatch(r"^\d(-?\d){5}$", library_id):
            print("\nPlease Enter Valid library Id of 6 digits!\n")
            return
        
        # creating the tuple that we will send over to the database
        # we set this to a tuple becuase the execute query method needs an iterable to match the position of values
        new_user = (name,library_id)

        query = "INSERT INTO users(name,library_id) VALUES (%s, %s)"

        # excecute the query
        cursor.execute(query, new_user) #prepares query with arguments
        conn.commit() #commits and sends changes to our database
        print(f"{new_user} User has been successfully added to the database!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()

def view_users(conn):

    try:
        cursor = conn.cursor()
        user_id = int(input("Please enter the user(id) by which you want to search"))
        user_search = (user_id,)
        query = "SELECT * from users where id = %s"    
        cursor.execute(query,user_search)

        user_details = cursor.fetchall()

        if not user_details:
            print(f"User with id {user_id} doesnt exist")
        else:
            # for user in user_details:
            #     print(user)
            #     print("User Search was succesful!")

            for user in user_details:
                print(f"""             ---- User Details ----:
                        User-Id : {user[0]}
                        UserName : {user[1]}
                        Library-Id : {user[2]}
                """)
                

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
    pass

def display_all_users(conn):
    try:
        cursor = conn.cursor()

        # create a SQL query as a python string
        query = "SELECT * FROM users"

        # Executing the query using the cursor
        cursor.execute(query)

        user_details = cursor.fetchall()
        for user in user_details:
                print(f"""                 ---- User Details ----:
                        UserID : {user[0]}
                        UserName : {user[1]}
                        Library-Id : {user[2]}
                    """)
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            pass

def remove_users(conn):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        user_id = int(input("Which user(id) would you like to remove? "))

        user_to_remove = (user_id,)
        query_check = "select * FROM users WHERE id = %s"
        cursor.execute(query_check, user_to_remove)
        user_info = cursor.fetchall()
        
        if not user_info:
            print("Cannot remove the user ,since the user with this id doesn't exist")
        else:
        # SQL Query
            query = "DELETE FROM users WHERE id = %s"
            # executing the query
            cursor.execute(query, (user_id, ))
            conn.commit()
            print("User Removed Successfully")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
    pass 

 