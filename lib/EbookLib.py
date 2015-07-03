import zipfile
from lib.Book import Book
from lxml import etree



class EbookLib:
    img = None
    res = {}

    def __init__(self):
        pass

    def epub(self, fname):
        ns = {
            'n':'urn:oasis:names:tc:opendocument:xmlns:container',
            'pkg':'http://www.idpf.org/2007/opf',
            'dc':'http://purl.org/dc/elements/1.1/'
        }

        # prepare to read from the .epub file
        zip = zipfile.ZipFile(fname)

        # find the contents metafile
        txt = zip.read('META-INF/container.xml')
        tree = etree.fromstring(txt)
        cfname = tree.xpath('n:rootfiles/n:rootfile/@full-path',namespaces=ns)[0]

        # grab the metadata block from the contents metafile
        cf = zip.read(cfname)
        self.res["content"] = cfname
        cfdir = cfname.split('/')
        if len(cfdir) > 1:
            cdir = cfdir[0] + "/"
        else:
            cdir = ""

        self.res["cdir"] = cdir
        tree = etree.fromstring(cf)
        p = tree.xpath('/pkg:package/pkg:metadata',namespaces=ns)[0]

        # repackage the data
        for s in ['title', 'language', 'creator', 'date', 'identifier']:
            self.res[s] = p.xpath('dc:%s/text()' % s, namespaces=ns)[0]

        i = tree.xpath('/pkg:package/pkg:manifest', namespaces=ns)[0]
        
        self.img = cdir + i.xpath('pkg:item[starts-with(@id, "cover")]/@href', namespaces=ns)[0]
        #test = i.xpath('item[@id="cover"]/@href', namespaces=ns)[0]
        self.res['ext'] = fname.split('.')[-1]
        self.res['img'] = self.img
        zip.close()

    def epub_image(self, fname, path):
        zip = zipfile.ZipFile(path+"/"+fname)
        self.epub(path+"/"+fname)
        try:
            img = zip.read(self.img)
        except KeyError:
            return "No image"

        with open(path+"/cover.jpeg", 'wb') as f:
            f.write(img)
        zip.close()
