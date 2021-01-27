import cv2
import numpy as np

def generate_black(width: int, height: int) -> np.ndarray:
    """generate blask image

    :param width: image width
    :type width: int
    :param height: image height
    :type height: int

    :rparam: black image
    :rtype: np.ndarray
    """

    black = np.zeros(shape=(width, height, 0))
    return black

def generate_white(width: int, height: int) -> np.ndarray:
    """generate white image

    :param width: image width
    :type width: int
    :param height: image height
    :type height: int

    :rparam: white image
    :rtype: np.ndarray
    """

    black = np.zeros(shape=(width, height, 3))
    white = black + 255

    return white

def generate_red(width: int, height: int) -> np.ndarray:
    """generate red image

    :param width: image width
    :type width: int
    :param height: image height
    :type height: int

    :rparam: red image
    :rtype: np.ndarray
    """

    black = np.zeros(shape=(width, height, 3))
    red = [255, 0, 0][::-1]

    return red

def generate_green(width: int, height: int) -> np.ndarray:
    """generate green image

    :param width: image width
    :type width: int
    :param height: image height
    :type height: int

    :rparam: green image
    :rtype: np.ndarray
    """

    black = np.zeros(shape=(width, height, 3))
    green = black + [0, 255, 0][::-1]

    return green

def generate_blue(width: int, height: int) -> np.ndarray:
    """generate blue image

    :param width: image width
    :type width: int
    :param height: image height
    :type height: int

    :rparam: blue image
    :rtype: np.ndarray
    """

    black = np.zeros(shape=(width, height, 3))
    blue = black + [0, 0, 255][::-1]

    return blue
