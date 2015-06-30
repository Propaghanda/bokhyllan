from lib.Database import Database


class Listing:
    book = {}
    books = []
    json_prepared = {}

    def __init__(self):
        pass

    def info(self, message):
        self.book = {}
        self.books = []
        self.message = message
        db = Database()
        query = db.query("SELECT * FROM `book`", "").fetchall()
        # add items from db to dict for json output
        for item in query:
            self.book = {
                'title': item['title'],
                'author': item['author'],
                'date': item['date'],
                'ISBN': item['ISBN'],
                'ext': item['ext'],
                'language': item['language']
            }
            self.books.append(self.book)
            self.json_prepared['books'] = self.books
        self.json_prepared['books'] = self.books

        return self.json_prepared
