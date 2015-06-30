from lib.Upload import Upload
from lib.Remove import Remove
from lib.Edit import Edit
from lib.Download import Download

from view.Listing import Listing
from view.EbookInfo import EbookInfo
#from lib.Database import *
from jinja2 import Environment, FileSystemLoader
import cherrypy
from cherrypy.lib import file_generator

cherrypy.config.update("conf/server.conf")
env = Environment(loader=FileSystemLoader('public/html'))
upload = Upload()
listing_view = Listing()
info_view = EbookInfo()
edit = Edit()
download = Download()


remove = Remove()
#TODO: Split up files, use REST API for downloading, uploading


class Manager(object):

    @cherrypy.expose()
    def index(self):
        t = env.get_template('index.html')
        return t.render()

    @cherrypy.expose()
    def download(self, id):
        download.get_file(id)
        cherrypy.response.headers['Content-Disposition'] = 'attachment; filename='+download.real_name
        with open(download.path, "rb") as f:
            return f.read()

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def upload(self, my_file):
        upload.ebook(my_file)
        return upload.info()

    @cherrypy.expose()
    def remove(self, book_id):
        remove.book(book_id)
        return remove.info()

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
    def edit(self, title="", author="", date="", ISBN="", ext="", language="", fname=""):
        return edit.new_epub(title, author, date, ISBN, ext, language, fname)


if __name__ == '__main__':
    cherrypy.quickstart(Manager(), '/', 'conf/app.conf')
