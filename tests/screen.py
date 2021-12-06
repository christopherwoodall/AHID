#!/usr/bin/env python3
import pyscreenshot as ImageGrab
import pygetwindow as gw
import pyautogui as pag
import os
import time
import PIL

def screenGrab(box):
    game = gw.getWindowsWithTitle('FLASH')[0]
    game.activate()
    im = ImageGrab.grab()
    image_path = os.getcwd() + '\\screenshots\\snap__' + str(int(time.time())) + '.png'
    #im.save(image_path)
    #im = PIL.Image.open(image_path)
    im_crop = im.crop((
        int(box.left),
        int(box.top),
        int(box.width),
        int(box.height)
    ))
    im_crop.save(image_path, quality=100)

def main():
    screenGrab()

if __name__ == '__main__':
    main()