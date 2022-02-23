#!/usr/bin/python

import argparse
import time
import threading
import os

if os.uname()[1] == "frame":
    import gpiozero

os.environ['WERKZEUG_RUN_MAIN'] = 'true'
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import logging
import pygame.mixer as mixer
import yaml
from flask import Flask
from flask_socketio import SocketIO

from preferences import Preferences
from composition import Composition
from logger import Logger

# --------------------------------------------------------------------------------------

if os.uname()[1] == "frame":
    switch = gpiozero.Button(4)
composition = None
preferences = Preferences()
logger = Logger()
app = None

def main():
    global composition
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--composition", default=None, help="composition to be played")
    parser.add_argument("-v", "--volume", default=1.0, help="volume (0.0, 1.0)")
    parser.add_argument("-d", "--debug", default=False, help="enable debug output")
    parser.add_argument("-W", "--web", default=True, help="enable web interface")
    parser.add_argument("-p", "--port", default="2046", help="port for the webapp")
    parser.add_argument("-H", "--host", default="0.0.0.0", help="host for the webapp")
    parser.add_argument("-P", "--preferences", default=None, help="load a preferences yaml file")
    args = parser.parse_args()

    if args.preferences:
        preferences.load("yaml", args.preferences)
    else:
        preferences.load("args", args)

    if preferences.debug:
        logger.setDebug()

    if preferences.composition not in Composition.fetch_compositions():
        logger.warning(f"composition {preferences.composition} is not in available compositions: {Composition.fetch_compositions()}!")
    
    mixer.init()

    if preferences.composition != None:
        composition = Composition(preferences.composition, preferences.debug)
        composition.begin()

    web_thread = None
    if preferences.web:
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
        web_thread = threading.Thread(name="web thread", target=socketio.run, args=(app, preferences.host, preferences.port))
        web_thread.daemon = True
        web_thread.start()
        logger.info(f"started socket server on {preferences.host}:{preferences.port}")

    try:
        while 1:
            if os.uname()[1] == "frame":
                if switch.is_pressed:
                    if composition == None:
                        logger.info("switch on...")
                        # TODO consider if we always want to have a composition playing when we turn it on?
                        # i'd tend to yes
                        name = preferences.composition if preferences.composition else "gabor" 
                        composition = Composition(name, preferences.debug)
                        composition.begin()
                else:
                    if composition:
                        logger.info("switch off...")
                        composition.stop()
                        composition = None
                        preferences.update('composition', None)
                        preferences.save()
            else:
                logger.debug(f'external host: {os.uname()[1]}')

            
            time.sleep(0.1)
    except KeyboardInterrupt:
        preferences.save()
        if composition:
            composition.stop()
        
        if mixer:
            mixer.quit()

        logger.info("...coda.\n")
        exit(0)

# --------------------------------------------------------------------------------------

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connect')
def connect():
    logger.info("new socket client connected")
    state = Composition.fetch_metas()

    current = None
    if composition:
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

        mixer.init()

        if composition == None or composition.name != name:
            try:
                composition.stop()
            except:
                pass

            composition = Composition(name, preferences.debug)

        composition.begin()
        preferences.update('composition', name)
        socketio.emit('status', {'composition': composition.meta}, json=True)
        preferences.save()
    else:
        logger.warning(f"no such composition \"{name}\" to begin")
        app.abort(400)      

@socketio.on("stop")
def stop():
    global composition
    logger.info(f"socket request to stop composition: {composition.name}")
    if composition:
        composition.stop()
        composition = None
        preferences.update('composition', None)
    socketio.emit('status', {'composition': None}, json=True)

@socketio.on("volume")
def volume(_vol):
    volume = int(_vol)
    normalized = volume * 0.01
    for i in range(mixer.get_num_channels()):
        mixer.Channel(i).set_volume(normalized)

    preferences.update('volume', normalized)

# --------------------------------------------------------------------------------------

if __name__ == "__main__":
    logger.info("music frame v0.1")
    main()
    
