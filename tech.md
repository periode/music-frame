# tech

## hardware

### main

- exciters:
- - [dayton exciter - DAEX25CT-4](https://www.variant-hifi.de/produkt/exciters/dayton-audio-daex25ct4-1422.html) / 11.50e 10W
- - 4 Ohm [impedance](http://www.learningaboutelectronics.com/Articles/What-is-speaker-impedance)
- - 3 W RMS output
- amp: 
- [hifiberry miniamp](https://www.hifiberry.com/shop/boards/miniamp/)
- [adafruit stereo speaker bonnet](https://www.adafruit.com/product/3346) - cheaper and smaller

size of the mounted surface: approx 50x35cm, voltage sent: between 5V and 12V

### software

- python version: 3.7+
- `pip install -r requirements.txt`
- - mutagen: get track duration
- file playback
  - [mplayer](http://www.mplayerhq.hu/design7/info.html) (raspberry pi)
  - play (linux)

[how to make python3 default](https://stackoverflow.com/questions/62275714/how-to-change-the-default-python-version-in-raspberry-pi)

- `sudo ln -s /usr/bin/pip3 /usr/bin/pip`
- `sudo rm /usr/bin/python && sudo ln -s /usr/bin/python3 /usr/bin/python`

### alternative

- battery version: [pisugar2](https://www.tindie.com/products/pisugar/pisugar2-battery-for-raspberry-pi-zero/)
- raspi amp: [audio shim amp](https://thepihut.com/collections/raspberry-pi-audio-hats/products/audio-amp-shim-3w-mono-amp)
- controller: [arduino nano](https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829) - 4.95
- amplifier: [lm386 module](https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829) - 2.95
- storage: [sd card module](https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829) - 3.50
- voltage step-up: to find
- integrated sd + dac: [yx5300](https://www.ebay.de/itm/YX5300-MP3-Musik-Player-Modul-Serial-UART-TTL-Module-Arduino-Raspberry-YX6300/253998552373?hash=item3b237e5535:g:0MMAAOSwWIJb-t2i)
- esp32 board: [wemos pro](https://docs.wemos.cc/en/latest/d32/d32_pro.html)

### arduino software

- playback of WAV files from SD Card: [TMRpcm](https://github.com/TMRh20/TMRpcm)

## notes

- issue with software volume control?
  - https://www.hifiberry.com/docs/hifiberryos/hifiberryos-how-to-control-playback/ (making a rotary volume control)

## cnc

- baud rate should be set to 115200 (on mac)
- modelled on blender
