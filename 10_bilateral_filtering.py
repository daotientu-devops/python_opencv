import cv2
import numpy as np
# Input: noisy image
img = cv2.imread('images/taj.jpg')
"""
Lọc song phương (bilateral filter)
Apply bilateral filter with d = 15
sigmaColor = sigmaSpace = 75
==> output: Xử lý nhiễu
"""
bilateral = cv2.bilateralFilter(img, 15, 75, 75)
cv2.imwrite('images/taj_bilateral.jpg', bilateral)
cv2.imshow('Bilateral Filtering', bilateral)
cv2.waitKey(0)