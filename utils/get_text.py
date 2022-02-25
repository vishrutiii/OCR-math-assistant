import os
import sys
import math
import time
from numpy.lib.type_check import imag
import pytesseract
import PIL
from PIL import Image
from utils.read_image import read_image
# from read_image import read_image
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\dev24\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

def get_text(filename : str = ""):
    """
    It will take the input filename, and extract the input the maths text from it.
    """
    image = read_image(filename, show=False, module="PIL")

    text = pytesseract.image_to_string(image)
    return (text, image)