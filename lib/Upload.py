from lib.EbookLib import EbookLib
import random

class Upload:
    size = 0
    filename = None
    my_file = None
    tempid = None
    info = None

    def __init__(self):
        self.info = {}
        pass

    def ebook(self, my_file):
        elib = EbookLib()
        self.my_file = my_file
        self.tempid = str(random.randint(1, 1000))
        ext = my_file.filename.split('.')[-1]
        self.filename = self.tempid + "." + ext

        if "application/epub+zip" in str(self.my_file.content_type):
            self.write(my_file)
            elib.epub('books/temp/'+self.filename)
            elib.epub_image(self.tempid)
            self.info["book"] = elib.res
            self.info["status"] = "Success"
        else:
            self.info["status"] = "Unsupported format"

        self.info["content_type"] = str(self.my_file.content_type)

    def write(self, my_file):
        # Write file in 8192 byte chunks
        with open(('books/temp/' + self.filename), 'wb') as f:
            while True:
                data = my_file.file.read(8192)
                if not data:
                    break
                f.write(data)
                self.size += len(data)
        self.info["size"] = str(self.size)
        self.info["filename"] = str(self.tempid)

