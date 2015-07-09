import codecs
import io
import zipfile


class Mimetype:

    def __init__(self):
        pass

    def get_type(self, data): #  Checks input buffer for valid file types
        hexify = codecs.getencoder('hex')

        hexdata = hexify(data[:5])[0]

        if hexify(data[:4])[0] == b'504b0304': # Reads the 4 first bytes to check if the file is a zip
            iodata = io.BytesIO(data)
            zip = zipfile.ZipFile(iodata)
            try:
                m = zip.read('mimetype') # Checks for the file mimetype inside the zip to make sure it's an epub
                if m == b'application/epub+zip':
                    return 'application/epub+zip'
            except KeyError:
                pass
        if hexify(data[:5])[0] == b'255044462d': # Reads the first 5 bytes to check for the pdf signature %PDF-
            return 'application/pdf'
        else:
            return 'Unknown filetype, '+str(hexdata)

