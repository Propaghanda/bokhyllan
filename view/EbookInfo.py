from lib.ParseEbook import ParseEbook

epub = ParseEbook()


class EbookInfo:

    def __init__(self):
        pass

    def epub(self, fname):
        return {str(fname)}
