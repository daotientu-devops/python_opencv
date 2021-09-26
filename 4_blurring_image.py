# Importing libraries
import cv2
import numpy as np
image = cv2.imread("images/image1.jpg")
cv2.imshow('Original Image', image)
cv2.waitKey(0)
"""
Importing types of bluring:
Gaussian Blurring:Gaussian blur is the result of blurring an image by a Gaussian function. It is a widely used effect in graphics software, typically to reduce image noise and reduce detail. It is also used as a preprocessing stage before applying our machine learning or deep learning models.
E.g. of a Gaussian kernel(3×3)
  1/16 \quad \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2\\ 1 & 2 & 1 \\  \end{bmatrix}  
Median Blur (Làm mờ trung bình): The Median Filter is a non-linear digital filtering technique, often used to remove noise from an image or signal. Median filtering is very widely used in digital image processing because, under certain conditions, it preserves edges while removing noise. It is one of the best algorithms to remove Salt and pepper noise.
Bilateral Blur (Làm mờ song phương): A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels. This weight can be based on a Gaussian distribution. Thus, sharp edges are preserved while discarding the weak ones.
"""
# Gaussian blur
gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', gaussian)
cv2.waitKey(0)
# Median blur
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)
# Bilateral blur
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
