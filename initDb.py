from peewee import *
from datetime import date

db = SqliteDatabase('bok.db')

class Book(Model):
    title = CharField()
    author = CharField()
    date = DateField()
    ISBN = CharField()
    ext = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.


db.connect()

#db.create_table(Book)
#test = Book(title='asda', author='dfgdf', date=date(1923, 1, 14), ISBN='ASDGFA-234', ext='epub')
#test.save()
test = Book.get(Book.id == 2)