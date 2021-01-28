import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

def pil2cv(imgPIL: Image) -> np.ndarray:
    imgCV_BGR = np.array(imgPIL, dtype=np.uint8)[:, :, ::-1]
    return imgCV_BGR

def cv2pil(imgCV: np.ndarray) -> Image:
    imgCV_RGB = imgCV[:, :, ::-1]
    imgPIL = Image.fromarray(imgCV_RGB)
    return imgPIL
