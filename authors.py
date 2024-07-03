from connect_mysql import connect_db
from mysql.connector import Error
from colorama import Fore, Back, Style

def add_authors(conn):
    try:
        cursor = conn.cursor()

        # collect user information to add to the database
        name = input("Please enter the author name: ")
        biography = input("Please enter author biography")

        new_author = (name,biography)

        query = "INSERT INTO authors(name,biography) VALUES (%s, %s)"

        # excecute the query
        cursor.execute(query, new_author) #prepares query with arguments
        conn.commit() #commits and sends changes to our database
        print(f"{new_author} User has been successfully added to the database!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
    pass

def view_authors(conn):
    try:
        cursor = conn.cursor()
        author_id = int(input("Please enter the author(id) by which you want to search"))
        author_search = (author_id,)
        query = "SELECT * from authors where id = %s"    
        cursor.execute(query,author_search)

        author_details = cursor.fetchall()

        if not author_details:
            print(f"Author with id {author_id} doesnt exist")
        else:
            for auth in author_details:
                print(Fore.GREEN)
                print(auth)
                print(Style.RESET_ALL)
                print("Author Search was succesful!")
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
    pass

def display_all_authors(conn):
    try:
        cursor = conn.cursor()
        # create a SQL query as a python string
        query = "SELECT * FROM authors"

        # Executing the query using the cursor
        cursor.execute(query)

        for row in cursor.fetchall():#fetchall returns data from the query execution as a list of tuples
            print(Fore.LIGHTBLUE_EX)
            print(row) #printing each row as a tuple
            print(Style.RESET_ALL)
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()

def remove_authors(conn):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        author_id = int(input("Which author(id) would you like to remove? "))

        author_to_remove = (author_id,)
        query_check = "select * FROM authors WHERE id = %s"
        cursor.execute(query_check, author_to_remove)
        author_info = cursor.fetchall()
     
        if not author_info:
            print("Cannot remove author , since the author with this id doesnt exist")
        else:
        # SQL Query
            query = "DELETE FROM authors WHERE id = %s"
            # executing the query
            cursor.execute(query, (author_id, ))
            conn.commit()
            print("Author Removed Successfully")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
    pass 

 