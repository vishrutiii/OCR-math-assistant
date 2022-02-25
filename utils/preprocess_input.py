import numpy as np
import cv2
import matplotlib.pyplot as plt
# import utils

from PIL import Image
# from utils import *
from read_image import *
import warnings
warnings.filterwarnings('ignore')

def save_fig(image, filename : str = ""):
    plt.savefig(filename)

def filter(gray_image,filter_size):
    temp = []
    indexer = filter_size//2
    new_image = gray_image.copy()

    row, column = new_image.shape

    for i in range(row):
        for j in range(column):
            for k in range(i-indexer, i+indexer+1):
                for m in range(j-indexer, j+indexer+1):
                    if(k > -1) and (k<row):
                        if(m > -1) and (m<column):
                            temp.append(gray_image[k,m])
        temp.remove(gray_image[i,j])

        max_value = max(temp)
        min_value = min(temp)

        if gray_image[i,j] > max_value:
            new_image[i,j] = max_value
            
        elif gray_image[i,j] < min_value:
            new_image[i,j] = min_value

        temp = []

    return new_image.copy()

class Preprocess:
    def __init__(self,filename, filter_size):
        self.filename = filename
        self.filter_size = filter_size
        self.counter = 0
        self.gray_image = ""

    def show_save_plot(self,kwargs):
        if "show" in list(kwargs.keys()):
            if kwargs['show']:
                pass
        
        if "save" in list(kwargs.keys()):
            if kwargs['save']:
                try:
                    if "filename" in list(kwargs.keys()):
                        if kwargs['filename'] != "":
                            save_fig(self.gray_image, kwargs['filename'])
                        else:
                            raise AttributeError("Filename Not Found!")
                except:
                    raise ValueError("Enter the filename to save the figure!")

    def readImage(self, rotate = True):
        image = read_image(self.filename, show=False, module="opencv", cvtColor=False)

        if rotate : 
            image = np.rot90(image)

        image = cv2.resize(image, (500,600))
        self.image = image

    def BGR2HSV(self):
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.hsv_image = hsv_image

    def BGR2GRAY(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.gray_image = gray_image

    def add_filter(self, **kwargs):
        if "gaussian" in list(kwargs.keys()):
            if kwargs['gaussian']:
                self.gray_image = cv2.GaussianBlur(self.gray_image, (5,5), 5/6)
        else:

            self.gray_image = filter(self.gray_image, self.filter_size)
        self.show_save_plot(kwargs)
    
    def add_threshholding(self, **kwargs):
        self.gray_image = cv2.adaptiveThreshold(self.gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11, 22)
        self.show_save_plot(kwargs)

    def add_dilation(self, **kwargs):
        self.gray_image = cv2.morphologyEx(self.gray_image, cv2.MORPH_ERODE, np.ones((3,3)))
        self.show_save_plot(kwargs)

    def get_edges(self, **kwargs):
        self.gray_image = cv2.Canny(self.gray_image, 10, 150)
        self.show_save_plot(kwargs)

    def findContours(self,show = False, **kwargs):
        contours, hierarchy = cv2.findContours(self.gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        dr_im = np.copy(self.image)
        rectangle = []
        for contour, hier in zip(contours[1:], hierarchy[0][1:]):
            area = cv2.contourArea(contour)
            if area < 150 or hier[3] > 0: 
                continue
            x, y, w, h = cv2.boundingRect(contour)
            rectangle.append((x,y,w,h))
            cv2.rectangle(dr_im, (x, y), (x+w, y+h), (255,0,0), 1)
        if show:
            cv2.imshow("Contours Image",dr_im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        requiredImages = []
        for i, rect in enumerate(rectangle):
            x, y, w, h = rect
            cv2.imwrite("./Expression/%d.jpg" % i, (self.gray_image[y:y+h, x:x+w] != 255).astype("uint8")*255)
            im = (self.gray_image[y:y+h, x:x+w] != 255).astype("uint8")
            requiredImages.append(im)
        self.show_save_plot(kwargs)
        return requiredImages
# plot and save contours and figures


# def preprocess_input(filename : str = "", filter_size : int = 5):
#     preprocess_data = Preprocess(filename, filter_size)
#     preprocess_data.readImage()
#     preprocess_data.BGR2GRAY()
#     preprocess_data.add_filter(gaussian = True)
#     preprocess_data.add_threshholding()
#     preprocess_data.add_dilation()
#     preprocess_data.get_edges()
#     images = preprocess_data.findContours(show=False)

#     return images


# image_path = "A:\\Pending Projects\\OCR Calculator\\ocr-calculator\\Images\\bodmas.jpeg"
# images = preprocess_input(image_path)
# print(len(images))