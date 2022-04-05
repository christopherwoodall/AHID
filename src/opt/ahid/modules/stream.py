#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import re
import sys
import time

from pathlib import Path

import numpy as np
import cv2

class DetectFaces:
    def __init__(self, image_bytes):
        self.frame_targets = b'0x0'
        frame_bytes = image_bytes
        frame_arr   = np.fromstring(frame_bytes, dtype=np.uint8)
        frame_cv    = cv2.imdecode(frame_arr, flags=cv2.COLOR_BGR2GRAY)

        faceCascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')
        #faceCascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_fullbody.xml')
        #bodyCascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_fullbody.xml')
        faces = faceCascade.detectMultiScale(
                frame_cv,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30)
        )
        if len(faces) > 0:
            print(f"Found {len(faces)} Faces!")
            for (x, y, w, h) in faces:
                cv2.rectangle(frame_cv, (x, y), (x+w, y+h), (0, 255, 0), 3)
            _, buf = cv2.imencode('.png', frame_cv)
            self.frame_targets = buf.tostring()


def Mouse(x, y):
    device = Path("/dev/hidg1")
    # Move
    report = bytearray(4)
    report[1] = x & 0xFF
    report[2] = y & 0xFF
    # Click
    #report = bytearray(4)
    #report[0] = 0x01
    #device.write_bytes(report)
    #device.write_bytes(bytearray(4))
    device.write_bytes(report)
    device.write_bytes(bytearray(4))
    print(f'{x},{y}')


#https://github.com/mrnugget/opencv-haar-classifier-training