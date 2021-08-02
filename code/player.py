import time
import random
import subprocess
import sys
import os
import threading

if len(sys.argv) > 1:
    state = sys.argv[1]
else:
    exit("No playmode provided!")


if state == "vexations":
    vexations_files = ["0", "1", "2", "3", "4", "5"]
    vexations_intervals = [27, 26, 26, 52, 27, 57]
    vexations_tracks = ["main"]
elif state == "swirl":
    # load all files
    # probably a dict
    swirl_tracks = ["saba"]
    swirl_intervals = [3, 3, 3, 3]
    swirl_files = ["0", "1", "2", "3"]
else:
    exit(f'No existing playmode: {state}!')

tracks = list()

def play(_filenames, _intervals, _track, _composition, _evt):
    index = 0
    start_time = time.time()
    timer = 0

    while _evt.is_set():
        if time.time() - start_time > timer:
            index = random.randint(0, len(_filenames)-1)
            timer = _intervals[index] + random.randint(1, 3) # make that into a variable?

            filename = f'{_composition}/{_track}/{_filenames[index]}.mp3'
            filename = os.path.join(os.path.dirname(__file__), filename)
            subprocess.Popen(["play", filename], shell=False)

            start_time = time.time()

def swirl(_filenames, _intervals, _tracks, _evt):
    print("starting swirl")
    
    global tracks
    _evt.set()

    for _track in _tracks:
        track = threading.Thread(target=play, args=(_filenames, _intervals, _track, "swirl", _evt), daemon=True)
        tracks.append(track)
        track.start()



def vexations(_filenames, _intervals, _tracks, _evt):
    print("starting vexations")

    global tracks
    _evt.set()

    for _track in _tracks:
        track = threading.Thread(target=play, args=(_filenames, _intervals, _track, "vexations", _evt), daemon=True)
        tracks.append(track)
        track.start()


def main():
    run_event = threading.Event()
    run_event.set()
    if state == "vexations":
        vexations(vexations_files, vexations_intervals, vexations_tracks, run_event)
    elif state == "swirl":
        # run 4 parallel threads
        swirl(swirl_files, swirl_intervals, swirl_tracks, run_event)

    try:
        while 1:
            time.sleep(.1)
    except KeyboardInterrupt:
        print("attempting to close threads.")
        
        run_event.clear()
        for track in tracks:
            track.join()
        print("threads successfully closed")
        time.sleep(2)


main()