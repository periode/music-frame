from flask import Flask
from flask_socketio import SocketIO
import logging
import threading

from composition import Composition
from logger import Logger

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
composition = Composition()
logger = Logger()
preferences = None

def spinup():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    web_thread = threading.Thread(name="web thread", target=socketio.run, args=(app, preferences.host, preferences.port))
    web_thread.daemon = True
    web_thread.start()
    logger.info(f"started socket server on {preferences.host}:{preferences.port}")

@socketio.on('connect')
def connect():
    logger.info("new socket client connected")
    state = Composition.fetch_metas()

    current = None
    if composition.is_playing:
        current = composition.meta        

    socketio.emit('state', {"compositions": state, "current": current, "preferences": preferences.prefs}, json=True)

@socketio.on("start")
def start(_name):
    global composition
    name = _name

    logger.info(f"socket request to start composition: {name}")
    if name:
        if name not in Composition.fetch_compositions():
            return f"not a valid composition {name}"

        try:
            composition.stop()
        except:
            pass

        composition.load(name)
        composition.begin()

        socketio.emit('status', {'composition': composition.meta}, json=True)
        
        preferences.update('composition', name)
        preferences.save()
    else:
        logger.warning(f"no such composition \"{name}\" to begin")
        app.abort(400)      

@socketio.on("stop")
def stop():
    logger.info(f"socket request to stop composition: {composition.name}")
    if composition:
        composition.stop()
        preferences.update('composition', None)
    socketio.emit('status', {'composition': None}, json=True)

@socketio.on("volume")
def volume(_vol):
    v = int(_vol)
    n = v * 0.01
    Composition().setVolume(n)
    preferences.update('volume', n)