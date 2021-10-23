# https://gist.github.com/skt7/71044f42f9323daec3aa035cd050884e
# https://www.timpoulsen.com/2018/finding-the-dominant-colors-of-an-image.html
# https://www.pyimagesearch.com/start-here/

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from sklearn.cluster import KMeans


# img = cv2.imread(r"C:\Users\balma\Documents\Programming\Python\Learning-practice\flask\Histogram_Genie_Dominant_Color\app\static\uploads\colors.jpg")
# cv2.imshow('image',img)
# cv2.waitKey()
# # # print(img)

CLUSTERS = None
IMAGE = None
COLORS = None
LABELS = None

def run_img_func(img):
    img = cv2.imread(img)
    # print(img)

    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    img = img.reshape((img.shape[0] * img.shape[1],3))

    
    
    kmeans = KMeans(n_clusters = 3)
    kmeans.fit(img)
    COLORS = kmeans.cluster_centers_
    
    LABELS = kmeans.labels_
    return COLORS.astype(int)

colors = run_img_func(r"C:\Users\balma\Documents\Programming\Python\Learning-practice\flask\Histogram_Genie_Dominant_Color\app\static\uploads\colors.jpg")
print(colors)
    # # cv2.imshow('image',img)
    # # cv2.waitKey() 
    # # cv2.destroyAllWindows()
    # img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # #get rgb values from image to 1D array
    # r, g, b = cv2.split(img2)
    # r = r.flatten()
    # g = g.flatten()
    # b = b.flatten()

    # #plotting 
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # ax.scatter(r, g, b)
    # plt.show()

# def print_img_test(img):
#     print
