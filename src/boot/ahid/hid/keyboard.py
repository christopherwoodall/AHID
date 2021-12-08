#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
from pathlib import Path

time.sleep(5)
device = Path("/dev/hidg1")

report = bytearray(4)
partial_wheel = 0
x,y = -70, 50

#move
report[1] = x & 0xFF
report[2] = y & 0xFF
report[3] = partial_wheel & 0xFF
device.write_bytes(report)
device.write_bytes(bytearray(4))

#click
report = bytearray(4)
report[0] = 0x01
device.write_bytes(report)
device.write_bytes(bytearray(4))


