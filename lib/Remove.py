import os
from lib.Database import Database
from lib.Book import Book


class Remove:
    ext = None
    title = None
    author = None
    error = None

    def __init__(self):
        pass

    def book(self, id):
        db = Database()
        book = Book(id)

        try:
            os.remove(book.full_path)
            os.remove(book.image)
            db.query("DELETE FROM book WHERE id=:id", {"id": id}).fetchone()
            db.commit()
            self.error = "Success"
        except WindowsError as e:
            self.error = str(e)+" Deleting from db anyways"
            db.query("DELETE FROM book WHERE id=:id", {"id": id}).fetchone()
            db.commit()


    def info(self):
        return self.error



