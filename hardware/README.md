# hardware

## electronics

the computer used is a [raspberry pi zero w 2](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/).

the audio exciters is a [dayton - DAEX13CT-4](https://www.variant-hifi.de/produkt/exciters/dayton-audio-daex13ct4-1416.html), with 4 Ohm [impedance](http://www.learningaboutelectronics.com/Articles/What-is-speaker-impedance) and 3 W RMS output - since the amp only provides 3W, having with significantly more watts (e.g. 10) doesn't make an audible difference.

connecting the computer and the output device is the [adafruit stereo speaker bonnet](https://www.adafruit.com/product/3346), both a DAC and amplifier, providing 3W output.

### alternatives

- battery version: [pisugar2](https://www.tindie.com/products/pisugar/pisugar2-battery-for-raspberry-pi-zero/)
- raspi amp: [hifiberry miniamp](https://www.hifiberry.com/shop/boards/miniamp/)
- raspi amp: [audio shim amp](https://thepihut.com/collections/raspberry-pi-audio-hats/products/audio-amp-shim-3w-mono-amp)
- controller: [arduino nano](https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829) - 4.95
- arduino amplifier: [lm386 module](https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829) - 2.95
- arduino storage: [sd card module](https://www.ebay.de/itm/Nano-ATmega-328-Board-CH340-USB-Chip-Arduino-Kompatibel/252742123829) - 3.50
- arduino integrated sd + dac: [yx5300](https://www.ebay.de/itm/YX5300-MP3-Musik-Player-Modul-Serial-UART-TTL-Module-Arduino-Raspberry-YX6300/253998552373?hash=item3b237e5535:g:0MMAAOSwWIJb-t2i)
- esp32 board: [wemos pro](https://docs.wemos.cc/en/latest/d32/d32_pro.html)

## board

### frame

the frame is made both of __8mm plywood__ and __2.5mm acrylic__. the 8mm wood thickness is better for bass response and resists better to warping (6mm warps easily, and 10mm might sound a bit more muffled). the acrylic is used to cover the back of the frame.

the dimensions of the front board iare 420mm \* 260mm \* 8mm.

one suggested finish is pickling (brown or white) as a base layer and linseed oil as a top layer.

### cad

the most recent CAD (fusion) file can be found [here](models/poglos_main_board_20211121.f3d).