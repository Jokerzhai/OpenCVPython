import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 374, 3), np.uint8)

# Draw Circle
# To draw a circle, you need its center coordinates and radius.
# We will draw a circle inside the rectangle drawn above.

img = cv2.circle(img, (190, 128),  63, (0, 0, 255), -1)   # red
img = cv2.circle(img, (116, 256),  63, (0, 255, 0), -1)   # green
img = cv2.circle(img, (276, 256),  63, (255, 0, 0), -1)   # blue

img = cv2.circle(img, (190, 128),  16, (0, 0, 0), -1)
img = cv2.circle(img, (116, 256),  16, (0, 0, 0), -1)
img = cv2.circle(img, (276, 256),  16, (0, 0, 0), -1)

img = cv2.line(img, (190, 128), (116, 256), (0, 0, 0), 2)
img = cv2.line(img, (190, 128), (276, 256), (0, 0, 0), 2)
img = cv2.line(img, (116, 256), (276, 256), (0, 0, 0), 2)
# the second argument is the location of circle, the whole image is 512* 512
# the third argument is the radius of circle
# the forth argument choose RGB channel ,different combination shows different colour
# the fifth argument is to fill or not , -1 is yes ,0 is no

# Display the pic
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destoryAllWindows()