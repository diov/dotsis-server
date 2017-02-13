from flask import Flask
from flask import request
from services.wymusic import WyMusic

app = Flask(__name__)
music = WyMusic()


@app.route('/songs', methods=['GET', 'POST', 'DELETE'])
def add_music():
    {
        'GET': lambda request_obj: music.list(),
        'POST': lambda request_obj: music.add(request_obj.form.get('origin_url')),
        'DELETE': lambda request_obj: music.remove(),
    }[request.method](request)
    return 'Hello, world!'


@app.route('/stop')
def stop_music():
    music.stop()


app.run(host='0.0.0.0', port=4545, debug=True)
