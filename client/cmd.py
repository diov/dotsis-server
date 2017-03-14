import argparse

import sys

import requests

APP_DESC = '''
树莓派点歌台_命令行版本
'''
print(APP_DESC)
parser = argparse.ArgumentParser(description=APP_DESC)
parser.add_argument('url', metavar='URL', nargs='+', help='music url')
parser.add_argument('-i', '--ip', type=str, default='192.168.2.9:4545', help='set Raspberry Pi\'s ip and port')
parser.add_argument('-n', '--next', action='store_true', help='next song')
parser.add_argument('-l', '--list', action='store_true', help='list songs')
args = parser.parse_args()

next_song = args.next
list_song = args.list
url = args.url
ip = args.ip

if next_song:
    req = requests.delete("http://{}/songs".format(ip))
    if req.status_code == 200:
        songs = req.json()
        if len(songs) > 0:
            print("{} == {}\n".format(songs[0].get('singer'), songs[0].get('name')))
        else:
            print('没歌了！')
elif list_song:
    req = requests.get("http://{}/songs".format(ip))
    if req.status_code == 200:
        songs = req.json()
        if len(songs) > 0:
            for song in songs:
                print("{} == {}\n".format(song.get('singer'), song.get('name')))
        else:
            print('没歌了！')
else:
    data = {'origin_url': url}
    req = requests.post("http://{}/songs".format(ip), data=data)
    if req.status_code == 200:
        song = req.json()
        print("{} == {}\n".format(song.get('singer'), song.get('name')))
    else:
        print(' 点歌失败')
