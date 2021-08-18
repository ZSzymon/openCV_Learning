import math
import time
import cv2 as cv

class FpsPrinter:
    def __init__(self, printEach=1):
        self.printEach = printEach
        self.nextTime = time.time()

    def printFps(self, beginTime, endTime):
        diff = endTime - beginTime
        if math.isclose(diff, 0, rel_tol=1e-6):
            FPS = 999
        else:
            FPS = 1.0 / diff

        if self.nextTime < time.time():
            print(f'FPS: {FPS}')
            self.nextTime = time.time() + self.printEach

    def __call__(self, beginTime, endTime):
        self.printFps(beginTime, endTime)
