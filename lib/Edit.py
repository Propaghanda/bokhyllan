from lib.Database import Database
from lib.EbookLib import EbookLib
import os

elib = EbookLib()


class Edit:
    success = 0

    def __init__(self):
        pass

    def epub(self, id):
        return None

    def new_epub(self, title, author, date, ISBN, ext, language, fname, imgext):  # used for uploading new ebook
        db = Database()
        try:
            self.move(fname, author, title, ext, imgext)
            self.success = 1
        except FileExistsError as error:
            return {"success": self.success, "message": str(error)}

        db.query('''INSERT INTO `book` (`author`, title, `date`, ISBN, ext, language) VALUES
                  (:author, :title, :date, :ISBN, :ext, :language)''',
                 {"author": author, "ISBN": ISBN, "title": title, "date": date, "language": language, "ext": ext})
        db.commit()
        return {"book": {"author": author, "ISBN": ISBN, "title": title, "date": date, "language": language, "ext": ext, "fname": fname},
                "success": self.success}

    def move(self, tempid, author, title, ext, imgext):
        book_path = 'books/'+author+"/"+title
        fname = author + " - " + title + "." + ext
        if not os.path.exists(book_path):  # Check if path exists before moving
            os.makedirs(book_path)
        os.rename('books/temp/'+tempid+"."+ext, book_path+"/"+fname)
        os.rename('books/temp/'+tempid+"."+imgext, book_path+"/cover."+imgext)

