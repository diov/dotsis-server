import re

import requests

from models.song import Song
from services.base_music import BaseMusic

regex = r"?id="
domain_regex = r"music.163.com"


class WyMusic(BaseMusic):
    def analysis(self, url):
        music_id = re.split(regex, url)[1]
        if music_id:
            params = {'id': music_id, 'ids': str([music_id])}
            domain = 'http://music.163.com/api/song/detail'
            headers = {'Cookie': 'appver=1.5.0.75771', 'Referer': 'http://music.163.com/'}
            request = requests.get(domain, params=params, headers=headers)
            if request.status_code == 200:
                song_data = request.json()['songs'][0]['mp3Url']
                if song_data:
                    return Song(song_data['name'], song_data['singer'], song_data['album'], song_data['mp3Url'])
        else:
            BaseMusic.support_error()

    def match(self, url):
        url_fix = re.search(domain_regex, url)
        if url_fix:
            return self.analysis(url)
