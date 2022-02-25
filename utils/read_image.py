import os
import sys

import cv2
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def read_image(image_path, show = True, module : str = "", cvtColor : bool = False):
    # complete the function
    if module == "opencv":
        image = cv2.imread(image_path)
        try:
            if cvtColor:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return image
        except : 
            return image
        finally :
            if show:
                cv2.imshow("Image",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        image = Image.open(image_path)
        if show:
            image.show()
        return np.array(image)

def resize_image(image_path, show = True, module : str = "" ):
    if module == "opencv":
        image = cv2.imread(image_path)
        try:
            image = cv2.resize(image, (500, 600), interpolation = cv2.INTER_LINEAR) #780,540 random, INTER_NEAREST
            return image
        except : 
            return image
        finally :
            #plt.imshow(image)
            if show:
                cv2.imshow("Image",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        image = Image.open(image_path)
        if show:
            image.show()
        return np.array(image)

def show_image(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# image_path = "C:\\vishruti\\OCR Calculator\\ocr-calculator\\Images\\bodmas.jpeg"
# image = resize_image(image_path, show=False)
# show_image(image)