import time
import math
import os
import random
import threading

import pygame.mixer as mixer
import yaml

from logger import Logger


class Composition:
    _compositions = None
    _metas = None

    def __init__(self, _name, _debug):
        self.logger = Logger()
        self.logger.info(f"loading composition - {_name}")
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
            self.logger.debug(f"opening meta file: {path}")

            self.meta = yaml.safe_load(open(path))
            self.logger.debug(f"composition meta: {self.meta}")
        except:
            exit(f"no meta found for composition: {self.name}.")

        # getting all tracks from dir names
        for dirpath, dirs, files in os.walk(
            os.path.join(os.path.dirname(__file__), "compositions/", self.name)
        ):
            self.tracks = dirs
            
            self.logger.debug(f'found tracks: {self.tracks}')
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
                        self.logger.error(
                            f'no mode found for track {track}: {track_meta["mode"]}'
                        )
                    

                self.intervals.append(intervals)
                self.volumes.append(volumes)
                self.periods.append(periods)
                self.offsets.append(offsets)

        
        self.logger.debug(f"filenames: {self.filenames}")
        self.logger.debug(f"intervals: {self.intervals}")
        self.logger.debug(f"volumes: {self.volumes}")
        self.logger.debug(f"periods: {self.periods}")
        self.logger.debug(f"offsets: {self.offsets}")

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
            time.sleep(1)

        for thread in self.threads:
            thread.join()

    def play(self, _index):
        self.logger.debug(f"playing track#{_index}")
        
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
                    
                    self.logger.debug(f"playing {self.name}/{self.tracks[_index]}/{self.filenames[_index][instance]}")
                    audio = mixer.Sound(
                        f"compositions/{self.name}/{self.tracks[_index]}/{self.filenames[_index][instance]}"
                    )
                    mixer.Channel(_index).play(audio, -1)
                
                vol = (math.sin(self.offsets[_index][instance] + time.time() * self.periods[_index][instance]) + 1 ) / 2
                mixer.Channel(_index).set_volume(vol)
    
    @classmethod
    def fetch_compositions(cls):
        if cls._compositions:
            return cls._compositions
        else:
            for dirpath, dirs, files in os.walk(os.path.join(os.path.dirname(__file__), 'compositions')):
                cls._compositions = dirs
                return cls._compositions

    @classmethod
    def fetch_metas(cls):
        if cls._metas:
            return cls._metas
        else:
            cls._metas = []
            for name in cls._compositions:
                try:
                    meta = yaml.safe_load(
                        open(
                            os.path.join(os.path.dirname(__file__), "compositions/", name)
                            + "/instructions.yml"
                        )
                    )

                    cls._metas.append({
                        "name"        : meta["name"],
                        "artist"      : meta["artist"],
                        "description" : meta["description"]
                    })

                except:
                    exit(f"no meta found for composition: {name}.")
                
            return cls._metas
