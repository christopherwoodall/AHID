#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import PIL
import io
import base64
import requests
import pyscreenshot as ImageGrab
import pygetwindow as gw
import pyautogui as pag


class ScreenShot:
    def grab(self, encoded=True):
        game = gw.getWindowsWithTitle('FLASH')[0]
        game.activate()
        im = ImageGrab.grab()
        im_crop = im.crop((
            int(game.left),
            int(game.top),
            int(game.width),
            int(game.height)
        ))
        if encoded:
            return self.encode(im_crop)

    def encode(self, img):
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        buffered.seek(0)
        img_byte = buffered.getvalue()
        #img_str = "data:image/png;base64," + base64.b64encode(img_byte).decode()
        #return base64.b64encode(img_byte).decode()
        return base64.urlsafe_b64encode(img_byte).decode()


def sendFrame(frame):
    URL = "http://192.168.137.19/stream.php"
    PARAMS = {'code': frame}
    r = requests.post(url = URL, data = PARAMS)
    #data = r.json()
    #print(data)
    print(r)
    print(r.text)


def main():
    capture = ScreenShot()
    frame = capture.grab()
    sendFrame(frame)

if __name__ == '__main__':
    main()

