import pygame.mixer as mixer
import time

mixer.init()

channels = [
    mixer.Channel(0),
    mixer.Channel(1),
    mixer.Channel(2),
    mixer.Channel(3)
]

for i in range(4):
    track = mixer.Sound(f'gabor/main/{i}.mp3')
    channels[i].play(track)

while mixer.get_busy():
    time.sleep(0.1)

exit()