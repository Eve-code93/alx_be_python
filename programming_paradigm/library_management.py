class Book:
    """Represents a book with a title, author, and availability status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""
    
    def __init__(self):
        self._books = []  # Private list to store Book objects
    
    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}")
                return
        print(f"Sorry, '{title}' is either not in the library or already checked out.")
    
    def return_book(self, title):
        """Finds a book by title and returns it if checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"'{title}' is either not in the library or was not checked out.")
    
    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books in the library.")
