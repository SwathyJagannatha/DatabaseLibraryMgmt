In this project, you will integrate a MySQL database with Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in database integration, SQL, and Python.

Integration with the "Library Management System" Project from Module 4 (OOP):

For this project, you will build upon the foundation laid in "Module 4: Python Object-Oriented Programming (OOP)." The object-oriented structure and classes you developed in that module will serve as the core framework for the Library Management System. You will leverage the classes such as Book, User, Author,  that you previously designed, extending their capabilities to integrate seamlessly with the MySQL database. THIS CAN BE DONE FUNCTIONALLY. (with functions not OOP)

Enhanced User Interface (UI) and Menu:

Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system. <div class="oc-markdown-custom-container oc-markdown-activatable" contenteditable="false" data-value="``` Welcome to the Library Management System with Database Integration!
Main Menu:

Book Operations
User Operations
Author Operations
Quit "> Welcome to the Library Management System with Database Integration!

Main Menu:

Book Operations
User Operations
Author Operations
Quit ```

Book Operations: <div class="oc-markdown-custom-container oc-markdown-activatable" contenteditable="false" data-value="``` 

Book Operations:

Add a new book
Borrow a book
Return a book
Search for a book
User Operations: <div class="oc-markdown-custom-container oc-markdown-activatable" contenteditable="false" data-value="``` User Operations:
Add a new user
View user details
Display all users 

Author Operations: 

Add a new author
View author details
Display all authors 


Database Integration with MySQL:

Integrate a MySQL database into the Library Management System to store and retrieve data related to books, users, authors, and genres.
Design and create the necessary database tables to represent these entities. You will align these tables with the object-oriented structure from the previous project.
Establish connections between Python and the MySQL database for data manipulation, enhancing the persistence and scalability of your Library Management System.
Data Definition Language Scripts:

Create the necessary database tables for the Library Management System. For instance:
Books Table:
Welcome to the Library Management System with Database Integration! **** Main Menu: 1. Book Operations 2. User Operations 3. Author Operations 4. Genre Operations 5. Quit

Database Connection:

Establish a connection to the MySQL database using the mysql-connector-python library.
Create a database cursor to execute SQL queries. Functions for Data Manipulation:
Create functions for adding new books, users, authors, and genres to the database.
Implement functions for updating book availability, marking books as borrowed or returned.
Develop functions for searching books by book_id, title, author, or genre.
Define functions for displaying lists of books, users, authors
Implement functions for user registration and viewing user details. User Interface Functions:
Create a user-friendly command-line interface (CLI) with clear menu options.
Implement functions to handle user interactions using the input() function.
Validate user input using regular expressions (regex) to ensure proper formatting. Error Handling:
Use try, except, else, and finally blocks to manage errors gracefully.
Handle exceptions related to database operations, input validation, and other potential issues.
Provide informative error messages to guide users. Clean Code Principles:
Use meaningful variable and function names that convey their purpose.
Write clear comments and docstrings to explain the functionality of functions and classes.
Follow PEP 8 style guidelines for code formatting and structure.
Ensure proper indentation and spacing for readability. Modular Design:
Organize code into separate modules to promote modularity and maintainability.
Create distinct modules for database operations, user interactions, error handling, and core functionalities. 
