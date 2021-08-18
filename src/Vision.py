import cv2 as cv
import numpy as np
from .debugModes import DEBUG_MODE


def getCenterPosition(rectangle):
    """Return center point of rectangle.

    :param rectangle: x, y, w, h.
    :return: center of given rectangle (x, y)
    """
    x, y, w, h = rectangle
    center_y = y + int(h / 2)
    center_x = x + int(w / 2)
    return center_x, center_y


class Vision:
    
    @staticmethod
    def resizePhoto(img, scale_percent):
        """ Resize given photo.

        :param img:
        :param scale_percent: scale in percent.
        :return: resized photo.
        """
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        return resized

    @staticmethod
    def getHeightWidth(img):
        """Get height and width of photo.

        :param img:
        :return: tuple of h,w
        """
        return img.shape[0], img.shape[1]

    @staticmethod
    def createBottomRight(top_left, img):
        """ Create botton right point with given top left point.

        :param top_left: (y, x) point
        :param img: nd.array type of image.
        :return: botton right point.
        """
        return top_left[0] + img.shape[0], top_left[1] + img.shape[1]

    @staticmethod
    def drawRectangleOn(img, topLeft, bottonRight, color=(0, 255, 0)):
        cv.rectangle(img, topLeft, bottonRight,
                     color=color, thickness=2, lineType=cv.LINE_4)

    pass

    @staticmethod
    def findClickPositions(img, sub_img, threshold=0.49,
                           marker_color=(255, 0, 255), line_color=(0, 255, 0), debug=None):
        subImg_h, subImg_w = Vision.getHeightWidth(sub_img)
        result = cv.matchTemplate(img, sub_img, cv.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        centerPoints = []
        if len(locations) > 0:
            # create the list of [x, y, w ,h]
            rectangles = []
            for loc in locations:
                x, y = loc
                rect = [int(x), int(y), subImg_w, subImg_h]
                rectangles.append(rect)
                rectangles.append(rect)
            rectangles, _ = cv.groupRectangles(rectangles, 1, 0.5)
            centerPoints = []
            for x, y, w, h in rectangles:
                topLeft = x, y
                bottomRight = x + w, y + h
                center_x, center_y = getCenterPosition((x, y, w, h))
                centerPoints.append((center_x, center_y))
                if debug == DEBUG_MODE.RECTANGLES:
                    Vision.drawRectangleOn(img, topLeft, bottomRight, line_color)
                elif debug == DEBUG_MODE.POINTS:
                    cv.drawMarker(img, (center_x, center_y), color=marker_color)
                elif debug == DEBUG_MODE.RECTANGLES | DEBUG_MODE.POINTS:
                    cv.drawMarker(img, (center_x, center_y), color=marker_color)
                    Vision.drawRectangleOn(img, topLeft, bottomRight, line_color)

            if debug:
                debugPhoto = Vision.resizePhoto(img, 50)
                cv.imshow("Matches", debugPhoto)
                cv.waitKey()

        return centerPoints