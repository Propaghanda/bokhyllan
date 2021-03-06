import os
import shutil

class Save:
    size = 0
    filename = None
    my_file = None
    tempid = None
    info = None

    def __init__(self):
        pass

    def move(self, filename, bookObj):
        if not os.path.exists(bookObj.dir):
            os.makedirs(bookObj.dir)
        os.rename(filename, bookObj.full_path)

    def copy(self, filename, bookObj):
        if not os.path.exists(bookObj.dir):
            os.makedirs(bookObj.dir)
        shutil.copyfile(filename, bookObj.full_path)
