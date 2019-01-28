# Q.4: Binarization of Otsu
# Detail: Implement Otsu's binarization
# Otsu's binarization is called a discriminant analysis method,
# and it is a method to automatically determine the separation threshold in binarization.
# This is calculated from the ratio **between** **intra-class variance** and **interclass variance** .
# Less than the threshold t is class 0, and equal or more than t is class 1.
# $w_0$, $w_1$: The ratio of the number of pixels of each class separated by the threshold t ($w_0 + w_1 = 1$ is satisfied)
# $S0^2, S1^2$ ... Distribution of pixel values of each class
# $M0, M1$ ... average value of pixel values of each class
#```python
# Sw^2 = w0 * S0^2 + w1 * S1^2 # Within-class variance
# Sb^2 = w0 * (M0 - Mt)^2 + w1 * (M1 - Mt)^2 = w0 * w1 * (M0 - M1) ^2 # Interclass variance
# St^2 = Sw^2 + Sb^2 = (const)  # Distribution of pixels of the whole image
# The degree of separation is defined by the following equation.
# X = Sb^2 / Sw^2 = Sb^2 / (St^2 - Sb^2) # Separation degree
# Therefore:

# ```python
# argmax_{t} X = argmax_{t} Sb^2
# ```
#  That is, the threshold value t that satisfies $Sb^2 =  w0 * w1 * (M0 - M1) ^2 $ may be used as the binarization threshold.

# |Input (imori.jpg)|Output (th = 127) (answer_4.jpg)|
# |:---:|:---:|
# |![](imori.jpg)|![](answer_4.jpg)|

# Answer >> [4_Binarization_of_Otsu.py](./4_Binarization_of_Otsu.py)

import cv2
import numpy as np

# Read image
img = cv2.imread("lena.png").astype(np.float)
# image type transform from uin8 to float

H, W, C = img.shape
print H, W, C

# Grayscale
out = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
out = out.astype(np.uint8)
# image type transform from float to uint8


# Determine threshold of Otsu's binarization
max_sigma = 0
max_t = 0

# _t means threshold
for _t in range(1, 512):
    v0 = out[np.where(out < _t)]
    m0 = np.mean(v0) if len(v0) > 0 else 0.
    w0 = len(v0) / (H * W)  #
    v1 = out[np.where(out >= _t)]
    m1 = np.mean(v1) if len(v1) > 0 else 0.
    w1 = len(v1) / (H * W)
    sigma = w0 * w1 * ((m0 - m1) ** 2)
# Sb^2 = w0 * (M0 - Mt)^2 + w1 * (M1 - Mt)^2 = w0 * w1 * (M0 - M1) ^2 # Interclass variance
    if sigma > max_sigma:
       max_sigma = sigma
       max_t = _t

print out
print ("the length of v0 ", len(v0))
print ("the length of v1 ", len(v1))
print ("v0 is ", v0)
print ("v1 is ", v1)
print ("w0 is ", w0)
print ("w1 is ", w1)
print ("m0 is ", m0)
print ("m1 is ", m1)
print ("sigma is ", sigma)
print ("threshold is ", _t)
print ("max_sigma is ", max_sigma)
print ("max_t is ", max_t)

# Binarization
print("threshold >>", max_t)
th = max_t
out[out < th] = 0
out[out >= th] = 255

# Save result

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
