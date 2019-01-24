import cv2
import numpy as np

img = cv2.imread('board.jpg')
img1 = cv2.imread('GrayBoard.jpg')
# You can access a pixel value by its row and column coordinates.
# For BGR image, it returns an array of Blue, Green, Red values.
# For grayscale image, just corresponding intensity is returned.

px = img[100, 100]
px1 = img1[101, 101]

print px        # print BGR [34 38 26]
print px1       # print the corresponding intensity [29 29 29]

blue = img[100, 100, 0]
print blue       # print only blue [34]

# the following ones are the image's properties
print img.shape  # print board shape
print img1.shape

print img.size   # total number of pixels of image
print img1.size

print img.dtype  # observe the data type of image
print img1.dtype

# img[:, :, 0] = 0
img[:, :, 1] = 0
img[:, :, 2] = 0


core  = img[56:116 , 40:186] # the first argument is y,the second argument is x
core1 = img[304:436 , 340:500]

cv2.imshow('core',  core)
cv2.imshow('core1', core1)
cv2.waitKey(0)
cv2.destoryAllWindows()
