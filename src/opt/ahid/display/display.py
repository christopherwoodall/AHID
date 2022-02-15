#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

## IMPORTS ##
import time
import random
import subprocess

from colorsys import hsv_to_rgb
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789


## DISPLAY ##
BAUDRATE = 64000000

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

spi = board.SPI()

disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=240,
    height=240,
    x_offset=0,
    y_offset=80,
    rotation=180,
)


# Backlight
backlight = digitalio.DigitalInOut(board.D26)
backlight.switch_to_output()


# Input pins:
button_A = digitalio.DigitalInOut(board.D5)
button_A.direction = digitalio.Direction.INPUT

button_B = digitalio.DigitalInOut(board.D6)
button_B.direction = digitalio.Direction.INPUT

button_L = digitalio.DigitalInOut(board.D27)
button_L.direction = digitalio.Direction.INPUT

button_R = digitalio.DigitalInOut(board.D23)
button_R.direction = digitalio.Direction.INPUT

button_U = digitalio.DigitalInOut(board.D17)
button_U.direction = digitalio.Direction.INPUT

button_D = digitalio.DigitalInOut(board.D22)
button_D.direction = digitalio.Direction.INPUT

button_C = digitalio.DigitalInOut(board.D4)
button_C.direction = digitalio.Direction.INPUT


# Create blank image for drawing.
height = disp.width
width = disp.height
image = Image.new("RGB", (width, height))

print( height, width )
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)



def toggle_backlight():
    backlight.value = not backlight.value


def clear_screen():
    #disp.fill(0)
    #disp.write()
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

toggle_backlight()
#clear_screen()



# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)


# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
font = ImageFont.truetype("/opt/ahid/fonts/perfect_dos_vga_437.ttf", 18)
#font = ImageFont.load_default()


while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)


    # Shell scripts for system monitoring from here:
    # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d' ' -f1"
    IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
    Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}'"  # pylint: disable=line-too-long
    Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")

    # Write four lines of text.
    y = top
    #print(y)
    draw.text((x, y), IP, font=font, fill="#FFFFFF")

    y += font.getsize(IP)[1]
    #print(font.getsize(IP)[1])
    draw.text((x, y), CPU, font=font, fill="#FFFF00")

    y += font.getsize(CPU)[1]
    #print(font.getsize(CPU)[1])
    draw.text((x, y), MemUsage, font=font, fill="#00FF00")

    y += font.getsize(MemUsage)[1]
    #print(font.getsize(MemUsage)[1])
    draw.text((x, y), Disk, font=font, fill="#0000FF")

    y += font.getsize(Disk)[1]
    #print(font.getsize(Disk)[1])
    draw.text((x, y), Temp, font=font, fill="#FF00FF")


    test = '123456789012345678901234'
    y += font.getsize(Temp)[1]
    #print(font.getsize(Temp)[1])
    draw.text((x, y), test, font=font, fill="#FF00FF")

    #print(font.getsize(test)[1])

    # Display image.
    disp.image(image)
    time.sleep(1)




class Display:
    def __init__(self):
        BAUDRATE = 64000000

        cs_pin = digitalio.DigitalInOut(board.CE0)
        dc_pin = digitalio.DigitalInOut(board.D25)
        reset_pin = digitalio.DigitalInOut(board.D24)

        spi = board.SPI()

        disp = st7789.ST7789(
            spi,
            cs=cs_pin,
            dc=dc_pin,
            rst=reset_pin,
            baudrate=BAUDRATE,
            width=240,
            height=240,
            x_offset=0,
            y_offset=80,
            rotation=180,
        )
        # Backlight
        backlight = digitalio.DigitalInOut(board.D26)
        backlight.switch_to_output()


        # Input pins:
        button_A = digitalio.DigitalInOut(board.D5)
        button_A.direction = digitalio.Direction.INPUT

        button_B = digitalio.DigitalInOut(board.D6)
        button_B.direction = digitalio.Direction.INPUT

        button_L = digitalio.DigitalInOut(board.D27)
        button_L.direction = digitalio.Direction.INPUT

        button_R = digitalio.DigitalInOut(board.D23)
        button_R.direction = digitalio.Direction.INPUT

        button_U = digitalio.DigitalInOut(board.D17)
        button_U.direction = digitalio.Direction.INPUT

        button_D = digitalio.DigitalInOut(board.D22)
        button_D.direction = digitalio.Direction.INPUT

        button_C = digitalio.DigitalInOut(board.D4)
        button_C.direction = digitalio.Direction.INPUT

        # Create blank image for drawing.
        height = disp.width
        width = disp.height
        image = Image.new("RGB", (width, height))

        print( height, width )
        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)



class Viewport:
    def __init__(self):
        ...

