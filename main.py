from lib.Upload import Upload
from lib.Remove import Remove
from lib.Edit import Edit
from lib.Book import Book

from view.Listing import Listing
from view.EbookInfo import EbookInfo
from view.UploadView import UploadView

from jinja2 import Environment, FileSystemLoader
import cherrypy

cherrypy.config.update("conf/server.conf")
env = Environment(loader=FileSystemLoader('public/html'))
listing_view = Listing()
info_view = EbookInfo()
edit = Edit()


remove = Remove()
#TODO: Split up files, use REST API for downloading, uploading


class Manager(object):

    @cherrypy.expose()
    def index(self):
        t = env.get_template('index.html')
        return t.render()

    @cherrypy.expose()
    def download(self, id):
        book = Book(id)
        cherrypy.response.headers['Content-Disposition'] = 'attachment; filename='+book.real_name
        with open(book.full_path, "rb") as f:
            return f.read()

    @cherrypy.expose()
    def image(self, id):
        book = Book(id)
        cherrypy.response.headers['Content-Type'] = "image/png"
        with open(book.image, "rb") as f:
            return f.read()

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def upload(self, my_file):
        upload = UploadView()
        upload.hashcheck(my_file)
        return upload.info

    @cherrypy.expose()
    def remove(self, id):
        remove.book(id)
        return remove.error

    @cherrypy.expose('listing')
    @cherrypy.tools.json_out()
    def listing_view(self, message=""):
        return listing_view.info(message)

    @cherrypy.expose('ebinfo')
    @cherrypy.tools.json_out()
    def info_view(self, fname):
        return info_view.epub(fname)

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def edit(self, title="", author="", date="", ISBN="", ext="", language="", fname="", imgext=""):
        return edit.new_epub(title, author, date, ISBN, ext, language, fname, imgext)


if __name__ == '__main__':
    cherrypy.quickstart(Manager(), '/', 'conf/app.conf')
