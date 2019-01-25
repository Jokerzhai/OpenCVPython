import cv2
import numpy as np

# load two images
img1 = cv2.imread('board.jpg')
# img2 = cv2.imread('left01.jpg')
img2 = cv2.imread('opencvlogo.png')

# I want to put logo on top-left corner, So I create a ROI

# read the the size of img2 including rows and cols

rows, cols, channels = img2.shape

# draw the size of img1 in the img2
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse msk also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_and(ret, mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
# waitKey is different from waitkey
cv2.destroyAllWindows()

