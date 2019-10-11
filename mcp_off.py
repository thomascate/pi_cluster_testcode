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
