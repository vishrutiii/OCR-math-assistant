## OCR-Calculator
This is aimed to develop an Optical Character Recognition (OCR) Calculator generating system which with the help of CNN’s and  Computer Vision Techniques, can prove to be a substantial tool to calculate a set of problems by automatically reading them off the image provided by the user through both the locally saved file or in live captioning through the device’s capturing component.

## Technologies used

Python
Numpy
Pandas 
Matplotlib
Seaborn
OpenCV
Pillow
Tensorflow (Keras)
Tkinter
JSON
math, os, sys, datetime
pytesseract

## Installation

```
pip3 install requirements.txt
```

## Workflow

![workflow](https://github.com/vishrutiii/OCRcalculator/blob/main/Images/workflow1.png?raw=true)
![workflow-pipeline](https://github.com/vishrutiii/OCRcalculator/blob/main/Images/workflow2.png?raw=true)

## Interface

Tkinter Interface

![interface](https://github.com/vishrutiii/OCRcalculator/blob/main/Images/tkinterinterface.png?raw=true)

## Image Preprocessing

Gaussian Blur Filter

Conservative Smoothing

Convert the image into a thresholding image

Dilate and get the edges of the image

Edge Detection

Get the contours of the image

Plot the contours in the image

## Modelling

![model](https://github.com/vishrutiii/OCRcalculator/blob/main/Images/model.png?raw=true)

![plot](https://github.com/vishrutiii/OCRcalculator/blob/main/Images/accuracyplot.png?raw=true)

## Output

In this image, we can the detection of text i.e., contoured image.

![output-contours](https://github.com/vishrutiii/OCRcalculator/blob/main/Images/outputbodmas.png?raw=true)

Image with prediction.
The image detecting all the text with numbers and signs.

![output](https://github.com/vishrutiii/OCRcalculator/blob/main/Images/outputbodmas2.png?raw=true)

## Licence

MIT
