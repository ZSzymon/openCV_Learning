import time
from unittest import TestCase
import cv2 as cv
from src.ScreenCapturer import ScreenCapturer
from src.debugModes import DEBUG_MODE
from src.utilities import FpsPrinter
from src.windowPrinter import WindowPrinter
import main

class TestScreenCapturer(TestCase):

    def testMainWindow(self):
        '''Main window of program.

        :param args: args of object with implemented run method.
        :return:
        '''
        mainFunction = main.mainWindow
        mainFunction()
