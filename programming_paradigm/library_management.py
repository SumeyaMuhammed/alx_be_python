class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def checked_out(self):
        self._is_checked_out =True

    def returned(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

        

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, new_book):
        self._books.append(new_book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.checked_out()
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.returned()

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
            