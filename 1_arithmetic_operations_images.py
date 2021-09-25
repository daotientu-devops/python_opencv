# Python program to illustrate
# arithmetic operation of addtion of two images

# organizing imports
import cv2
import numpy as np

# path to input images are specified and images are loaded with imread command
image1 = cv2.imread('images/image1.jpg')
image2 = cv2.imread('images/image2.jpg')

# cv2.addWeighted is applied over the image inputs with applied parameters
#@param src1 first input array
#@param alpha weight of the first array elements
#@param src2 second input array of the same size and channel number as src1.
#@param beta weight of the second array elements
#@param gamma scalar added to each sum (vô hướng)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

# the window showing output image with the weighted sum
cv2.imshow('Weighted Image', weightedSum)

# cv2.subtract is applied over the image inputs with applied parameters
# Calculates the per-element difference between two arrays or array and a scalar
sub = cv2.subtract(image1, image2)
cv2.imshow('Subtracted Image', sub)

# De-allocate any associated memory usage
if cv2.waitKey() & 0xff == 27:
    cv2.destroyAllWindows()
