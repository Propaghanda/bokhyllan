import hashlib
from lib.Database import Database


class Checksum:
    def __init__(self):
        pass

    def check(self, md5):
        db = Database()
        data = db.query("SELECT * FROM book WHERE md5=:md5", {"md5": md5}).fetchall()
        db.commit()

        if len(data)==0:
            return True
        else:
            return False

