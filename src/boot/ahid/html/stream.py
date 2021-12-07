#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
from pathlib import Path

class Mouse:
    def __init__(self):
        self.device = Path("/dev/hidg1")


def main():
    ...

if __name__ == '__main__':
    frame = sys.argv[1]
    Path("/boot/ahid/html/debug.txt").write_text(frame)
    #main()


'''
#move
report = bytearray(4)
x,y = -80, 60
report[1] = x & 0xFF
report[2] = y & 0xFF
mouse.write_bytes(report)
mouse.write_bytes(bytearray(4))
time.sleep(0.69)
#click
report = bytearray(4)
report[0] = 0x01
mouse.write_bytes(report)
mouse.write_bytes(bytearray(4))
time.sleep(0.69)
'''
