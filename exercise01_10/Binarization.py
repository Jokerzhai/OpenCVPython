# Q.3: Binarization
# Binarize the image.
# Binarization is a method of expressing images as binary black and white.
# Here, the threshold is set to 128 in gray scale and binarized by the following equation.
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float)

img_1 = cv2.imread("imori.jpg")
img1 = img_1.copy()
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Grayscale
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Binarization
th = 128
out[out < th] = 0
out[out >= th] = 255

gray[gray < th] = 0
gray[gray >= th] = 255


# use for to display 2 images
titles = ['binarization 1',
          'binarization 2']
images = [out, gray]

for i in xrange(2):
    plt.subplot(2, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

