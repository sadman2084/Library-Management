from tkinter import Tk, Label, Entry, Button, Text

class Library:
    """A class representing a library with book management functionalities."""

    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book_title):
        self.books.append(book_title)
        self.no_of_books += 1

    def show_books(self):
        book_list = "\n".join(self.books)
        return f"Total number of books: {self.no_of_books}\n\n{book_list}"

class LibraryGUI:
    """A class representing a simple GUI for the library."""

    def __init__(self, library):
        self.library = library
        self.window = Tk()
        self.window.title("Library Management")

        self.num_books_label = Label(self.window, text="Number of Books:")
        self.num_books_entry = Entry(self.window)

        self.add_book_button = Button(self.window, text="Add Book", command=self.add_book)
        self.show_books_button = Button(self.window, text="Show Books", command=self.show_books)

        self.book_list_text = Text(self.window, height=10, width=50)

        self.place_widgets()

    def place_widgets(self):
        """Arranges the GUI widgets on the window."""
        self.num_books_label.grid(row=0, column=0)
        self.num_books_entry.grid(row=0, column=1)

        self.add_book_button.grid(row=1, columnspan=2)
        self.show_books_button.grid(row=2, columnspan=2)

        self.book_list_text.grid(row=3, columnspan=2)

    def add_book(self):
        """Gets book title from entry and adds it to the library."""
        book_title = self.num_books_entry.get()
        self.library.add_book(book_title)
        self.num_books_entry.delete(0, "end")  

    def show_books(self):
        """Updates the text box with the library information."""
        book_info = self.library.show_books()
        self.book_list_text.delete("1.0", "end")
        self.book_list_text.insert("1.0", book_info)

    def run(self):
        """Starts the main event loop for the GUI."""
        self.window.mainloop()

if __name__ == "__main__":
    library = Library()
    gui = LibraryGUI(library)
    gui.run()
