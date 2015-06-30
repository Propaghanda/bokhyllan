import os
from lib.Database import Database


class Remove:
    ext = None
    title = None
    author = None
    error = None

    def __init__(self):
        pass

    def book(self, id):
        db = Database()
        query = db.query("SELECT * FROM book WHERE id=:id", {"id": id}).fetchone()

        self.author = query['author']
        self.title = query['title']
        self.ext = query['ext']

        try:
            os.remove('books/'+self.author+"/"+self.title+"/"+self.author+" - "+self.title+"."+self.ext)
            db.query("DELETE FROM book WHERE id=:id", {"id": id}).fetchone()
            db.commit()
            self.error = "Success"
        except WindowsError as e:
            self.error = str(e)+" Deleting from db anyways"
            db.query("DELETE FROM book WHERE id=:id", {"id": id}).fetchone()
            db.commit()





    def info(self):
        return self.error



