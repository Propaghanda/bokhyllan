from peewee import *

db = SqliteDatabase('../bok.db')

class Book(Model):
    title = CharField()
    author = CharField()
    date = DateField()
    ISBN = CharField()
    ext = CharField()

    class Meta:
        database = db
