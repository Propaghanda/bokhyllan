import sqlite3


class Database:
    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = sqlite3.connect('bok.db', check_same_thread=False)
        self._db_connection.row_factory = sqlite3.Row
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def commit(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()