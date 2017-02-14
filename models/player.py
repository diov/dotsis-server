import subprocess
import threading


class Player:
    p = None
    play_list = None
    # is playing or not
    play_flag = False

    def __init__(self):
        self.play_list = []

    def popen_call(self, onExit, popenArgs):
        """
        Runs the given args in a subprocess.Popen, and then calls the function
        onExit when the subprocess completes.
        onExit is a callable object, and popenArgs is a lists/tuple of args that
        would give to subprocess.Popen.
        """

        def runInThread(onExit, popenArgs):
            self.p = subprocess.Popen(['mpg123', popenArgs], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
            self.p.wait()
            if self.play_flag:
                onExit()
            return

        thread = threading.Thread(target=runInThread, args=(onExit, popenArgs))
        thread.start()
        return thread

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
        if len(self.play_list) > 0:
            song = self.play_list.pop(0)
            self.play_flag = True
            self.popen_call(self.next_song(), song)
        else:
            self.play_flag = False

    def remove_music(self):
        if len(self.play_list) > 0:
            self.play_list.pop(0)
            self.next_song()
