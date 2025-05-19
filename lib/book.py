class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count
        self._is_checked_out = False

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            print("Title must be a string")
            return
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        if value <= 0:
            print("Page count must be a positive integer")
            return
        self._page_count = value

    @property
    def is_checked_out(self):
        return self._is_checked_out

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return "Book checked out"
        return "Book already checked out"

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return "Book returned"
        return "Book is not checked out"

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")