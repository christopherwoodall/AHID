#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import re
import sys
import time

from pathlib import Path

import numpy as np
import cv2


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



def Detect(frame):
    frame_bytes = base64.urlsafe_b64decode(frame)
    frame_arr   = np.frombuffer(frame_bytes, dtype=np.uint8)
    frame_cv    = cv2.imdecode(frame_arr, flags=cv2.IMREAD_GRAYSCALE)
    #frame_cv    = cv2.imdecode(frame_arr, flags=cv2.IMREAD_COLOR)
    grayframe = frame_cv
    #grayframe    = cv2.cvtColor(frame_cv, cv2.COLOR_BGR2GRAY)
    #grayframe   = cv2.cvtColor(frame_cv, cv2.COLOR_GRAY2BGR)

    #good = np.array(PIL.Image.open('good.png'))
    img = cv2.imread('good.png', cv2.IMREAD_GRAYSCALE)

    # creating the SIFT algorithm
    #sift = cv2.SIFT_create()
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp_image, desc_image =sift.detectAndCompute(img, None)

    # initializing the dictionary
    index_params = dict(algorithm = 0, trees = 5)
    search_params = dict()

    # by using Flann Matcher
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # find the keypoints and descriptors with SIFT
    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)

    # finding nearest match with KNN algorithm
    matches= flann.knnMatch(desc_image, desc_grayframe, k=2)

    good_points=[]

    for m, n in matches:
        #append the points according
        #to distance of descriptors
        #if(m.distance < 0.6*n.distance):
        #    good_points.append(m)
        #print(m.distance)
        #print(n.distance)
        good_points.append(m)
    #print(good_points)
    # maintaining list of index of descriptors
    # in query descriptors
    query_pts = np.float32([kp_image[m.queryIdx]
                    .pt for m in good_points]).reshape(-1, 1, 2)

    # maintaining list of index of descriptors
    # in train descriptors
    train_pts = np.float32([kp_grayframe[m.trainIdx]
                    .pt for m in good_points]).reshape(-1, 1, 2)

    # finding  perspective transformation
    # between two planes
    matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)

    # ravel function returns
    # contiguous flattened array
    matches_mask = mask.ravel().tolist()
    # initializing height and width of the image
    h, w = img.shape

    # saving all points in pts
    pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)

    # applying perspective algorithm
    dst = cv2.perspectiveTransform(pts, matrix)
    # using drawing function for the frame
    #homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)

    x,y = int(dst[0][0][0])-12, int(dst[0][0][1])-12

    Mouse(x,y)
    #self.mouse.move(x,y)

    # showing the final output
    # with homography
    #cv2.imshow("Homography", homography)
    #cv2.waitKey(0)
    #time.sleep(1)


if __name__ == '__main__':
    frame = sys.argv[1]
    Detect(frame)

