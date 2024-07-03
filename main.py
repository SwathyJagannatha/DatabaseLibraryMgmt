# lastrowid -grabs the id from the last created item in our db
# from customers import add_customer, update_customer, remove_customer, get_customers, add_customer2, add_customer3
# from orders import add_order, update_order, remove_order, get_order_info

from colorama import Fore, Back, Style
from books import add_books,search_book,display_book,borrow_book,return_book,display_borrowed
from users import add_users,view_users,display_all_users,remove_users
from authors import add_authors,view_authors,display_all_authors,remove_authors
from connect_mysql import connect_db
from mysql.connector import Error

# adding conn as a parameter to the functions and then executing the queries within the functions
def book_operations():
    try:
        conn = connect_db()

        while True:
            response = input("""
            What would you like to do?
              1. Add a New Book
              2. Search for a Book
              3. Display Book
              4. Borrow a Book
              5. Return a book
              6. Display borrowed books
              7. Quit
              """) 
             #the update option for your book functionality only needs to update the availability

            if response == "1":
                add_books(conn)
            elif response == "2":
                search_book(conn)
            elif response == "3":
                display_book(conn)
            elif response == "4":
                borrow_book(conn)
            elif response == "5":
                return_book(conn)
            elif response == "6":
                display_borrowed(conn)
            elif response == "7":
                print("terminating books operations...")
                break
            else:
                print("Please enter a valid response...")
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            conn.close() #turns of the connection to the db

def user_operations():
  try:
    conn = connect_db()
    while True:
        response = input(f"""
             {Fore.RED}
             What would you like to do?
             1. Add a New User
             2. View User Details
             3. Display all Users
             4. Remove User
             5. Quit
             {Style.RESET_ALL}
             """)
        if response == "1":
            add_users(conn)
        elif response == "2":
            view_users(conn)
        elif response == "3":
            display_all_users(conn)
        elif response == "4":
            remove_users(conn)
        elif response == "5":
            print("terminating order operations...")
            break
        else:
            print("Please enter a valid response...")
  except Error as e:
        print(f"Error: {e}")

  finally:
        if conn and conn.is_connected():
            conn.close() #turns of the connection to the db

def author_operations():
  try:
    conn = connect_db()
    while True:
        response = input(f"""
             {Fore.RED}
             What would you like to do?
             1. Add a New Author
             2. View Author Details
             3. Display all Author
             4. Remove Author
             5. Quit
             {Style.RESET_ALL}
             """)
        if response == "1":
            add_authors(conn)
        elif response == "2":
            view_authors(conn)
        elif response == "3":
            display_all_authors(conn)
        elif response == "4":
            remove_authors(conn)
        elif response == "5":
            print("terminating order operations...")
            break
        else:
            print("Please enter a valid response...")
  except Error as e:
        print(f"Error: {e}")

  finally:
        if conn and conn.is_connected():
            conn.close() #turns of the connection to the db

def main():

    while True:
        print(f"""{Fore.GREEN}{Style.BRIGHT}Welcome to the Library Management System with Database Integration!{Style.RESET_ALL}""")
        response = input("1  User Operations \n2  Book Operations \n3. Author Operations\n4. Exit\n")
        if response == "1":
            user_operations()
        elif response == "2":
            book_operations()
        elif response == "3":
            author_operations()
        elif response == "4":
            print("Thanks for comin!")
            break

if __name__ == "__main__":
    main()

