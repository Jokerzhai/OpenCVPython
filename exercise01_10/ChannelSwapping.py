# Q.1: Channel Swapping
# Detail: Read the image and change RGB in order of BGR.
# 2 method to swap the channel in the same image
import cv2
from matplotlib import pyplot as plt

# Read image
img = cv2.imread("imori.jpg")
img_1 = img.copy()
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# RGB > BGR
img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

# You could use cv2.cvtColor() function to directly swap the color channels.
img_rgb = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)

# use for to display 3 images
titles = ['Original Image', 'the first method', 'the second method']
images = [img_1, img, img_rgb, ]

for i in xrange(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

