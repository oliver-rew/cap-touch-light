# this program enables or disables an LED based on cap touch input, with a
# short OFF delay
import board
import touchio
import time
from digitalio import DigitalInOut, Direction

# init the cap touch input
touch_pad = board.A0
touch = touchio.TouchIn(touch_pad)

# init the LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

# how long we should wait after release to turn off the LED
off_delay = 0.5

# time the button was released
released = 0.0

# current state of touch sensor
touched = False

# last state of touch sensor
last = False

while True:
    # read the touch sensor
    touched = touch.value

    # if touched, turn on the LED
    if touched:
        led.value = True

    # if not touched but was previously, record the time of release
    elif last:
        released = time.monotonic()

    # if we have been released for the delay, disable the LED
    elif time.monotonic() - released > off_delay:
        led.value = False

    # record the previous state
    last = touched
