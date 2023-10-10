#spi code
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#spi code
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 12
PIXEL_ORDER = neopixel.GRB
#COLORS = (0xFF0000, 0x00FF00, 0x0000FF)
DELAY = 0.1
color = [0xFF,0x00, 0x00]
increment = 12
LED_COUNT = 12  # Number of LEDs in your external WS2812 LED ring
BRIGHTNESS = 1.0

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False
)

while True:
    """for color in COLORS:
        for i in range(NUM_PIXELS):
            pixels[i] = color
            pixels.show()
            time.sleep(DELAY)
            pixels.fill(0)"""
    color[0] += increment

    if color[0] >= 255:
        color[0] = 255
        increment = -12

    if color[0] <= 0:
        color[0] = 0
        increment = 12

    # Fill the entire WS2812 LED ring with the same color
    for i in range(LED_COUNT):
        pixels[i] = tuple(color)

    pixels.show()
    time.sleep(0.01)













        
