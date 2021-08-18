import os
import logging
import time
import math
import cv2 as cv
from queue import Queue
from settings import IMAGES_ROOT
from src.Vision import Vision
from src.debugModes import DEBUG_MODE
from src.ScreenCapturer import ScreenCapturer
from src.windowPrinter import WindowPrinter
from src.utilities import FpsPrinter
def init_logger():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def mainWindow(*args, **kwargs):
    '''Main window of program.

    :param args: args of object with implemented run method.
    :return:
    '''

    screenShooter = ScreenCapturer(debug=DEBUG_MODE.SCREEN_CAPTURE,
                                   windowPosition=(0,0,1940,1080))
    screenShooter.start()

    fpsPrinter = FpsPrinter(0.5)
    windowPrinter = WindowPrinter(windowName="Bot",
                                  windowShowPoint=(2400, 20))
    while True:
        beginTime = time.time()
        for arg in args:
            arg.run()

        screenShot = screenShooter.getScreenShoot()
        windowPrinter.showImage(screenShot)

        endTime = time.time()
        fpsPrinter(beginTime, endTime)
        if cv.waitKey(11) & 0xFF == ord('q'):
            screenShooter.stop()
            cv.destroyAllWindows()
            break


if __name__ == '__main__':
    mainWindow()

    pass
