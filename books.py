from connect_mysql import connect_db
from mysql.connector import Error
from datetime import date,datetime
from colorama import Fore, Back, Style
import re

def add_books(conn):
    try:
        cursor = conn.cursor()

        # collect customer information to add to the database
        title = input("Please enter the book title: ")

        if not re.fullmatch(r"[\w\s]+", title):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        
        author_id = input("Please enter author id")
        genre_id = input("Please enter genre id(not mandatory)" )
        isbn = input("Please enter book ISBN number")
        
        if not re.fullmatch(r"^\d(-?\d){6}$", isbn):
            print("\nInvalid Type Error. Please Enter Valid isbn(6 digits)\n")
            return
        
        publication_date = input("Enter the publication date")

        # creating the tuple that we will send over to the database
        # we set this to a tuple becuase the execute query method needs an iterable to match the position of values
        new_book = (title,author_id,genre_id,isbn,publication_date)

        # SQL Query to insert book information                  place holders for the data to be inserted
        query = "INSERT INTO books (title,author_id,genre_id,isbn,publication_date) VALUES (%s, %s, %s, %s ,%s)"

        # excecute the query
        cursor.execute(query, new_book) #prepares query with arguments
        conn.commit() #commits and sends changes to our database
        print(f"{new_book} Book has successfully been added to the database!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()

def search_book(conn):
     try:
        cursor = conn.cursor()

        user_ip = input("Enter the field by which you want to search a book(book_id, title, isbn)?").lower()
        # collect book information to add to the database
        if user_ip == "title":
            title_ip = input("Please enter the book title by which you want to search")
            if not re.fullmatch(r"[\w\s]+", title_ip):
                print("\nInvalid Type Error. Please Enter Valid Input\n")
                return

            title_search = (f"%{title_ip}%",)
            query = "SELECT * from books where title LIKE %s"    
            cursor.execute(query, title_search)

            book_details = cursor.fetchall()

            if not book_details:
                print(f"Book with title {title_ip} doesnt exist")
            else:
                for book in book_details:
                   print(Fore.BLUE)
                   print(f"""{Fore.BLUE}""")
                   print(book)
                   print("Book Search was succesful!")
                   print(Style.RESET_ALL)
            pass
        
        elif user_ip == "book_id":
            book_id = int(input("Please enter the book(id) by which you want to search"))
            book_search = (book_id,)
            query = "SELECT * from books where id = %s"    
            cursor.execute(query,book_search)

            book_details = cursor.fetchall()

            if not book_details:
                print(f"Book with id {book_id} doesnt exist")
            else:
                for book in book_details:
                    print(Fore.YELLOW)
                    print(book)
                    print("Book Search was succesful!")
                    print(Style.RESET_ALL)
            pass 
        
        elif user_ip == "isbn":
            input_id = input("Please enter the book ISBN by which you want to search")
            book_search = (input_id,)
            query = "SELECT * from books where isbn = %s"    
            cursor.execute(query,book_search)
            book_details = cursor.fetchall()

            if not book_details:
                print(f"Book with isbn {input_id} doesnt exist")
            else:
                for book in book_details:
                   print(Fore.MAGENTA)
                   print(book)
                   print("Book Search was succesful!")
                   print(Style.RESET_ALL)
            pass  

     except Error as e:
        print(f"Error encountered: {e}")

     finally:
        if conn and conn.is_connected():
            cursor.close()     
     pass

def display_book(conn):
    try:
        cursor = conn.cursor()

        query = """SELECT * FROM books"""
        
        # execute our query
        cursor.execute(query)

        # looping through results

        for book in cursor.fetchall():
            # Convert the datetime.date to a string
            book = list(book)
            book[5] = book[5].strftime('%Y-%m-%d')
            print(Fore.CYAN)
            print(tuple(book))
            print(Style.RESET_ALL)

    except Error as e:
        print(f"Error encountered: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()      
    pass

def borrow_book(conn):
    try:
        cursor = conn.cursor()

        # Get input from the user
        book_ip = input("Enter the book title you would like to borrow: ")  # e.g., "Harry Potter"
        user_ip = input("Enter your library ID: ")  # e.g., 1

        # Check if the book exists and is available
        query1 = "SELECT id, availability FROM books WHERE title = %s"
        cursor.execute(query1, (book_ip,))
        book_res = cursor.fetchone()

        if not book_res:
            print("Sorry, the book doesn't exist")
            return

        book_id, availability = book_res

        if not availability:
            print("Sorry, the book is not available")
            return 
        
        # Check if the user exists
        query2 = "SELECT id FROM users WHERE library_id = %s"
        cursor.execute(query2, (user_ip,))
        user_res = cursor.fetchone()

        if not user_res:
            print("Sorry! The specified user ID doesn't exist in the system!")
            return
        
        user_id = user_res[0]

        # Both book and user exist and the book is available
        print("Book and user are valid and present in the system")
        user_date = input("Enter the book borrow date (YYYY-MM-DD): ")
        borrow_date = date.fromisoformat(user_date)

        # SQL Query to insert borrowed book information
        query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
        cursor.execute(query, (user_id, book_id, borrow_date))

        # Mark the book as not available
        update_query = "UPDATE books SET availability = 0 WHERE id = %s"
        cursor.execute(update_query, (book_id,))
        conn.commit()  # Commit the transaction
        print(f"{book_ip} has successfully been borrowed!")

    except Error as e:
        print(f"Error encountered: {e}")
        conn.rollback()  # Rollback the transaction in case of an error

    finally:
        if conn and conn.is_connected():
            cursor.close()
            # conn.close()  # Do not close the connection here if you want to reuse it
    pass

def display_borrowed(conn):
    try:
        cursor = conn.cursor()

        query = """SELECT * FROM borrowed_books"""
        
        # execute our query
        cursor.execute(query)

        # looping through results
        for book in cursor.fetchall():
            book = list(book)
            if book[4] is not None:
                book[4] = book[4].strftime('%Y-%m-%d')
            print(Fore.BLUE)
            print(tuple(book))
            print(Style.RESET_ALL)

    except Error as e:
        print(f"Error encountered: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()      
    pass

def return_book(conn):
    try:
        cursor = conn.cursor(buffered=True)

        # Get input from the user
        book_ip = input("Enter the book title you would like to return: ")  # e.g., "Harry Potter"
        user_ip = input("Enter your library ID: ")  # e.g., 1

        # Check if the book exists
        query1 = "SELECT id, availability FROM books WHERE title = %s"
        cursor.execute(query1, (book_ip,))
        book_res = cursor.fetchone()

        if not book_res:
            print("Sorry, the book doesn't exist")
            return

        book_id, availability = book_res

        if availability:
            print("Sorry, the book has not been borrowed")
            return 

        # Check if the user exists
        query2 = "SELECT id FROM users WHERE library_id = %s"
        cursor.execute(query2, (user_ip,))
        user_res = cursor.fetchone()

        if not user_res:
            print("Sorry! The specified user ID doesn't exist in the system!")
            return
        
        user_id = user_res[0]

        # Check if this user has borrowed this book and it hasn't been returned yet
        query3 = """
        SELECT id, borrow_date 
        FROM borrowed_books 
        WHERE book_id = %s AND user_id = %s AND return_date IS NULL
        """
        cursor.execute(query3, (book_id, user_id))
        borrow_res = cursor.fetchone()

        if not borrow_res:
            print("No matching borrow record found for this book and user, or the book has already been returned.")
            return

        borrow_id, borrow_date = borrow_res

        # Both book and user exist and the book is currently borrowed
        print("Book and user are valid and present in the system")
        user_date = input("Enter the book return date (YYYY-MM-DD): ")
        return_date = date.fromisoformat(user_date)

        # SQL Query to update the return date in borrowed_books table
        query4 = "UPDATE borrowed_books SET return_date = %s WHERE id = %s"
        cursor.execute(query4, (return_date, borrow_id))

        # Mark the book as available
        update_query = "UPDATE books SET availability = 1 WHERE id = %s"
        cursor.execute(update_query, (book_id,))

        conn.commit()  # Commit the transaction
        print(f"{book_ip} has successfully been returned!")

    except Error as e:
        print(f"Error encountered: {e}")
        conn.rollback()  # Rollback the transaction in case of an error

    finally:
        if conn and conn.is_connected():
            cursor.close()
    pass