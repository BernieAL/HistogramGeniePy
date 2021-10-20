
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2


# img = cv2.imread(r"C:\Users\balma\Documents\Programming\Python\Learning-practice\flask\Histogram_Genie_Dominant_Color\app\test.jpg")
# print(img)



def run_img_func(img):
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #get rgb values from image to 1D array
    r, g, b = cv2.split(img2)
    r = r.flatten()
    g = g.flatten()
    b = b.flatten()

    #plotting 
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(r, g, b)
    plt.show()