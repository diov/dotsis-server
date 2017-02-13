import re

import requests

from models.player import Player
from services.base_music import BaseMusic

regex = r"id="


class WyMusic(BaseMusic):
    def __init__(self):
        super().__init__()
        self.player = Player()

    def analysis(self, url):
        music_id = re.split(regex, url)[1]
        if music_id:
            params = {'id': music_id, 'ids': str([music_id])}
            domain = 'http://music.163.com/api/song/detail'
            headers = {'Cookie': 'appver=1.5.0.75771', 'Referer': 'http://music.163.com/'}
            request = requests.get(domain, params=params, headers=headers)
            if request.status_code == 200:
                mp3_url = request.json()['songs'][0]['mp3Url']
                if mp3_url:
                    return mp3_url
        else:
            BaseMusic.support_error()

    def add(self, url):
        mp3_url = self.analysis(url)
        if mp3_url:
            self.player.add_music(mp3_url)

    def list(self):
        return self.player.get_list()

    def remove(self):
        self.player.remove_music()
