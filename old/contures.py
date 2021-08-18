import os
import time
import numpy as np
import cv2
import mss
from settings import BASE_DIR, IMAGES_ROOT
from grabscreen import grab_screen

class AutoBot:
    pass

def test():
    #if cv.waitKey(10) & 0xFF == ord('q'):
    #    break

    for i in range(100):
        image = grab_screen(region=(50+i, 100, 799, 449))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.Canny(image, threshold1=200, threshold2=300)
        cv2.imshow("img", image)
        time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def test2():
    image = grab_screen(region=(50, 100, 799, 449))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image, (3,3), 0)

    image = cv2.Sobel(src=image, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    cv2.imshow("img", image)

    cv2.waitKey(1)

def test3():
    path = os.path.join(IMAGES_ROOT, 'img.png')
    img = cv2.imread(path)
    # Display original image
    cv2.imshow('Original', img)
    cv2.waitKey(0)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=200, threshold2=200)  # Canny Edge Detection
    # Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test3()