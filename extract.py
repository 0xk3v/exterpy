"""
Python Module to Extract Text from Given Images.
"""

import cv2
from PIL import Image


class Extractor():

    """Main class for Extractor Module """

    def __init__(self):
        """TODO: to be defined. """
        self.im = None

    def mark_region(self, imagE_path):
        """ Method to extract text """
        # type: ignore
        self.im = cv2.imread(imagE_path)

        self._gray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        self.blur = cv2.GaussianBlur(self._gray, (9, 9), 0)
        self.thresh = cv2.adaptiveThreshold(self.blur, 255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY_INV, 11, 30)
        # Dilate to combine adjacent text contours
        self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        self.dilate = cv2.dilate(self.thresh, self.kernel, iterations=4)

        # Find contours, highlight text areas, and extract ROIs
        self.cnts = cv2.findContours(
            self.dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.cnts = self.cnts[0] if len(self.cnts) == 2 else self.cnts[1]

        self.line_items_coordinates = []
        for c in self.cnts:
            area = cv2.contourArea(c)
            x, y, w, h = cv2.boundingRect(c)

            if y >= 600 and x <= 1000:
                if area > 10000:
                    image = cv2.rectangle(
                        self.im, (x, y), (2200, y+h), color=(255, 0, 255), thickness=3)
                    line_items_coordinates.append([(x, y), (2200, y+h)])

            if y >= 2400 and x <= 2000:
                image = cv2.rectangle(
                    self.im, (x, y), (2200, y+h), color=(255, 0, 255), thickness=3)
                line_items_coordinates.append([(x, y), (2200, y+h)])

        return image, line_items_coordinates
