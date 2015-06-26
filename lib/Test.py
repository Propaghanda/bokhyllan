class Test:
    message = 'tjolla'

    def __init__(self):
        self.gg = 'gg'

    def info(self, book_db, message):
        self.message = message
        testbook = book_db.get(book_db.id == 1)
        return message, testbook.title
