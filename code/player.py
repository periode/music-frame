import time
import random
import subprocess

files = ["1", "2", "3", "4", "5", "6"]
durations = [27, 26, 26, 52, 27, 57]
index = 0
start_time = time.time()
timer = 0

while True:
    if time.time() - start_time > timer:
        index = random.randint(0, len(files)-1)
        timer = durations[index] + random.randint(3, 5)
        file = f'vexations/{files[index]}.wav'
        subprocess.Popen(["aplay", file])

        start_time = time.time()
