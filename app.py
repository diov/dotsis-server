from flask import Flask
from flask import request
from services.wymusic import WyMusic

app = Flask(__name__)
music = WyMusic()


@app.route('/songs')
def add_music():
    {
        'GET': lambda: music.list(),
        'POST': lambda url: music.add(url),
        'DELETE': lambda: music.remove(),
    }[request.method](request.args.get('origin_url'))


app.run(port=4545, debug=True)
