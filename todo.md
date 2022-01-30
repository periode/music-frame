# todo

- [x] web interface for composition and communication
  - [x] switch from labelling as technique to labelling as compositions (swirl, gabor, vexations)
  - [x] layout
  - [x] random
  - [x] polyphonic
  - [x] add references
  - [x] deliver audio files through `static.enframed.net`
<<<<<<< HEAD
  - [ ] DIY version
- [ ] power supply
  - [x] connect power supply
    - [ ] glue it
    - [ ] double sided tape on raspi
=======
- [ ] power supply
  - [ ] connect power supply
>>>>>>> 177918da9734fe93ae2b81b9514a5c762a71b34f
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
<<<<<<< HEAD
    - [x] CPU usage goes up to 180%: change the amount of time waiting in main thread? change the memory split between GPU and CPU? -> 16MB
=======
>>>>>>> 177918da9734fe93ae2b81b9514a5c762a71b34f
  - [x] local web interface
- [ ] code
  - [x] added debug mode
  - [x] add cute output: for each track pick a single character to print on the terminal (e.g. . - * ^) - memory leak
  - [x] make `run_event` and `threads` member fields of `Composition`
  - [x] check pygame playback on raspi
<<<<<<< HEAD
    - [x] fix `ALSA lib pcm.c:8545:(snd_pcm_recover) underrun occurred` error [src](https://forums.adafruit.com/viewtopic.php?f=19&t=175237&p=858042) -> nope, trying to have all files as WAV?
=======
    - [ ] fix `ALSA lib pcm.c:8545:(snd_pcm_recover) underrun occurred` error
>>>>>>> 177918da9734fe93ae2b81b9514a5c762a71b34f
  - [x] move all binaries to pygame
  - [x] check bug on swirl where some files are not found - explicitly set filenames to null in composition init
  - [x] apache server
    - [x] running on arch
    - [x] running on pi
<<<<<<< HEAD
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
=======
  - [x] connect with the flask API
>>>>>>> 177918da9734fe93ae2b81b9514a5c762a71b34f
    - [x] make the server run on its own thread
    - [x] list available compositions
    - [x] start compositions
    - [x] stop compositions
    - [x] volume control
    - [x] save/load preferences
    - [x] reactive layout
    - [x] volume slider
    - [x] finish help text
<<<<<<< HEAD
    - [x] make a "loading" display while the composition loads
=======
>>>>>>> 177918da9734fe93ae2b81b9514a5c762a71b34f
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
