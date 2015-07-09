import hashlib
import mimetypes
from lib.Checksum import Checksum
from lib.Upload import Upload


class UploadView:
    info = None


    def __init__(self):
        self.info = {}
        pass

    def hashcheck(self, my_file):
        data = my_file.file.read()
        md5 = hashlib.md5(data).hexdigest()
        checksum = Checksum()
        if checksum.check(md5):
            my_file.file.seek(0)
            upload = Upload()
            upload.ebook(my_file, md5)
            upload.info["md5"] = md5
            self.info = upload.info
        else:
            self.info["status"] = "Book already exists, skipping"
