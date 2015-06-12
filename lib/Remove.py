from peewee import *
import os


class Remove:
    ad = []
    out = """<html>
            <body>
                myFile length: %s<br />
                myFile filename: %s<br />
            </body>
            </html>"""

    def __init__(self):
        pass

    def book(self, book_db, book_id):
        self.book_id = book_id 
        book = book_db.get(book_db.id == 5)
        #del_file = book.title + " - " + book.author + "." + book.ext
        #os.remove('books/'+del_file)
        #book.delete_instance()

    def info(self):
        return (str(self.book)) 


