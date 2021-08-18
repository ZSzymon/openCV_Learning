import os
import time
import numpy as np
import cv2
import mss
import pyautogui
import mss
import random
from win32api import GetSystemMetrics
from settings import BASE_DIR, IMAGES_ROOT

import ctypes

user32 = ctypes.windll.user32
screensize = 3840, 1080
print(screensize[0])
print(screensize[1])
sct = mss.mss()
dimensions_right = {
    'left': screensize[0] - 400,
    'top': 0,
    'width': 350,
    'height': 600
}
points = [
    #y, x
    [(0,60), (0,300) ],
    [(120, 450), (130, 460)],
    [(200, 450), (210, 460)],
    [(270, 450), (280, 460)]
]


def takeScreenShot():
    '''Place app in right up place.'''
    image = np.array(sct.grab(dimensions_right), np.uint8)
    #image = image[:, :, :-1]

    #image = pyautogui.screenshot()
    #image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    #image = image[1080-600: 1080, 1920-350 : 1920,  :]
    return image


def click():
    x, y = 3540, 300
    pyautogui.click(x=x, y=y)


def showIm(img, desc="desc"):
    cv2.imshow(desc, img)
    cv2.waitKey(11)


def averageColor(img):
    return img.mean(axis=0).mean(axis=0)


def printAvgColor(color):
    blank_image = np.zeros((100, 100, 3), np.uint8)
    blank_image[:, :, :] = color
    cv2.imshow("fea",blank_image)
    cv2.waitKey(10000)

def getNSquere(image, n):

    point = points[n]
    y1 = point[0][1]
    y2 = point[1][1]
    x1 = point[0][0]+200
    x2 = point[1][0]+300
    subImage = image[point[1], point[0], :]

    return subImage

def test_rectangleOnImage():
    ss = takeScreenShot()
    w = 350
    h = 600


    color = (0, 0, 0)
    # ss = cv2.rectangle(ss, points[choice][0], points[choice][1], color, 2)
    cv2.imshow("s", ss)
    cv2.waitKey(1000003)
    cv2.destroyWindow("s")



    subSS = getNSquere(ss, 0)
    cv2.imshow("ff", subSS)
    cv2.waitKey(111111)
    cv2.destroyWindow("ff")
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    while True:
        ss = test_rectangleOnImage()
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
