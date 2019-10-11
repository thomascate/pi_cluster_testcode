#!/usr/bin/env python3
import time

import board
import busio
import digitalio

from adafruit_mcp230xx.mcp23008 import MCP23008
i2c = busio.I2C(board.SCL, board.SDA)


mcp24 = MCP23008(i2c, address=0x24)
mcp21 = MCP23008(i2c, address=0x21)
mcp23 = MCP23008(i2c, address=0x22)
#mcp = MCP23008(i2c)
pin0 = mcp24.get_pin(0)
pin1 = mcp23.get_pin(0)
pin2 = mcp21.get_pin(0)

pin0.switch_to_output(value=False)
pin1.switch_to_output(value=False)
pin2.switch_to_output(value=False)

# Setup pin1 as an input with a pull-up resistor enabled.  Notice you can also
# use properties to change this state.

#pin1.value = True 
#print("pin1 on")
#time.sleep(600)

# Now loop blinking the pin 0 output and reading the state of pin 1 input.
sleep_time = 1
while True:
    # Blink pin 0 on and then off.
    pin0.value = True
    print("pin0 on")
    time.sleep(sleep_time)
    pin0.value = False
    print("pin0 off")

    pin1.value = True
    print("pin1 on")
    time.sleep(sleep_time)
    pin1.value = False
    print("pin1 off")

    pin2.value = True
    print("pin2 on")
    time.sleep(sleep_time)
    pin2.value = False
    print("pin2 off")

