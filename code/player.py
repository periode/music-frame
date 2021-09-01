import time
import random
import subprocess
import sys
import os
import threading
import socket

from mutagen.mp3 import MP3

class Composition:
    name = ""
    tracks = []
    filenames = []
    intervals = []
    def __init__(self, _name):
        print("- loading composition: ", _name)
        self.name = _name

        # getting all tracks from dir names
        for dirpath, dirs, files in os.walk(os.path.join(os.path.dirname(__file__), self.name)): 
            self.tracks = dirs
            break

        # getting all filenames and intervals from tracks
        for track in self.tracks:
            current_dir = os.path.join(os.path.dirname(__file__), self.name, track)

            for dirpath, dirs, files in os.walk(current_dir): 
                self.filenames.append(files)

                intervals = list()
                for f in files:
                    audio = MP3(os.path.join(current_dir, f))
                    intervals.append(audio.info.length)

                self.intervals.append(intervals)
                
        
        print(self.tracks)
        print(self.filenames)
        print(self.intervals)

# --------------------------------------------------------------------------------------

host = socket.gethostname()
print("host is " + host)
binary = "play"

if host == "tonkasten":
    binary = "mplayer"

states = ["vexations", "swirl"]
threads = list()

if len(sys.argv) > 1:
    state = sys.argv[1]
else:
    exit("No playmode provided! " + str(states))

if state not in states:
    exit(f'No existing playmode: {state}!')


def play(_filenames, _intervals, _track, _composition, _evt):
    index = 0
    start_time = time.time()
    timer = 0

    while _evt.is_set():
        if time.time() - start_time > timer:
            index = random.randint(0, len(_filenames)-1)
            timer = _intervals[index] + random.randint(1, 3) # make that into a variable?

            filename = f'{_composition}/{_track}/{_filenames[index]}'
            filename = os.path.join(os.path.dirname(__file__), filename)
            subprocess.Popen([binary, filename], shell=False)

            start_time = time.time()

def begin(_composition, _evt):
    print("- starting ", _composition.name)
    
    global threads
    _evt.set()

    for i in range(len(_composition.tracks)):
        thread = threading.Thread(target=play, args=(_composition.filenames[i], _composition.intervals[i], _composition.tracks[i], _composition.name, _evt), daemon=True)
        threads.append(thread)
        thread.start()


def main():
    composition = Composition(state)

    run_event = threading.Event()
    run_event.set()
    
    begin(composition, run_event)
    
    try:
        while 1:
            time.sleep(.1)
    except KeyboardInterrupt:
        
        run_event.clear()
        for thread in threads:
            thread.join()
        time.sleep(2)
        print("...tschuss!")


main()