from flask import Flask
from flask import request
from services.wymusic import WyMusic

app = Flask(__name__)
music = WyMusic()


@app.route('/songs')
def add_music():
    {
        'GET': lambda url: music.list(),
        'POST': lambda url: music.add(url),
        'DELETE': lambda url: music.remove(),
    }[request.method](request.args.get('origin_url'))
    return 'Hello, world!'


app.run(host='192.168.2.9', port=4545, debug=True)
