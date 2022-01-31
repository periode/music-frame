# todo

- [x] web interface for composition and communication
  - [x] switch from labelling as technique to labelling as compositions (swirl, gabor, vexations)
  - [x] layout
  - [x] random
  - [x] polyphonic
  - [x] add references
  - [x] deliver audio files through `static.enframed.net`
  - [ ] DIY version
- [ ] power supply
  - [x] connect power supply
    - [ ] glue it
    - [ ] double sided tape on raspi
  - [ ] connect front switch
- [x] frame design
  - [x] drawing
  - [x] basic frame in blender
  - [x] support both standing and hanging
    - [x] possibility for table-like
  - [x] rough modeling in blender
  - [x] details in fusion
- [x] controller
  - [ ] network setup
  - [x] software volume control
    - [x] [using softvol 1](https://bytesnbits.co.uk/raspberry-pi-i2s-sound-output/)
    - [x] [using softvol 2](https://github.com/pimoroni/pirate-audio/issues/32) (`mplayer file -af volume=1`)
    - [x] pygame
  - [ ] stress test
    - [x] CPU usage goes up to 180%: change the amount of time waiting in main thread? change the memory split between GPU and CPU? -> 16MB
  - [x] local web interface
- [ ] code
  - [x] added debug mode
  - [x] add cute output: for each track pick a single character to print on the terminal (e.g. . - * ^) - memory leak
  - [x] make `run_event` and `threads` member fields of `Composition`
  - [x] check pygame playback on raspi
    - [x] fix `ALSA lib pcm.c:8545:(snd_pcm_recover) underrun occurred` error [src](https://forums.adafruit.com/viewtopic.php?f=19&t=175237&p=858042) -> nope, trying to have all files as WAV?
  - [x] move all binaries to pygame
  - [x] check bug on swirl where some files are not found - explicitly set filenames to null in composition init
  - [x] apache server
    - [x] running on arch
    - [x] running on pi
    - [x] captive portal
    - [ ] issue with the "gstatic.connectivitycheck" on android
      - [x] [this one](https://github.com/jerryryle/rogue_ap/blob/main/setup.sh) with modifications:
        - do not copy files over for the python wsgi app
        - change the apache config file to specify `ServerName poglos.here`
        - delete some of the python wsgi modules in the apache conf
        - add an iptables rule for ssh connection: `-A PREROUTING -i br0 -p tcp -m tcp --dport 22 -j DNAT --to-destination 10.1.1.1:22`
      - [x] adapt all files and configs from the repo
  - [x] connect with the flask API
    - [x] consider sockets
    - [x] add logging
    - [ ] design
      - [ ] typography rather than colors
      - [ ] logo should be unique (echo with the logo carved on the board with the cnc)
      - [ ] should we always see what is playing? should it be on a separate view?
        - [ ] if it's on a separate view, there is room for generative graphics!
        - [ ] what kind of headspace do i want the user to be in?
    - [x] make the server run on its own thread
    - [x] list available compositions
    - [x] start compositions
    - [x] stop compositions
    - [x] volume control
    - [x] save/load preferences
    - [x] reactive layout
    - [x] volume slider
    - [x] finish help text
    - [x] make a "loading" display while the composition loads
  - [x] pygame playback
    - [x] make lfo for volume
  - [x] make each playmode into classes
    - [x] make the data structure
    - [x] implement delay offsets through composition instruction config file
  - [x] threads
    - [x] research
    - [x] figure out how to cleanly close the threads (based on [this](https://stackoverflow.com/questions/41961430/how-to-cleanly-kill-subprocesses-in-python))
  - [x] use a player which supports mp3
    - [x] using `play` on arch
    - [x] check on raspi
      - [x] had to use mplayer
    - [x] have an args list for each player (e.g. quiet or not)
  - [x] test on raspberry pi

## notes

background music as an artwork.

it's about the surprise, the unexpected that comes out of the expected. the thing you know, and forgot you were aware of. it's about turning on the music the same way you turn on your favorite light on a coloured spot of the room. maybe like a musical plant.

questions of timing, of spacing, of silence. questions of repetition and resolution (how often does it resolve? does it ever resolve, like [this](https://www.youtube.com/watch?v=IE8gISNPz7I)?). carl stone made [elastic](https://www.youtube.com/watch?v=X-OHTj4xcgg) (hence symmetrical?) music.

[laurie spiegel on musical manipulation](http://www.retiary.org/ls/writings/musical_manip.html):  shift / reverse / rescale / interpolate / corrupt

[laurie spiegel - noise in composition](http://retiary.org/ls/writings/info_theory_music.html)

- different modes? (morning, afternoon, night)
- one long-ass soundscape vs. recombinating segments
- how much user control? volume, which composition, but all the way to changing parameters?

for conversion: `ffmpeg-normalize *.wav -ext mp3 -t -5 -c:a libmp3lame -t .`

names:

- sound board
- timbre
- sonancy
- assonance