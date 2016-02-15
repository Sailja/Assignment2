from pyimagesearch.transform import four_point_transform
import cv2
import numpy as np
import argparse
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
#ask the user to double click on four points
print("Click on four corners")

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
args = vars(ap.parse_args())
image = mpimg.imread(args["image"])

im=plt.imread(args["image"])

#taking input from usser
ax = plt.gca()
fig = plt.gcf()
implot = ax.imshow(im)
coord=[]
def onclick(event):
    if event.xdata != None and event.ydata != None:
        coord.append((int(event.xdata), int(event.ydata)))
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
print(coord)


warped = four_point_transform(image, np.array(coord))

# show the original and warped images
plt.imshow(image),plt.show()
#cv2.imshow("Original", image)
plt.imshow(warped),plt.show()
#cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.imwrite('Q1a.jpg', warped) 
cv2.destroyAllWindows()
