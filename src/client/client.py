#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import PIL
import pyscreenshot as ImageGrab
import pygetwindow as gw
import pyautogui as pag


class ScreenShot:
    def grab(self, encoded=True):
        game = gw.getWindowsWithTitle('FLASH')[0]
        game.activate()
        im = ImageGrab.grab()
        im_crop = im.crop((
            int(box.left),
            int(box.top),
            int(box.width),
            int(box.height)
        ))
        #im_crop.save(image_path, quality=100)
        if encoded:
            return self.encode(im_crop)

    def encode(self, img):
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        buffered.seek(0)
        img_byte = buffered.getvalue()
        img_str = "data:image/png;base64," + base64.b64encode(img_byte).decode()
        return img_str


capture = ScreenShot()
#frame = capture.grab()


'''
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
'''

