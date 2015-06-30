from lib.Database import Database
import shutil


class Download:

    title = None
    author = None
    ext = None
    fname = None
    real_name = None
    path = None

    def __init__(self):
        pass

    def get_file(self, id):
        db = Database()
        query = db.query("SELECT * FROM book WHERE id=:id", {"id": id}).fetchone()

        self.author = query['author']
        self.title = query['title']
        self.ext = query['ext']
        self.real_name = self.author + " - " + self.title + "." + self.ext
        self.fname = str(query['id'])+"."+self.ext
        self.path = 'books/'+self.author+"/"+self.title+"/"+self.real_name

