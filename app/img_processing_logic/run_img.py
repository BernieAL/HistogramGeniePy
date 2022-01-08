# https://gist.github.com/skt7/71044f42f9323daec3aa035cd050884e
# https://www.timpoulsen.com/2018/finding-the-dominant-colors-of-an-image.html
# https://www.pyimagesearch.com/start-here/



# https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71

from scipy.sparse import dok
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os



#COLOR IDENTIFICATION SECTION
#here we identify colors from an image and display top colors as pie chart

#first we define function to convert rgb to hex, so we can use them as labels for chart
# On reading the color which is in RGB space, we return a string. {:02x} simply displays the hex value for the respective color.
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]),int(color[1]),int(color[2]))


#define a method that will get image into python as rgb space
#read file in using imread and then change its color space before returning it
def get_image(image_path):
    image=cv2.imread(image_path)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image


#image is the target to extract colors from
# total num of colors we want to extract
# show chart is boolean that devides whether to show pie chart or not
def get_colors(image,number_of_colors,show_chart):
    #resize image to 600 * 400 to reduce the amount of pixels and reduce time needed to extract colors from image
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

    #kmeans algo creates cluters based on supplied count of clusters
    #we form clusters of colors that will be our top colors
    #we then fit and predict on the same image to extract the prediction into variable labels
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)


    #Use Counter to get all the labels
    counts = Counter(labels)
    #to find all colors we use CLf.cluster_centers
    center_colors = clf.cluster_centers_
    #ordered_colors iterates over the keys present in count, and divides each value by 255
    ordered_colors = [center_colors[i] for i in counts.keys()]
    #get hex color, multiply by 255 using RGB2HEX since we just divided by 255
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    #get rgb color
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    #if true, we plot pie char with each portion defined using count.values()
    #pie chart labels as hex_colors and colors as ordered_colors
    if(show_chart):
        plt.figure(figsize = (8,6))
        plt.pie(counts.values(),labels = hex_colors, colors=hex_colors)

    return hex_colors

# https://www.cined.com/film-color-schemes-cinematic-color-design/
# https://coolors.co/image-picker
# https://planetcalc.com/7661/
#def get_complimentary():
# https://stackoverflow.com/questions/40233986/python-is-there-a-function-or-formula-to-find-the-complementary-colour-of-a-rgb
#this function will calculate the complimentary colors of the dominant colors to be returned along with dom colors in run_main


#def get_analogous

#def get_tradiac

#def get_split











#driver for all image processing functions
#takes in original target image and passes to corresponding images
#returns dominant color values and complementary 

def run_main(image):
    
    dominant_colors = (get_colors(get_image(image),2,True))
    return dominant_colors
    # complimentary_colors = (dominant_colors)
    # return dominant_colors,complimentary_colors


# image = (r"C:\Users\balma\Documents\Programming\Python\Learning-practice\flask\Histogram_Genie_Dominant_Color\app\static\uploads\colors.jpg")
# print(get_colors(get_image(image),2,True))


