from lib.EbookLib import EbookLib
import random

elib = EbookLib()

class Upload:
    size = 0
    filename = None
    my_file = None
    tempid = None
    info = None

    def __init__(self):
        pass

    def ebook(self, my_file):
        self.my_file = my_file
        self.tempid = str(random.randint(1, 1000))
        ext = my_file.filename.split('.')[-1]
        self.filename = self.tempid + "." + ext

        # Write file in 8192 byte chunks
        with open(('books/temp/' + self.filename), 'wb') as f:
            while True:
                data = my_file.file.read(8192)
                if not data:
                    break
                f.write(data)
                self.size += len(data)

        test = elib.epub('books/temp/'+self.filename)
        elib.epub_image(self.tempid)
        self.info = {"size": str(self.size), "filename": str(self.tempid), "content_type": str(self.my_file.content_type),
                "book": elib.res}
