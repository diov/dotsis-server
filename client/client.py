import fire
import requests

APP_DESC = '''
树莓派点歌台_命令行版本
'''


class Play(object):
    def __init__(self, ip='192.168.2.9:4545'):
        self.ip = ip

    def add(self, url):
        data = {'origin_url': url}
        req = requests.post("http://{}/songs".format(self.ip), data=data)
        if req.status_code == 200:
            song = req.json()
            print("{} == {}\n".format(song.get('singer'), song.get('name')))
        else:
            print(' 点歌失败')

    def next(self):
        req = requests.delete("http://{}/songs".format(self.ip))
        if req.status_code == 200:
            songs = req.json()
            if len(songs) > 0:
                print("{} == {}\n".format(songs[0].get('singer'), songs[0].get('name')))
            else:
                print('没歌了！')

    def list(self):
        req = requests.get("http://{}/songs".format(self.ip))
        if req.status_code == 200:
            songs = req.json()
            if len(songs) > 0:
                for song in songs:
                    print("{} == {}\n".format(song.get('singer'), song.get('name')))
            else:
                print('没歌了！')


if __name__ == '__main__':
    print(APP_DESC)
    fire.Fire(Play)
