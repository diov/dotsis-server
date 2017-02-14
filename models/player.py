import subprocess
import threading

import time


class Player:
    p = None
    play_list = None
    # is playing or not
    play_flag = False

    def __init__(self):
        self.play_list = []

    def popen_call(self, on_exit, popen_args):
        """
        Runs the given args in a subprocess.Popen, and then calls the function
        on_exit when the subprocess completes.
        on_exit is a callable object, and popen_args is a lists/tuple of args that
        would give to subprocess.Popen.
        """

        def run_in_thread(callback, args):
            self.p = subprocess.Popen(['mpg123', args], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
            self.p.wait()
            self.play_list.pop(0)
            if self.play_flag:
                callback()
            return

        thread = threading.Thread(target=run_in_thread, args=(on_exit, popen_args))
        thread.start()
        return thread

    def stop_song(self):
        if self.p and self.play_flag:
            self.play_flag = False
            self.p.terminate()
            self.p = None

    def get_list(self):
        return self.play_list

    def add_music(self, song):
        self.play_list.append(song)
        if not self.play_flag:
            self.next_song()

    def next_song(self):
        if len(self.play_list) > 0:
            song = self.play_list[0]
            self.play_flag = True
            self.popen_call(self.next_song, song.get('res_url'))
        else:
            self.play_flag = False

    def remove_music(self):
        if self.play_flag:
            self.stop_song()
            time.sleep(0.01)
            self.next_song()
