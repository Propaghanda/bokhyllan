from lib.Database import Database
from lib.Save import Save
from lib.Edit import Edit
from lib.EbookLib import EbookLib
from lib.Book import Book
from lib.Checksum import Checksum
from lib.Mimetype import Mimetype
import hashlib
import os

class Scan:
    info = None

    def __init(self):
        self.info = {}

    def epub(self, path):
        self.info = {}
        checksum = Checksum()
        edit = Edit()
        elib = EbookLib()
        mime = Mimetype()
        save = Save()
        self.info['path'] = path
        for item in os.listdir(path):
            #mime = mimetypes.guess_type(item)
            print(item)
            try: 
                with open(path+item, "rb") as my_file:
                    data = my_file.read()
                m = mime.get_type(data)
                if m == 'application/epub+zip':
                    self.info[item] = item
                    md5 = hashlib.md5(data).hexdigest()
                    if checksum.check(md5):
                        elib.epub(path+item)
                        elib.res["md5"] = md5
                        edit.new(path+item, elib.res)
                        save.copy(path+item, Book(edit.lastid))
                        elib.epub_image(Book(edit.lastid))
                        print (elib.res)
                        print (md5)
                    else:
                        pass
                    print (m)
                    my_file.close()
            except Exception as e:
                self.info[item+" error"] = str(e)
