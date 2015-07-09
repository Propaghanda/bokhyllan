from lib.EbookLib import EbookLib
from lib.Edit import Edit
from lib.Book import Book
from lib.Save import Save
from lib.Mimetype import Mimetype
import random


class Upload:
    size = 0
    filename = None
    tempid = None
    info = None
    md5 = None

    def __init__(self):
        self.info = {}
        pass

    def ebook(self, my_file, md5):
        elib = EbookLib()
        save = Save()
        edit = Edit()
        mime = Mimetype()
        self.tempid = str(random.randint(1, 1000))
        ext = my_file.filename.split('.')[-1]
        self.filename = 'books/temp/'+self.tempid + "." + ext
        self.info["content_type"] = str(my_file.content_type)
        m = mime.get_type(my_file.file.read())
        self.info["ct"] = str(m)

        if m == 'application/epub+zip':
            my_file.file.seek(0)
            self.write(my_file)
            elib.epub(self.filename)
            elib.res["md5"] = md5
            edit.new(self.filename, elib.res)
            save.move(self.filename, Book(edit.lastid))
            elib.epub_image(Book(edit.lastid))
            self.info["lastid"] = edit.lastid
            self.info["book"] = elib.res
            self.info["status"] = "Success"
        else:
            self.info["status"] = "Unsupported format"

    def write(self, my_file):
        # Write file in 8192 byte chunks
        with open((self.filename), 'wb') as f:
            while True:
                data = my_file.file.read(8192)
                if not data:
                    f.close()
                    break
                f.write(data)
                self.size += len(data)
        self.info["size"] = str(self.size)
        self.info["filename"] = str(self.tempid)

