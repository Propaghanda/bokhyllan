from lib.EbookLib import EbookLib

epub = EbookLib()


class EbookInfo:

    def __init__(self):
        pass

    def epub(self, fname):
        return {str(fname)}
