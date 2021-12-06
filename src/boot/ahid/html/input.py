#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
from pathlib import Path


#time.sleep(3)

class Keyboard:
    def __init__(self):
        self.device = Path("/dev/hidg0")

    def send_key(self, key):
        report    = bytearray(8)
        report[3] = key
        self.write_report(report)
        self.write_report(bytearray(8))

    def write_report(self, report):
        self.device.write_bytes(report)

        #if type(report) is str:
        #    report = bytes(report, "utf-8")
        #with open('/dev/hidg0', 'rb+') as fd:
            #fd.write(report.encode())
            #fd.write(report)



def unlock():
    kb = Keyboard()
    # send e
    report = bytearray(8)
    report[3] = 0x14
    kb.write_report(report)
    time.sleep(0.69)
    #mouse
    mouse = Path("/dev/hidg1")
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
    # release e
    kb.write_report(bytearray(8))



pin   = sys.argv[1]

if pin == "unlock":
    ...
    kb = Keyboard()
    # send e
    report = bytearray(8)
    report[3] = 0x14
    kb.write_report(report)
    time.sleep(0.69)
    #mouse
    mouse = Path("/dev/hidg1")
    #move
    report = bytearray(4)
    x,y = -30, -60 #-80, -60
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
    # release e
    kb.write_report(bytearray(8))


else:
    unlock()
    #https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
    KEY_CODES = {
        '1': 0x1e,
        '2': 0x1f,
        '3': 0x20,
        '4': 0x21,
        '5': 0x22,
        '6': 0x23,
        '7': 0x24,
        '8': 0x25,
        '9': 0x26,
        '0': 0x27,
        'RETURN': 0x28,
    }

    codes = list(pin)
    hid   = Keyboard()

    for code in codes:
        hid.send_key(KEY_CODES[code])
        time.sleep(0.15)
    #hid.send_key(KEY_CODES['RETURN'])
    #hid.write_report(bytearray(8))


'''
# testing mouse
write_report(chr(1)+NULL_CHAR+chr(100)+chr(0)+NULL_CHAR)
time.sleep(2)
write_report(chr(1)+NULL_CHAR+chr(100)+chr(100)+NULL_CHAR)
time.sleep(2)
write_report(chr(1)+NULL_CHAR+chr(228)+chr(228)+NULL_CHAR)
'''

# NOTES
# https://gist.github.com/rmed/0d11b7225b3b772bb0dd89108ee93df0
# https://stackoverflow.com/a/66401242
# https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition/
# https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
# https://stackoverflow.com/questions/27075328/list-of-hex-keyboard-scan-codes-and-usb-hid-keyboard-documentation
# https://github.com/thagrol/pwdgen/blob/master/hidsetup.sh
# https://github.com/raspberrypisig/pizero-usb-hid-keyboard
# https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main/adafruit_hid
#
# HID Usage Tables for Universal Serial Bus (USB)
#   https://usb.org/sites/default/files/hut1_21.pdf
# https://www.usb.org/defined-class-codes
# https://www.usb.org/developers/hidpage/Hut1_12v2.pdf
## https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main/adafruit_hid

