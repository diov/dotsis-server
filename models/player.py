import subprocess


class Player:
    p = None
    play_list = None

    def __init__(self):
        self.play_list = []

    def stop_song(self):
        if self.p:
            self.p.terminate()
            self.p = None

    def get_list(self):
        pass

    def add_music(self, url):
        self.play_list.append(url)

    def next_song(self):
        if self.play_list:
            song = self.play_list[0]
            self.p = subprocess.Popen(['mpg123', song], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        else:
            print('the playlist is empty')

    def remove_music(self):
        if len(self.play_list) > 0:
            self.play_list.pop(0)
