from peewee import *
import os


class Remove:
    test = ""

    def __init__(self):
        pass

    def book(self, book_db, book_id):
        book = book_db.select(book_db.id(book_id))
        file = book.title + " - " + book.author + "." + book.ext
        os.remove('download/'+file)
        book.delete_instance()
        self.test = test

    def fun_test(self):
        return self.test


