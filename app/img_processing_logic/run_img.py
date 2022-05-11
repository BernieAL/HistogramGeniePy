# https://gist.github.com/skt7/71044f42f9323daec3aa035cd050884e
# https://www.timpoulsen.com/2018/finding-the-dominant-colors-of-an-image.html
# https://www.pyimagesearch.com/start-here/



# https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71


import json
import colorsys
from scipy.sparse import dok
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
from colorthief import ColorThief


#color thief resource 
# https://github.com/fengsp/color-thief-py

#hilo and complement resource
# https://stackoverflow.com/a/40234924


#COLOR IDENTIFICATION SECTION
#here we identify colors from an image and display top colors as pie chart

#this is hardcoded in for testing this file without running the server
#the actual image path will be passed in from main.py
image_path = (r"C:\Users\balma\Documents\Programming\Python\Learning-practice\flask\Histogram_Genie_Dominant_Color\app\static\uploads\colors.jpg")



#define a method that will get image into python as rgb space
#read file in using imread and then change its color space before returning it
def get_image(image_path):
    image=cv2.imread(image_path)
    image_as_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # print(image_as_rgb)

def get_dominant_and_palette(image_path):

    color_thief = ColorThief(image_path)
    dom_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=5)
    # print(dom_color)
    # print(palette)
    return dom_color,palette

def hilo(a,b,c):

    if c < b: b, c = c, b
    if b < a: a, b = b, a
    if c < b: b, c = c, b
    return a + c

def complement(color):
    #unpacks colors sequentially from color tuple
    r,g,b = color
    
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))

#use palette to generate complimentary colors
#traverse tuples in palette
#for each tuple (color), get its complimentary color by calling complement(color)
def get_complementary(palette):
    complementary_vals = []
    counter = 0
    for color in palette:
        counter+=1
       
        complementary_vals.append(complement(color))
    print(f'original palette colors {palette}')
    print(f'complementary{complementary_vals}')        


get_image(image_path)
dom_color = (get_dominant_and_palette(image_path))[0]
palette = (get_dominant_and_palette(image_path))[1]
get_complementary(palette)



def run_main(image):
    # dominant_colors = (get_colors(get_image(image)))
    
    # # return dominant_colors
    # complimentary_colors = (dominant_colors)
    # # print(f"COMPLIMENTARY COLORS{complimentary_colors}")

    # colors = {
    #     "dominant":dominant_colors,
    #     "complimentary":complimentary_colors,
    #     # "analog":analogous_colors,
    #     # "triadic":triadic,
    #     # "split":split
    # }
    # return dominant_colors,complimentary_colors


    pass
# run_main(image)
# print(get_colors(get_image(image),2,True))


# class ColorThief(object):

#     def __init__(self,file):
#         "one color thief instance for each image"

#     def color:
