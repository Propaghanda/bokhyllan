from peewee import *


class Upload:
    db = SqliteDatabase('bok.db')
    size = 0
    out = """<html>
            <body>
                myFile length: %s<br />
                myFile filename: %s<br />
                myFile mime-type: %s
            </body>
            </html>"""
    author = ""
    title = ""
    my_file = ""

    def __init__(self):
        self.test = 'test'

    def book(self, book_db, my_file, title, author):
        self.db.connect()
        self.my_file = my_file
        self.title = title
        self.author =  author

        ext = my_file.filename.split('.')[-1]
        with open(('books/' + title + " - " + author + "." + ext), 'wb') as f:
            while True:
                data = my_file.file.read(8192)
                if not data:
                    break
                f.write(data)
                self.size += len(data)

        my_book = book_db.create(title=title, author=author, location=ext)
        my_book.save()

    def info(self):
        return self.out % (self.size, self.my_file.filename, self.my_file.content_type)