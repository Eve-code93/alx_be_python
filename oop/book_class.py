# book_class.py

class Book:
    """A class representing a book with its title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initialize a new Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method called when the instance is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an unambiguous string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
