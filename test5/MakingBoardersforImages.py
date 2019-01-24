import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

img = cv2.imread('opencvlogo.png')

# Now start explaining every argument
# the first argument is the image source
# the second argument is top , bottom, left, right
# border width in number of pixels in corresponding directions
# the third argument is borderType
# Flag defining what kind of border to be added.
# total 5 type as followed
# cv2.BORDER_REPLICATE  Adds a constant colored border.
# The value should be given as next argument.
# cv2.BORDER_REFLECT
# Border will be mirror reflection of the border elements,
# like this : fedcba|abcdefgh|hgfedcb
# cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT
# Same as above, but with a slight change,
# like this : gfedcb|abcdefgh|gfedcba
# cv2.BORDER_REPLICATE
# Last element is replicated throughout,
# like this: aaaaaa|abcdefgh|hhhhhhh
# cv2.BORDER_WRAP
# Cannot explain , it will look like this: cdefgh|abcdefgh|abcdefg


replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()