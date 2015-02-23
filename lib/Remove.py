from peewee import *


class Remove:
    test = ""
    def __init__(self, book_db):
        test = book_db.select()
        self.test = test

    def fun_test(self):
        return self.test


