#!/usr/bin/python

import time
import random
import math
import sys
import threading
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame.mixer as mixer
import yaml

DEBUG = False

class Composition:
    global DEBUG
    name = ""
    tracks = []
    filenames = []

    intervals = []
    volumes = []
    periods = []
    offsets = []

    def __init__(self, _name):
        print(f"loading composition - {_name}")
        self.name = _name
        try:
            self.instructions = yaml.safe_load(
                open(
                    os.path.join(os.path.dirname(__file__), self.name)
                    + "/instructions.yml"
                )
            )
        except:
            exit(f"no instructions found for composition: {self.name}.")

        # getting all tracks from dir names
        for dirpath, dirs, files in os.walk(
            os.path.join(os.path.dirname(__file__), self.name)
        ):
            self.tracks = dirs
            break

        # getting all filenames and intervals from tracks
        for track in self.tracks:
            current_dir = os.path.join(os.path.dirname(__file__), self.name, track)
            track_instructions = self.instructions["tracks"][track]

            for dirpath, dirs, files in os.walk(current_dir):
                self.filenames.append(files)

                intervals = []
                volumes = []
                periods = []
                offsets = []
                for f in files:
                    audio = mixer.Sound(os.path.join(current_dir, f))
                    offset = 0
                    if self.instructions["mode"] == "numeric":
                        offset = random.randint(
                            track_instructions["range"][0],
                            track_instructions["range"][1],
                        )

                        intervals.append(audio.get_length() + offset)
                        volumes.append(1)
                    elif self.instructions["mode"] == "oscillating":
                        offset = random.random() * track_instructions["offset"][1] + track_instructions["offset"][0]
                        period = random.random() * track_instructions["period"][1] + track_instructions["period"][0]
                        
                        periods.append(period)
                        offsets.append(offset)
                        intervals.append(0)
                    else:
                        print(
                            f'no mode found for track {track}: {track_instructions["mode"]}'
                        )
                    

                self.intervals.append(intervals)
                self.volumes.append(volumes)
                self.periods.append(periods)
                self.offsets.append(offsets)

        if DEBUG:
            print(f"tracks in composition: {self.tracks}")
            print(f"composition instructions: {self.instructions}")
            print(f"filenames: {self.filenames}")
            print(f"intervals: {self.intervals}")
            print(f"volumes: {self.volumes}")
            print(f"periods: {self.periods}")
            print(f"offsets: {self.offsets}")

    def begin(self, _evt, _threads):
        _evt.set()

        for i in range(len(self.tracks)):
            thread = threading.Thread(target=self.play, args=(i, _evt), daemon=True)
            _threads.append(thread)
            thread.start()

    def play(self, _index, _evt):
        instance = 0
        start_time = time.time()
        timer = 0

        while _evt.is_set():
            if self.instructions["mode"] == "numeric":
                if time.time() - start_time > timer:
                    instance = random.randint(0, len(self.filenames[_index]) - 1)
                    timer = self.intervals[_index][instance]

                    audio = mixer.Sound(
                        f"{self.name}/{self.tracks[_index]}/{self.filenames[_index][instance]}"
                    )
                    mixer.Channel(_index).play(audio)

                    start_time = time.time()
            elif self.instructions["mode"] == "oscillating":
                if not mixer.Channel(_index).get_busy():
                    audio = mixer.Sound(
                        f"{self.name}/{self.tracks[_index]}/{self.filenames[_index][instance]}"
                    )
                    mixer.Channel(_index).play(audio, -1)
                
                vol = (math.sin(self.offsets[_index][instance] + time.time() * self.periods[_index][instance]) + 1 ) / 2
                mixer.Channel(_index).set_volume(vol)


# --------------------------------------------------------------------------------------

def main():
    print("poglos v0.1")
    compositions = ["vexations", "swirl", "gabor"]

    if len(sys.argv) == 2:
        composition = sys.argv[1]
    else:
        exit(f"no playmode provided! {str(compositions)}")

    if composition not in compositions:
        exit(f"no existing playmode: {composition}!")

    mixer.init()
    composition = Composition(composition)

    threads = list()
    run_event = threading.Event()
    run_event.set()

    composition.begin(run_event, threads)

    try:
        while 1:
            time.sleep(0.1)
    except KeyboardInterrupt:
        run_event.clear()
        mixer.fadeout(1000)
        mixer.quit()
        for thread in threads:
            thread.join()

        print("\n...coda.")


main()
