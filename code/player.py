import time
import random
import subprocess
import sys
import os

if len(sys.argv) > 1:
    state = sys.argv[1]
else:
    exit("No playmode provided!")


if state == "vexations":
    vexations_files = ["0", "1", "2", "3", "4", "5"]
    vexations_durations = [27, 26, 26, 52, 27, 57]
elif state == "swirl":
    # load all files
    # probably a dict
    track = "saba"
    interval = 3
    swirl_files = ["0", "1", "2", "3"]
else:
    exit(f'No existing playmode: {state}!')

def swirl(_filenames, _interval, _track):
    index = 0
    start_time = time.time()
    timer = 0

    while True:
        if time.time() - start_time > timer:
            index = random.randint(0, len(_filenames)-1)
            timer = _interval + random.randint(-2, 3)

            filename = f'swirl/{_track}/{_filenames[index]}.mp3'
            filename = os.path.join(os.path.dirname(__file__), filename)
            subprocess.Popen(["aplay", filename])

            start_time = time.time()

def vexations(_filenames, _timer):
    index = 0
    start_time = time.time()
    timer = 0
    while True:
        if time.time() - start_time > timer:
            index = random.randint(0, len(_filenames)-1)
            timer = _timer[index] + random.randint(3, 5)

            filename = f'vexations/{_filenames[index]}.wav'
            filename = os.path.join(os.path.dirname(__file__), filename)
            subprocess.Popen(["aplay", filename])

            start_time = time.time()



if state == "vexations":
    vexations(vexations_files, vexations_durations)
elif state == "swirl":
    # run 4 parallel threads
    swirl(swirl_files, interval, track)

