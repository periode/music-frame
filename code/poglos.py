#!/usr/bin/python

import argparse
from locale import normalize
import time
import random
import math
import threading
import os
import json

os.environ['WERKZEUG_RUN_MAIN'] = 'true'
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame.mixer as mixer
import yaml
from flask import Flask, request
from flask_cors import CORS, cross_origin

from preferences import Preferences

class Composition:
    def __init__(self, _name, _debug):
        print(f"loading composition - {_name}")
        self.run_event = None
        self.threads = None

        self.debug = _debug
        self.tracks = []
        self.filenames = []

        self.intervals = []
        self.volumes = []
        self.periods = []
        self.offsets = []
        self.name = _name

        try:
            path = os.path.join(os.path.dirname(__file__), "compositions/", self.name, "instructions.yml")
            if self.debug:
                print(f"opening meta file: {path}")
            self.meta = yaml.safe_load(open(path))
            if self.debug:
                print(f"composition meta: {self.meta}")
        except:
            exit(f"no meta found for composition: {self.name}.")

        # getting all tracks from dir names
        for dirpath, dirs, files in os.walk(
            os.path.join(os.path.dirname(__file__), "compositions/", self.name)
        ):
            self.tracks = dirs
            if self.debug:
                print(f'found tracks: {self.tracks}')
            break

        # getting all filenames and intervals from tracks
        for track in self.tracks:
            current_dir = os.path.join(os.path.dirname(__file__), "compositions/", self.name, track)
            track_meta = self.meta["tracks"][track]

            for dirpath, dirs, files in os.walk(current_dir):
                self.filenames.append(files)

                intervals = []
                volumes = []
                periods = []
                offsets = []
                for f in files:
                    audio = mixer.Sound(os.path.join(current_dir, f))
                    offset = 0
                    if self.meta["mode"] == "numeric":
                        offset = random.randint(
                            track_meta["range"][0],
                            track_meta["range"][1],
                        )

                        intervals.append(audio.get_length() + offset)
                        volumes.append(1)
                    elif self.meta["mode"] == "oscillating":
                        offset = random.random() * track_meta["offset"][1] + track_meta["offset"][0]
                        period = random.random() * track_meta["period"][1] + track_meta["period"][0]
                        
                        periods.append(period)
                        offsets.append(offset)
                        intervals.append(0)
                        volumes.append(1)
                    else:
                        print(
                            f'no mode found for track {track}: {track_meta["mode"]}'
                        )
                    

                self.intervals.append(intervals)
                self.volumes.append(volumes)
                self.periods.append(periods)
                self.offsets.append(offsets)

        if self.debug:
            print(f"filenames: {self.filenames}")
            print(f"intervals: {self.intervals}")
            print(f"volumes: {self.volumes}")
            print(f"periods: {self.periods}")
            print(f"offsets: {self.offsets}")

    def begin(self):
        self.threads = []
        self.run_event = threading.Event() 
        self.run_event.set()

        for i in range(len(self.tracks)):
            thread = threading.Thread(target=self.play, args=(i,))
            self.threads.append(thread)
            thread.start()

    def stop(self):
        self.run_event.clear()
        
        if mixer:
            mixer.fadeout(1000)

        for thread in self.threads:
            thread.join()

    def play(self, _index):
        if self.debug:
            print(f"playing track#{_index}")
        
        instance = 0
        start_time = time.time()
        timer = 0

        while self.run_event.is_set():
            if self.meta["mode"] == "numeric":
                if time.time() - start_time > timer:
                    instance = random.randint(0, len(self.filenames[_index]) - 1)
                    timer = self.intervals[_index][instance]

                    audio = mixer.Sound(
                        f"compositions/{self.name}/{self.tracks[_index]}/{self.filenames[_index][instance]}"
                    )
                    mixer.Channel(_index).play(audio)

                    start_time = time.time()
            elif self.meta["mode"] == "oscillating":
                if not mixer.Channel(_index).get_busy():
                    if self.debug:
                        print(f"playing {self.name}/{self.tracks[_index]}/{self.filenames[_index][instance]}")
                    audio = mixer.Sound(
                        f"compositions/{self.name}/{self.tracks[_index]}/{self.filenames[_index][instance]}"
                    )
                    mixer.Channel(_index).play(audio, -1)
                
                vol = (math.sin(self.offsets[_index][instance] + time.time() * self.periods[_index][instance]) + 1 ) / 2
                mixer.Channel(_index).set_volume(vol)


# --------------------------------------------------------------------------------------
        

composition = None
preferences = Preferences()

def fetch_compositions():
    for dirpath, dirs, files in os.walk(os.path.join(os.path.dirname(__file__), 'compositions')):
        return dirs

def main():
    global composition
    global preferences

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
    

    if preferences.composition not in fetch_compositions():
        print(f"composition {preferences.composition} is not in available compositions: {fetch_compositions()}!")
    
    mixer.init()

    if preferences.composition != None:
        composition = Composition(preferences.composition, preferences.debug)
        composition.begin()

    web_thread = None
    if preferences.web:
        web_thread = threading.Thread(name="web thread", target=app.run, args=("0.0.0.0",preferences.port))
        web_thread.daemon = True
        web_thread.start()

    try:
        while 1:
            time.sleep(0.1)
    except KeyboardInterrupt:
        preferences.save()
        if mixer:
            mixer.quit()
        if composition:
            composition.stop()

        print("\n...coda.")
        exit(0)

# --------------------------------------------------------------------------------------

app = Flask(__name__, static_url_path="/www")
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

@app.route("/start")
@cross_origin()
def start():
    global composition
    name = request.args.get('composition')
    if name:
        if name not in fetch_compositions():
            return f"not a valid composition {name}"

        mixer.init()

        if composition == None or composition.name != name:
            if composition:
                composition.stop()
            composition = Composition(name, preferences.debug)

        composition.begin()
        preferences.update('name', name)
        return json.dumps(composition.meta)
    else:
        print(f"no such composition \"{name}\" to begin")
        app.abort(400)      

@app.route("/stop")
@cross_origin()
def stop():
    global composition
    print("stopping composition")
    if composition:
        composition.stop()
        preferences.update('name', None)
    return "stop the composition"

@app.route("/state")
@cross_origin()
def state():
    state = []
    compositions = fetch_compositions()

    for name in compositions:
        try:
            meta = yaml.safe_load(
                open(
                    os.path.join(os.path.dirname(__file__), "compositions/", name)
                    + "/instructions.yml"
                )
            )

            state.append({
                "name"        : meta["name"],
                "artist"      : meta["artist"],
                "description" : meta["description"]
            })

        except:
            exit(f"no meta found for composition: {name}.")

        current = None
        if composition:
            current = composition.meta
        

    return json.dumps({"compositions": state, "current": current, "preferences": preferences.prefs})

@app.route("/volume")
@cross_origin()
def volume():
    volume = int(request.args.get('vol'))
    normalized = volume * 0.01
    for i in range(mixer.get_num_channels()):
        mixer.Channel(i).set_volume(normalized)

    preferences.update('volume', normalized)
    return "success"

if __name__ == "__main__":
    print("poglos v0.1")
    main()
    