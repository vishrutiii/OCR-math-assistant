import os
import sys
import math

def create_file(filename : str = ""):
    f = open(filename, 'w')
    text = "Function, Input, Output\n"
    f.writelines(text)
    f.close()

def write_function(filename : str = "", f_name : str = "", input_fun : str = "", output_fun : str = ""):
    f = open(filename, 'a')
    text = "{}, {}, {}\n".format(f_name, input_fun, output_fun)
    f.writelines(text)
    f.close()

    #add abosulte path according to machines
filepath = "C:\\vishruti\\OCR Calculator\\ocr-calculator\\Data\\fun.txt"
create_file(filepath)
write_function(filepath,"Trigonometry","sin^2(x) + cos^2(x)","1" )
write_function(filepath,"Trigonometry","tan^2(x) + cot^2(x)","1" )
write_function(filepath,"Trigonometry","sec^2(x) + cosec^2(x)","1" )
