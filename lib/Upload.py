from lib.EbookLib import EbookLib

elib = EbookLib()

class Upload:
    size = 0
    filename = None
    my_file = None

    def __init__(self):
        pass

    def ebook(self, my_file):
        self.my_file = my_file
        self.filename = my_file.filename

        ext = my_file.filename.split('.')[-1]
        # Write file in 8192 byte chunks
        with open(('books/temp/' + self.filename), 'wb') as f:
            while True:
                data = my_file.file.read(8192)
                if not data:
                    break
                f.write(data)
                self.size += len(data)

    def info(self): #TODO move to view
        test = elib.epub('books/temp/'+self.filename)
        return {"size": str(self.size), "filename": str(self.filename), "content_type": str(self.my_file.content_type),
                "book": elib.res}
