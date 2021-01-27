from typing import List
import cv2
import numpy as np

# 画像合成
def synthetic(image1: np.ndarray, image2: np.ndarray, location: List[int]) -> np.ndarray:
    """synthtic two images

    :param image1: under image
    :type image1: np.ndarray
    :param image2: top image
    :type image2: np.ndarray

    :rtype: np.ndarray
    """
    height, width = image2.shape[:2]
    first_y, first_x = location
    image1[first_y:first_y+height, first_x:first_x+width] = image2

    return image1
