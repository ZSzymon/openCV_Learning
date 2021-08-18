import cv2 as cv
import threading
import pyautogui
import numpy as np
import time
import settings
from .debugModes import DEBUG_MODE
from queue import LifoQueue
from mss import mss

class ScreenCapturer:

    __lock = threading.Lock()
    __screenShot = None
    ## variable showing need to take new screen shoot.
    takeNewScreenShot = True
    stopped = True

    def __init__(self, windowPosition=None, debug=None):
        """ Class takings screenshots of window with given position.
            It takes new screen shoot when previous was used by other object.
            This class is thread safe.

        :param windowPosition: (top, left, width, height)
        :param debug: DEBUG_MODE value
        """
        if windowPosition is None:
            windowPosition = {"top": 40, "left": 0,
                              "width": 800, "height": 640}
        else:
            assert len(windowPosition) == 4, "WindowPostion must be a tuple.\nExample (40, 0, 800, 640)"
            x, y, w, h = windowPosition
            windowPosition = {"top": x, "left": y,
                              "width": w, "height": h}
        self.windowPosition = windowPosition
        self.debug = debug

    def takeScreenShot(self):
        '''Taking new screen shoot.

        '''
        #screenShot = pyautogui.screenshot()
        #screenShot = np.array(screenShot)
        #screenShot = cv.cvtColor(screenShot, cv.COLOR_RGB2BGR)
        ## Convert RGB to BGR
        #screenShot = screenShot[:, :, ::-1].copy()
        with mss() as sct:

            screenShot = np.array(sct.grab(self.windowPosition))
            screenShot = np.array(screenShot)
            screenShot = cv.cvtColor(screenShot, cv.COLOR_RGB2BGR)
            screenShot = screenShot[:, :, ::-1].copy()
        return screenShot

    def updateScreenShoot(self, screenShot):
        '''setting new screenshot.

        '''
        with self.__lock:
            self.__screenShot = screenShot
            self.takeNewScreenShot = False

    def getScreenShoot(self):
        ''' Getting newest avaible screenshot.

        :return: screenshoot of window.
        '''
        with self.__lock:
            screenShot = self.__screenShot
            self.takeNewScreenShot = True
        return screenShot

    pass

    def start(self):
        print("Starting new thread.")
        self.stopped = False
        t = threading.Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        if self.debug == DEBUG_MODE.SCREEN_CAPTURE:
            print("Running thread.")
        while not self.stopped:
            ##make screenshot when it's obligated.
            if self.takeNewScreenShot:
                if self.debug == DEBUG_MODE.SCREEN_CAPTURE:
                    # print("Capturing new screenshot")
                    pass
                screenshot = self.takeScreenShot()
                self.updateScreenShoot(screenshot)
            else:
                if self.debug == DEBUG_MODE.SCREEN_CAPTURE:
                    # print("Have nothing to do.")
                    pass
                ###if not do nothing.
                pass
            if self.debug == DEBUG_MODE.SCREEN_CAPTURE:
                time.sleep(settings.SLEEP_TIME)
