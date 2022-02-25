import os
import sys
import time
import math

sys.path.insert(0, "A:\\Pending Projects\\OCR Calculator\\ocr-calculator\\solver")
from cv2 import TermCriteria_COUNT
import pandas as pd
import numpy as np
from bodmas import *


def output(input_text : str = ""):
    """
    It will take input as a string and return the output of the given input mathematics problem
    """
    cal_object = Calculator(input_text)

    return cal_object.result

# print(output("6+8*9"))