class Song:
    name = None
    singer = None
    album = None
    res_url = None

    def __init__(self, name, singer, album, res_url):
        super().__init__()
        self.name = name
        self.singer = singer
        self.album = album
        self.res_url = res_url
