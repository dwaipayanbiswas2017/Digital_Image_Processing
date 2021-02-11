# AND operation between two images
import cv2
import numpy as np

img1 = cv2.imread('resources/image-square.jpeg')
img2 = cv2.imread('resources/TestSqaureBlue.png')

res = cv2.bitwise_and(img2, img1, mask = None)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Bitwise And', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
