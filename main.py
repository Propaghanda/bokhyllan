from peewee import *
from lib.Upload import Upload
from lib.Remove import Remove
from lib.Test import Test
from lib.Database import *
from jinja2 import Environment, FileSystemLoader
import cherrypy

cherrypy.config.update("conf/server.conf")
#db = SqliteDatabase('bok.db')
env = Environment(loader=FileSystemLoader('public/html'))
upload = Upload()
test = Test()

book_db = Book()
remove = Remove()
#TODO: Split up files, use REST API for downloading, uploading


class HelloWorld(object):

    @cherrypy.expose()
    def index(self):
        db.connect()
        t = env.get_template('index.html')
        books = book_db.select()
        return t.render(books=books)

    @cherrypy.expose()
    #@cherrypy.tools.accept(media='application/x-download')
    def download(self):
        return 'You shouldn\'t be here'

    @cherrypy.expose()
    def upload(self, my_file, title, author):
        upload.book(book_db, my_file, title, author)
        return upload.info()

    @cherrypy.expose()
    def remove(self, book_id):
        remove.book(book_db, book_id)
        return remove.info()

    @cherrypy.expose()
    def test(self, message):
        return test.info(message)

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), '/', 'conf/app.conf')
