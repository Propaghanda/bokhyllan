import codecs


class Mimetype:

    def __init__(self):
        pass

    def get_type(self, data):
        hexify = codecs.getencoder('hex')

        hexdata = hexify(data[:10])[0]
        print(hexdata)

        for i in [b'504b0304140000080000', b'504b0304140016080000']:
            if hexify(data[:10])[0] == i:
                return 'application/epub+zip'
            else:
                continue
        if hexify(data[:5])[0] == b'255044462d':
            return 'application/pdf'
        else:
            return 'Unknown filetype, '+str(hexdata)

