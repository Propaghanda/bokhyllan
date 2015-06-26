import sqlite3
from lib.Database import Database

class Test:
    #con = sqlite3.connect('bok.db', check_same_thread=False)
    #c = con.cursor()


    def __init__(self):
        self.gg = 'gg'

    def info(self, message):
        self.message = message
        Database.sth.execute("SELECT * FROM `book`")
        list = []
        for item in query:
            list.append(item)

        return str(list)
