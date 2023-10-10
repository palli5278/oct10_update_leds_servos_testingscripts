import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 12
PIXEL_ORDER = neopixel.GRB
LED_COUNT = 12
BRIGHTNESS = 1.0
spi = board.SPI()
position = 0

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False
)

def loop():
    global position

    for i in range(LED_COUNT):
        brightness = int(i * (255 / LED_COUNT)) // 2
        pixels[(i + position) % LED_COUNT] = (0, 0, brightness)

    pixels.show()
    position = (position + 1) % LED_COUNT
    time.sleep(0.1)

while True:
    loop()

