from lib.Database import Database
from lib.Save import Save
from lib.Book import Book
import os



class Edit:
    success = 0
    lastid = None

    def __init__(self):
        pass

    def epub(self, id):
        return None

    def new(self, fname,  book_list):  # used for uploading new ebook
        save = Save()
        db = Database()

        db.query('''INSERT INTO `book` (`author`, title, `date`, ISBN, ext, language, md5) VALUES
                  (:author, :title, :date, :ISBN, :ext, :language, :md5)''',
                 {"author": book_list["creator"], "ISBN": book_list["identifier"], "title": book_list["title"], "date": book_list["date"],
                     "language": book_list["language"], "ext": book_list["ext"], "md5": book_list["md5"]})
        self.lastid = db._db_cur.lastrowid
        db.commit()
        save.move(fname, Book(self.lastid))
