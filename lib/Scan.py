from lib.Database import Database
from lib.Save import Save
from lib.Edit import Edit
from lib.EbookLib import EbookLib
from lib.Book import Book
from lib.Checksum import Checksum
import hashlib
import os
import mimetypes

class Scan:
    def __init(self):
        pass
    
    def epub(self, path):
        checksum = Checksum()
        save = Save()
        edit = Edit()
        elib = EbookLib()
        for item in os.listdir(path):
            mime = mimetypes.guess_type(item)
            print(item)
            if mime[0] == 'application/epub+zip':
                with open(path+item, "rb") as my_file:
                    data = my_file.read()
                    md5 = hashlib.md5(data).hexdigest()
                if checksum.check(md5):
                    elib.epub(path+item)
                    elib.res["md5"] = md5
                    edit.new_epub(elib.res)
                    save.move(path+item, Book(edit.lastid))
                    elib.epub_image(Book(edit.lastid))
                    print (elib.res)
                print (mime)
                print (md5)
