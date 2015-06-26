import os
import sqlite3

class Remove:
    db = sqlite3.connect('bok.db', check_same_thread=False)
    db.row_factory = sqlite3.Row
    sth = db.cursor()
    out = """<html>
            <body>
                myFile length: %s<br />
                myFile filename: %s<br />
            </body>
            </html>"""

    def __init__(self):
        pass

    def book(self, book_db, book_id):
        self.db.connect()
        test = book_db.get(book_db.id == 5)
        #del_file = book.title + " - " + book.author + "." + book.ext
        #os.remove('books/'+del_file)
        #book.delete_instance()
        return test

    def info(self):
        return self.test()


