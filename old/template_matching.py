import os
import time
import numpy as np
import cv2
import mss
from settings import BASE_DIR, IMAGES_ROOT


def get_photo_path(name):
    return os.path.join(IMAGES_ROOT, name)


def calcPercentage(msk):
    '''
	returns the percentage of white in a binary image
	'''
    height, width = msk.shape[:2]
    num_pixels = height * width
    count_white = cv2.countNonZero(msk)
    percent_white = (count_white / num_pixels) * 100
    percent_white = round(percent_white, 2)
    return percent_white

def calculate_area2(photoName):
    image = cv2.imread(get_photo_path(photoName))
    #original = image.copy()

    lower = np.array([36, 25, 25], np.uint8)
    upper = np.array([70, 255, 255], np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    percentage = calcPercentage(mask)
    return percentage

def calculate_area(photoName):
    image = cv2.imread(get_photo_path(photoName))
    original = image
    img = mss.mss().shot()

    cv2.waitKey(1)

    lower = np.array([36, 25, 25], np.uint8)
    upper = np.array([70, 255, 255], np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    area = 0
    for c in cnts:
        area += cv2.contourArea(c)
        cv2.drawContours(original,[c], 0, (0,0,0), 2)
    cv2.imshow("original", original)
    cv2.waitKey()
    return area

if __name__ == '__main__':
    calculate_area(f"sc1.jpg")
    pass