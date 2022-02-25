# import necessary files
import os
import sys
import time

import PIL
import cv2
import datetime
import tkinter.messagebox as msgs

from tkinter import *
from typing import Sized
from tkinter.filedialog import askopenfilename

from PIL import ImageTk
from time import time
from datetime import datetime


import warnings
warnings.filterwarnings('ignore')


#modules required to get our results
from utils import *
import utils
from modelling.prediction import get_prediction
from modelling import prediction

# path where all images will be stored
path_of_image = "C:\\vishruti\OCR Calculator\ocr-calculator\Images"
class App:
    """
    This class contains the front end part of our project, It will capture the image, and send to the ou server where processing will be done, and results will be get using 
    Output button. 

    Here we have Tkinter GUI module to do our task
    """
    def __init__(self, root, title, video_source = 0):
        self.root = root # init the root
        self.root.title(title) # get the title of the window
        self.root.geometry("600x800") # define the dimesions of the window
        self.root.minsize(600,800) # config the min dimesnions of the window
        self.root.maxsize(600,800) # config the max dimesions of the window
        self.canvas_width = 400 # width of the canvas window
        self.canvas_height = 300 # height of the canvas window
        self.video_source = video_source # select which video source, web cam, or any other camera source
        self.cameraOpen = False # pointer to check whether the camera is opne or not
        self.image_ = None # pointer that points to the image which will/ was opened
        self.filename = "" # filename

        # display the title of the program in the window
        self.title_window = Label(text = "OCR Calculator", font = "comicsansms 20 bold")
        self.title_window.pack(fill = Y,padx = 20, pady = 20)

        #create a canvas where we can display our images
        self.tkinter_canvas = Canvas(self.root, width = self.canvas_width, height = self.canvas_height, bg="white")
        self.tkinter_canvas.pack()

        # creating a frame where we will display our buttons, for functionality
        self.frame = Frame(self.root) # init the frame, it is like the div in html, where we will defining our button
        self.frame.pack(side=TOP)

        self.select_button = Button(self.frame, borderwidth=7, bg="black", fg="white", text="Select From Computer", font="comicsansms 13", command=self.openImage) # created a select button which will select the image from our local machine
        self.select_button.pack(side=TOP)

        self.showContours = Button(self.frame, borderwidth=7, bg="black", fg="white", text="Show Contours", font="comicsansms 13", command=self.showContour) # show contours button is used to plot the comtours in the image
        self.showContours.pack(side = TOP, pady=10, padx=10)

        self.predictions = Button(self.frame, borderwidth=7, bg="black", fg="white", text="Get Predictions", font="comicsansms 13", command=self.showPredictions) # predictions button will show the predictions of the problem
        self.predictions.pack(side = TOP, padx=10, pady=10)

        self.webcam_button = Button(self.frame, borderwidth=7, bg="black", fg="white", text="Open WebCam", font="comicsansms 13", command=self.openCamera) # webcam button is used to open the web camera of the local machine
        self.webcam_button.pack(side=RIGHT, pady=10, padx=10)

        self.snapshot = Button(self.frame, borderwidth=7, bg="black", fg="white", text="SnapShot", font="comicsansms 13", command=self.takeSnap) # snapshot is the button that is used to capture the images from the web camera
        self.snapshot.pack(side = RIGHT, pady=10, padx=10)

        # now we will initialize our output button which will show the output of our given input image
        self.output_frame = Frame(self.root)
        self.output_frame.pack()

        # output button that will pop up a message box with input and output
        self.output_button = Button(self.output_frame, borderwidth=7, bg="black", fg="white", text="GET OUTPUT", font="comicsansms 13", pady=20, padx=20, command=self.showOutput)
        self.output_button.pack(fill = X, pady = 60)

        # make the delay var, to refresh the page
        self.delay = 10

        # init the main loop of the program, to run the program
        self.root.mainloop()
        
    # funtion to open the image
    def openImage(self):
        # to refresh the page, to avoid overlapping
        if self.cameraOpen: # if our web camera is open, and we need to close it, so that we can open the image from our system
            self.closeCamera() # it will close the camera
        
        global file
        file = askopenfilename(defaultextension=".png", filetypes=[("JPG Image","*.jpg"), ("All Files", "."), ("PNG Image","*.png"),("JPEG Image","*.jpeg")]) # askopenfilename is  tkinter function to open the required image
        # if file is not selected then we define the image file is None
        if file == "":
            file = None
        else:
            title = os.path.basename(file) + "- OCR-Calculator" # this will gives the title to the window
            self.filename = os.path.abspath(file)
            self.root.title(title)
            img_ = PIL.Image.open(file) # open the image
            img_ = img_.resize((self.canvas_width, self.canvas_height)) # reszie the image in the dimension of camvas_width*canvas_height
            img = ImageTk.PhotoImage(image = img_) # it will convert PIL image to image that is supported by tkinter
            image_ = Label(image=img) # show in the image in window
            self.image_ = image_
            self.image_.image = img
            self.image_.place(x=97,y=78) # it will display the image at particulr coordinate
        print(self.filename)

    # show output function it will show the output of the given input
    def showOutput(self):
        try:
            if self.filename  != "":
                input_text = input_file(filename=self.filename)
                # input_text = "sin^2(x) + cos^2(x)"
                print(input_text)
                output_text = get_output(input_text)
                print(output_text)
                text = "Input : " + str(input_text) + "\nOutput : " + str(output_text[0])
                msgs.showinfo("Output",message=text ) # it will display our input and output
            else:
                msgs.showwarning("Error", "No Data Found!")
        except:
            # input_text = input_file(filename=self.filename)
            # print(input_text)
            msgs.showwarning("Error", "The program can't be executed.") # it will display when any error occur while getting the output.

    def openCamera(self):
        """
        This function will allows us to open the  web camera, we are opening the default camera in our local machine.
        """
        # it is used to refresh the page
        if self.image_ is not None:
            self.image_.config(image=None)
            self.image_.image = None
        
        # if camera is already open, then we will close the camera
        if self.cameraOpen:
            self.closeCamera()

        # to open the video using opencv
        video = cv2.VideoCapture(self.video_source)
        self.cameraOpen = True # pointer makes it true
        self.video = video
        # function to show the frame of video
        def show_frame(): 
            ret, frame = video.read()
            cv2image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(cv2image)
            img = img.resize((self.canvas_width, self.canvas_height))
            imgtk = ImageTk.PhotoImage(image = img)
            image_frames = Label(image=imgtk)
            image_frames.image = imgtk
            image_frames.place(x=97,y=78)
            image_frames.after(self.delay, show_frame)

        show_frame()
    
    # function to close the camera
    def closeCamera(self):
        self.video.release()
        cv2.destroyAllWindows()

    # function to take snapshot of the image
    def takeSnap(self):
        ret, frame_ = get_frame(self.video)
        if ret:
            curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S') #getting the current datetime
            filename = path_of_image + "\image_{}.jpg".format(str(curr_datetime)) # making the filepath with datetime
            cv2.imwrite(filename,frame_) # save the file using opencv
            cv2.imshow("maths_",cv2.cvtColor(frame_, cv2.COLOR_BGR2RGB)) # show the saved image, and convert the BGR image to RGB image
            print("File saved ")
            self.filename = filename
            print(self.filename)

    def showContour(self):
        filename = self.filename
        _ = prediction.preprocessInput(filename=filename,show=True)        

    def showPredictions(self):
        get_prediction(self.filename, show=True)

        
# this function is used to get the frame and used to save the image
# note: this function is out class, irrespective of the any other datatype
def get_frame(video):
    if video.isOpened():
        ret, frame = video.read()
        if ret:
            return (ret, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)) # convert the image into BGR
        else:
            return (ret, None)
    else:
        return (False, None)    


def input_file(filename : str = ""):
    """
    It will take the input filename, and extract the input the maths text from it.
    """
    
    return get_prediction(filename) 

def get_output(input_text : str = ""):
    """
    It will take input as a string and return the output of the given input mathematics problem
    """
    return utils.solver.output(input_text)