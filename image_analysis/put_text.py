# cv2では日本語使えないので
from typing import Tuple
import numpy as np
import cv2
from image_analysis.pillow2cv import *
from PIL import Image, ImageDraw, ImageFont

def cv2_put_text(image: np.ndarray, text: str, org: Tuple[int], fontFace, fontScale: int, color: Tuple[int]) -> np.ndarray:

    x, y = org
    b, g, r = color
    colorRGB = (r, g, b)
    imgPIL = cv2pil(image)
    draw = ImageDraw.Draw(imgPIL)
    fontPIL = ImageFont.truetype(font = fontFace, size = fontScale)
    draw.text(xy = (x, y), text = text, fill = colorRGB, font = fontPIL)
    imgCV = pil2cv(imgPIL)

    return imgCV
