import sys
import os
import math
import time

import cv2
from tkinter import *

import utils
from app import App

if __name__ == '__main__':
    root = Tk() # init the root 
    title = "OCR-Calculator" # title of the porgram
    App(root, title) # run the app