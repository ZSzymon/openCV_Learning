import cv2 as cv

class WindowPrinter:
    isMoved = False

    def __init__(self, windowName, windowShowPoint=(2000, 0)):
        self.windowName = windowName
        self.windowShowPoint = windowShowPoint
        x, y = windowShowPoint
        self.moveWindow(self.windowName, x, y)

    def moveWindow(self, windowName, x, y):
        cv.namedWindow(windowName)  # Create a named window
        cv.moveWindow(windowName, x, y)  # Move it to (x,y)

    def showImage(self, img):
        try:
            cv.imshow(self.windowName, img)
        except Exception as e:
            pass