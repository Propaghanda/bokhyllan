from lib.Database import Database
import shutil
import os


class Book:

    title = None
    author = None
    ext = None
    real_name = None
    full_path = None
    dir = None
    image = None

    def __init__(self, id):
        db = Database()
        query = db.query("SELECT * FROM book WHERE id=:id", {"id": id}).fetchone()

        self.author = query['author']
        self.title = query['title']
        self.ext = query['ext']
        self.real_name = self.author + " - " + self.title + "." + self.ext
        self.dir = 'books/'+self.author+"/"+self.title+"/"
        flist = os.listdir(self.dir)
        for item in flist:
            if 'cover' in item:
                self.image = self.dir+item
        #self.image = self.dir+"cover"
        self.full_path = self.dir+self.real_name


