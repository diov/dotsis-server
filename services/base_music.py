from models.player import Player


class BaseMusic:
    def __init__(self):
        self.player = Player()

    @staticmethod
    def support_error():
        raise Exception('不支持的分享地址')

    def match(self, url):
        raise Exception('Don\'t call this function not Implementation')

    def analysis(self, url):
        raise Exception('Don\'t call this function not Implementation')

    def add(self, url):
        song = self.match(url)
        if song.get('res_url'):
            self.player.add_music(song)
            return song
        else:
            return 'Unsupported Music'

    def list(self):
        return self.player.get_list()

    def remove(self):
        self.player.remove_music()
        return self.list()

    def stop(self):
        self.player.stop_song()
