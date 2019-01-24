import cv2
import numpy as np

img1 = cv2.imread('board.jpg')
img2 = cv2.imread('left01.jpg')

dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)


cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
