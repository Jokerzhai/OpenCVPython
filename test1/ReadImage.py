import cv2
import numpy as np

img0 = cv2.imread('board.jpg', 0) #Loads image in grayscale mode
img1 = cv2.imread('board.jpg', 1)#Loads a color image. Any transparency of image will be neglected. It is the default flag.
img2 = cv2.imread('board.jpg', -1)#Loads image as such including alpha channel


# cv2.imshow('board0.jpg',img0) #display the picture ,the second argument is to show different pictures,the first argument is window's name
# cv2.imshow('board1.jpg',img1)
# cv2.imshow('board2.jpg',img2)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

cv2.namedWindow('board0.jpg',cv2.WINDOW_NORMAL)
cv2.namedWindow('board1.jpg',cv2.WINDOW_NORMAL)
cv2.namedWindow('board2.jpg',cv2.WINDOW_NORMAL)
cv2.imshow('board0.jpg',img0)
cv2.imshow('board1.jpg',img1)
cv2.imshow('board2.jpg',img2)
cv2.waitKey(0)
cv2.destoryAllWindows()

# Save result
cv2.imwrite('out0.jpg', img0)
cv2.imwrite('out1.jpg', img1)
cv2.imwrite('out2.jpg', img2)