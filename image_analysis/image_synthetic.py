from typing import List
import cv2
import numpy as np
from image_analysis.error import *

# 画像合成
def synthetic(image1: np.ndarray, image2: np.ndarray, location: List[int]) -> np.ndarray:
    """synthtic two images

    :param image1: under image
    :type image1: np.ndarray
    :param image2: top image
    :type image2: np.ndarray

    :rtype: np.ndarray
    """
    try:
        if (len(image1.shape) != 3) or (len(image2.shape) != 3):
            raise RGBImageShapeException
        if len(location) != 2:
            raise LocationLengthException

        height, width = image2.shape[:2]
        first_y, first_x = location
        image1[first_y:first_y+height, first_x:first_x+width] = image2

        return image1

    except Exception as e:
        print(e)

def draw_vertical_line(image: np.ndarray, color: List[int], x_coordinate: int) -> np.ndarray:
    """draw vertical line on image

    :type image: np.ndarray
    :param color: line's color
    :type color: List[int]
    :param x_coordinate: line coordinate
    :type x_coordinate: int

    :rtype: np.ndarray
    """

    try:
        if (len(image.shape) != 3):
            raise RGBImageShapeException
        if len(color) != 3:
            raise ColorLengthException

        image[:, x_coordinate] = color

        return image

    except Exception as e:
        print(e)

def draw_horizontal_line(image: np.ndarray, color: List[int], y_coordinate: int) -> np.ndarray:
    """draw horizontal line on image

    :type image: np.ndarray
    :param color: line's color
    :type color: List[int]
    :param y_coordinate: line coordinate
    :type y_coordinate: int

    :rtype: np.ndarray
    """

    try:
        if len(image.shape) != 3:
            raise RGBImageShapeException
        if len(color) != 3:
            raise ColorLengthException

        image[y_coordinate, :] = color

        return image

    except Exception as e:
        print(e)
