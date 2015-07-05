from lib.EbookLib import EbookLib
import os

class Save:
    size = 0
    filename = None
    my_file = None
    tempid = None
    info = None

    def __init__(self, filename, bookObj):
        elib = EbookLib()
        if not os.path.exists(bookObj.dir):
            os.makedirs(bookObj.dir)
        os.rename(filename, bookObj.full_path)
        elib.epub(bookObj.full_path)
        elib.epub_image(bookObj)
        self.info = {}
        self.info["image"] = elib.img
        self.info["test"] = "test"
