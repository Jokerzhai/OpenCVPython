# Q.2: Grayscale
# Detail: Make the image grayscale.
# Grayscale is a kind of image luminance expression method and is calculated by the following formula.
# Y = 0.2126 R + 0.7152 G + 0.0722 B
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread("imori.jpg")
img_origion = img.copy()
print img_origion.dtype
# transform the uint8 to float
img = img.astype(np.float)
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

out = 0.2126 * r + 0.7152 * g + 0.0722 * b
# transform float to uint8
out = out.astype(np.uint8)

# Grayscale
# You could use the cv2.cvtColor() to change the rgb image into grayscale.
gray = cv2.cvtColor(img_origion, cv2.COLOR_BGR2GRAY)

# use for to display 3 images
titles = ['Original Image', 'grayscalemethod 1', 'grayscalemethod 2']
images = [img_origion, out, gray, ]

for i in xrange(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
