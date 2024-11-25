DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        db.read # Ensure the file exists

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # Append the book's title and author to the database file
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    title, author.append(DATABASE_FILE)

def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # Implement logic to search for a book in the database file
    title = input("Enter the title to search for: ")
    if title in DATABASE_FILE:
        return {title}
    else:
        None

def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # Read all books from the database file and return them as a list of dictionaries
    for books in DATABASE_FILE:
        if books in DATABASE_FILE:
            return books
        else:
            return "No books in the library" 
        
    # with open(DATABASE_FILE, 'r') as db:
    #     db.read
    
