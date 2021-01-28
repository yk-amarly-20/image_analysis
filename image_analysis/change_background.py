# 背景色を変換する

import cv2
import numpy as np
from image_analysis.error import *

def change_background(image: np.ndarray) -> np.ndarray:
    """change background color from black to white

    :param image: image whose background color is black
    :type image: np.ndarray

    :rtype: np.ndarray
    """

    try:
        if len(image.shape) != 3:
            raise RGBImageShapeException
        if image.shape[2] != 3:
            raise ColorLengthException

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        image[binary == 0] = 255

        return image

    except Exception as e:
        print(e)

def black_to_white(image: np.ndarray) -> np.ndarray:
    """change black color to white

    :type image: np.ndarray

    :rtype: np.ndarray
    """

    try:
        if len(image.shape) != 3:
            raise RGBImageShapeException
        if image.shape[2] != 3:
            raise ColorLengthException

        black = [0, 0, 0]
        white = [255, 255, 255]
        image[np.where((image == black).all(axis=2))] = white

        return image

    except Exception as e:
        print(e)
