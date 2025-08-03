class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                book.is_checked_out = True
        return book.is_checked_out

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                book.is_checked_out = False
                return
                

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_checked_out == False]
        for book in available_books:
            print(f"{book.title} by {book.author}")
