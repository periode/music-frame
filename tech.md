# tech

## hardware

### main

- exciter: [dayton audio - daex25fhe-4](https://www.soundimports.eu/en/dayton-audio-daex25fhe-4.html) - 8.95e
- controller: [arduino nano](
https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829
) - 4.95
- amplifier: [lm386 module](
https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829
) - 2.95
- storage: [sd card module](
https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829
) - 3.50

### alternative

- integrated sd + dac: [yx5300](https://www.ebay.de/itm/YX5300-MP3-Musik-Player-Modul-Serial-UART-TTL-Module-Arduino-Raspberry-YX6300/253998552373?hash=item3b237e5535:g:0MMAAOSwWIJb-t2i)
- esp32 board: [wemos pro](https://docs.wemos.cc/en/latest/d32/d32_pro.html)
- other amplifier: [pam8403](https://www.banggood.com/5pcs-PAM8403-Miniature-Digital-USB-Power-Amplifier-Board-2_5V-5V-p-918227.html?rmmds=buy&cur_warehouse=CN)

## software

- playback of WAV files from SD Card: [TMRpcm](https://github.com/TMRh20/TMRpcm)


## notes

- larger surface provides a fuller, slightly louder sound
- PAM8403 provides much louder sound, but with hiss:
    - fixes for hiss: add wo 1kohm resistors between Arduino's TX/RX and SD CARD

https://www.raspberrypi.org/forums/viewtopic.php?t=232159
https://forum.arduino.cc/index.php?topic=248426.0
https://forum.arduino.cc/index.php?topic=554100.0
https://www.eevblog.com/forum/beginners/noise-form-pam8403-amplifier-board/ (low pass filter)
https://www.ebay.com/itm/202799600574 audio transformators