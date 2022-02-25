import sys
sys.path.insert(0, "A:\\Pending Projects\\OCR Calculator\\ocr-calculator\\utils")

from preprocess_input import Preprocess
from read_image import *
from tensorflow.keras.models import load_model

import imutils
from imutils.contours import sort_contours
import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocessInput(filename : str = "", filter_size : int = 5, show = False):
    preprocess_data = Preprocess(filename, filter_size)
    preprocess_data.readImage()
    preprocess_data.BGR2GRAY()
    preprocess_data.add_filter(gaussian = True)
    preprocess_data.add_threshholding()
    preprocess_data.add_dilation()
    preprocess_data.get_edges()
    images = preprocess_data.findContours(show=show)

    return images

def read(image_path):
    return resize_image(image_path,show = False, module = "opencv")


def BGR2GRAY(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def get_prediction(image_path, show = False):
    chars = []
    img = read(image_path)
    img_gray = BGR2GRAY(img)
    model = load_model("A:\Pending Projects\OCR Calculator\ocr-calculator\modelling\maths_symbol_and_digit_recognition.h5")
    contours = preprocessInput(image_path)
    contours = sort_contours(contours, method="left-to-right")[0]
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'add', 'div', 'mul', 'sub']

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        if 20<=w and 30<=h:
            roi = img_gray[y:y+h, x:x+w]
            thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            (th, tw) = thresh.shape
            if tw > th:
                thresh = imutils.resize(thresh, width=32)
            if th > tw:
                thresh = imutils.resize(thresh, height=32)
            (th, tw) = thresh.shape
            dx = int(max(0, 32 - tw)/2.0)
            dy = int(max(0, 32 - th) / 2.0)
            padded = cv2.copyMakeBorder(thresh, top=dy, bottom=dy, left=dx, right=dx, borderType=cv2.BORDER_CONSTANT,
                                       value=(0, 0, 0))
            padded = cv2.resize(padded, (32, 32))
            padded = np.array(padded)
            padded = padded/255.
            padded = np.expand_dims(padded, axis=0)
            padded = np.expand_dims(padded, axis=-1)
            pred = model.predict(padded)
            pred = np.argmax(pred, axis=1)
            print(pred)
            label = labels[pred[0]]
            chars.append(label)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(img, label, (x-5, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
    if show : 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("Predicted Image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    e = ''
    for i in chars:
        if i=='add':
            e += '+'
        elif i=='sub':
            e += '-'
        elif i=='mul':
            e += '*'
        elif i=='div':
            e += '/'
        else:
            e += i
    return e

