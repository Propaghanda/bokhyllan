from lib.Database import Database
import os


class Edit:

    def __init__(self):
        pass

    def epub(self, id):
        return None

    def new_epub(self, title, author, date, ISBN, ext, language, fname):  # used for uploading new ebook
        db = Database()
        self.move(fname, author, title, ext)
        db.query('''INSERT INTO `book` (`author`, title, `date`, ISBN, ext, language) VALUES
                  (:author, :title, :date, :ISBN, :ext, :language)''',
                 {"author": author, "ISBN": ISBN, "title": title, "date": date, "language": language, "ext": ext})
        db.commit()
        return {"author": author, "ISBN": ISBN, "title": title, "date": date, "language": language, "ext": ext, "fname": fname}

    def move(self, file, author, title, ext):
        book_path = 'books/'+author+"/"+title
        fname = author + " - " + title + "." + ext
        if not os.path.exists(book_path):  # Check if path exists before moving
            os.makedirs(book_path)
        os.rename('books/temp/'+file, book_path+"/"+fname)

