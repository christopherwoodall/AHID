#!/usr/bin/env python3
import pyscreenshot as ImageGrab
import pygetwindow as gw
import pyautogui as pag
import os
import time
import PIL

import win32api, win32con
import numpy as np
import cv2

# https://medium.com/@martin.lees/image-recognition-for-automation-with-python-711ac617b4e5
# https://stackoverflow.com/questions/27343997/using-pil-python-image-library-to-detect-image-on-screen

class Screen:
    def __init__(self):
        ...


class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        win32api.SetCursorPos((x, y))

    def click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        print("click")

    def get_position(self):
        x, y = win32api.GetCursorPos()
        print(x, y)
        return x, y



image_path = os.getcwd() + '\\screenshots\\snap.png'

def findGame():
    game = gw.getWindowsWithTitle('FLASH')[0]
    game.activate()
    return game
def screenGrab(box):
    game = gw.getWindowsWithTitle('FLASH')[0]
    game.activate()
    im = ImageGrab.grab()
    im_crop = im.crop((
        int(box.left),
        int(box.top),
        int(box.width),
        int(box.height)
    ))
    im_crop.save(image_path, quality=100)
    #return im_crop
    return image_path



class SillyAI:
    def __init__(self):
        self.mouse = Mouse()
        self.screen = Screen()
        #target = np.array(PIL.Image.open('good.png'))

        self.target = cv2.imread('good.png', cv2.IMREAD_GRAYSCALE)
        self.game = findGame()
        #self.frame = np.array(screenGrab(self.game))
        #print(self.frame)
        while True:
            self.cheat()
            time.sleep(1)

    def get_frame(self):
        return cv2.imread(screenGrab(self.game))

    def cheat(self):
        img = self.target
        # creating the SIFT algorithm
        sift = cv2.SIFT_create()
        #sift = cv2.xfeatures2d.SIFT_create()
        # find the keypoints and descriptors with SIFT
        kp_image, desc_image =sift.detectAndCompute(img, None)
        # initializing the dictionary
        index_params = dict(algorithm = 0, trees = 5)
        search_params = dict()
        # by using Flann Matcher
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        # reading the frame
        frame = self.get_frame()

        # converting the frame into grayscale
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


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

        #print(pts)
        #print(matrix)
        # applying perspective algorithm
        dst = cv2.perspectiveTransform(pts, matrix)
        # using drawing function for the frame
        homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)

        x,y = int(dst[0][0][0])-12, int(dst[0][0][1])-12
        self.mouse.move(x,y)

        # showing the final output
        # with homography
        #cv2.imshow("Homography", homography)
        #cv2.waitKey(0)



letsgo = SillyAI()
#game_area = findGame()
#screenGrab(game_area)
#mousePos((game_area.left, game_area.top))
#https://www.geeksforgeeks.org/python-opencv-object-tracking-using-homography/
#https://medium.com/@martin.lees/image-recognition-for-automation-with-python-711ac617b4e5
