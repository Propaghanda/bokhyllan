from lib.Upload import Upload
from lib.Remove import Remove
from view.Index import Index
#from lib.Database import *
from jinja2 import Environment, FileSystemLoader
import cherrypy

cherrypy.config.update("conf/server.conf")
env = Environment(loader=FileSystemLoader('public/html'))
upload = Upload()
index_view = Index()


remove = Remove()
#TODO: Split up files, use REST API for downloading, uploading


class Manager(object):

    @cherrypy.expose()
    def index(self):
        t = env.get_template('index.html')
        return t.render()

    @cherrypy.expose()
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

    @cherrypy.expose('index.json')
    def index_view(self, message=12):
        return index_view.info(message)

if __name__ == '__main__':
    cherrypy.quickstart(Manager(), '/', 'conf/app.conf')
