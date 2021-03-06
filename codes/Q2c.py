import cv2
import numpy as np
import math
def img_interp(img, scale = 1.5):

    #angle_rad = 22.0/7.0* angle_deg / 180.0;

    rows, cols, colours = img.shape

    n_rows = int(round(rows * scale, 0))
    n_cols = int(round(cols * scale, 0))

    enlarged_img = np.ones((n_rows, n_cols, colours))

    for i in range(n_rows - 1):
        for j in range(n_cols - 1):
            x_coord = j / scale
            y_coord = i / scale

            xc = int(math.ceil(x_coord))
            xf = int(math.floor(x_coord))
            yc = int(math.ceil(y_coord))
            yf = int(math.floor(y_coord))

            W_xc = xc - x_coord
            W_xf = x_coord - xf
            W_yc = yc - y_coord
            W_yf = y_coord - yf

            enlarged_img[i, j, :] = 255 - np.around(W_xc * (W_yc * img[yf, xf, :] + W_yf * img[yc, xf, :]) + W_xf * (W_yc * img[yf, xc, :] + W_yf * img[yc, xc, :]), 0)

    return enlarged_img

img=cv2.imread('Ajanta_1.jpg',-1)
img=img_interp(img,2)
cv2.imshow('kgj',img)
cv2.waitKey(0)



