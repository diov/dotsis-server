import subprocess


class Player:
    p = None
    play_list = None
    # is playing or not
    play_flag = False

    def __init__(self):
        self.play_list = []

    def stop_song(self):
        if self.p:
            self.p.terminate()
            self.p = None
            self.play_list.clear()

    def get_list(self):
        pass

    def add_music(self, url):
        self.play_list.append(url)
        if not self.play_flag:
            self.next_song()

    def next_song(self):
        while len(self.play_list) > 0:
            song = self.play_list.pop(0)
            self.play_flag = True
            self.p = subprocess.Popen(['mpg123', song], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
            self.p.wait()
            self.play_flag = True
        else:
            print('the playlist is empty')

    def remove_music(self):
        if len(self.play_list) > 0:
            self.play_list.pop(0)
            self.next_song()
