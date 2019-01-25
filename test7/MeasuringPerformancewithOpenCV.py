import cv2
import numpy as np

img1 = cv2.imread('board.jpg')
e1 = cv2.getTickCount()
# your code execution
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time
# the result is 0.747622083783 seconds
