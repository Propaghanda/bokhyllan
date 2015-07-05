from lib.Database import Database
from lib.EbookLib import EbookLib
import os

elib = EbookLib()


class Edit:
    success = 0
    lastid = None

    def __init__(self):
        pass

    def epub(self, id):
        return None

    def new_epub(self, book_list):  # used for uploading new ebook
        db = Database()

        db.query('''INSERT INTO `book` (`author`, title, `date`, ISBN, ext, language, md5) VALUES
                  (:author, :title, :date, :ISBN, :ext, :language, :md5)''',
                 {"author": book_list["creator"], "ISBN": book_list["identifier"], "title": book_list["title"], "date": book_list["date"],
                     "language": book_list["language"], "ext": book_list["ext"], "md5": book_list["md5"]})
        self.lastid = db._db_cur.lastrowid
        db.commit()
    
    def move(self, tempid, author, title, ext, imgext):
        book_path = 'books/'+author+"/"+title
        fname = author + " - " + title + "." + ext
        if not os.path.exists(book_path):  # Check if path exists before moving
            os.makedirs(book_path)
        os.rename('books/temp/'+tempid+"."+ext, book_path+"/"+fname)
        #os.rename('books/temp/'+tempid+"."+imgext, book_path+"/cover."+imgext)

