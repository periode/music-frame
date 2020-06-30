# tonkasten

endless music box. wip.

## intent

a sonic atmosphere contained in a sealed box. turn it on, let it run and fill the room for as long as needed.

## resources

- [tech.md](tech.md) - list of all parts currently used for the prototype
- [music.md](music.md) - notes for musical generation
- [workshop.md](workshop.md) - workshop to build your own tonkasten

## thoughts and influences

- [buddha machine](https://www.youtube.com/watch?v=VlSM3GMuYVU), for the product design
- erik satie's [vexations](https://en.wikipedia.org/wiki/Vexations), for the ability to repeat the same motif without boredom
- brian eno's generative music (made with [Koan](https://www.wired.com/1997/10/can-generative-music-carry-the-nets-tunes/), now rebranded as [Wotja](https://intermorphic.com/wotja/)), for the technical contribution
- [listen to wikipedia](http://listen.hatnote.com/), for the possible data visualization
- [brand new noise](https://www.brandnewnoise.com/), for the product design (without the interaction/instrument aspect)
- different modes? (morning, afternoon, night)
- one long-ass soundscape vs. recombinating segments

## todo

- [ ] fix the build on the development arduino -> something got messed up withthe pins (it used to be pin 4 for CS, while the pin 10 was the one that was actually connected, and when i changed some things in the pcmConfig.h, it might have messed somehing up) -> **do a fresh build with the library tests in the arduino IDE**
- [ ] have a step-up converter for the speaker when running the LM386
- [x] check for multiple outputs -> multiple outputs only available on MEGA boards (cause the arduino only has 1 16-bit timer)
- [x] add capacitors at the Vin of amp -> did not improve
- [x] add lowpass filter (?) -> did not make a difference
- [ ] integrate a switch for turning on and off
- [ ] design full frame
- [ ] write a walkthrough
