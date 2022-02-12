# software

## setup

hw: raspberry pi zero 2
os: raspbian buster lite

- python version: 3.7+
- `pip install -r requirements.txt`
- file playback
  - [pygame](https://www.pygame.org)

[how to make python3 default](https://stackoverflow.com/questions/62275714/how-to-change-the-default-python-version-in-raspberry-pi)

- `sudo ln -s /usr/bin/pip3 /usr/bin/pip`
- `sudo rm /usr/bin/python && sudo ln -s /usr/bin/python3 /usr/bin/python`

## documentation

hostname: poglos

username: pi
password: poglos

### access point

[rogue ap](https://github.com/jerryryle/rogue_ap) was preferred

other research:

- [https://github.com/gitbls/autoAP]
- [https://github.com/balena-os/wifi-connect]
- [https://github.com/rudiratlos/hotspot]
- [https://www.raspberryconnect.com/projects/65-raspberrypi-hotspot-accesspoints/158-raspberry-pi-auto-wifi-hotspot-switch-direct-connection]
- [https://raspberrypi.stackexchange.com/questions/93311/switch-between-wifi-client-and-access-point-without-reboot]

## audio

the ideal is to share directly the project file (for instance, `.als` for ableton live, `.maxpat` for max, any source for programming environments), along with all samples used.

## instructions.yml

there is a config at the top of each track directory:

- mode
  - numeric: a given range of seconds to wait between two tracks
  - measure: a given range of proportions of the track length (0, 0.25, 0.5, 0.75, 1)
  - markov