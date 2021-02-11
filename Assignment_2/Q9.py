# NOT operation (Negative image)
import cv2
import numpy as np

img1 = cv2.imread('resources/image-square.jpeg')

res = cv2.bitwise_not(img1, mask = None)

cv2.imshow('Image 1', img1)
cv2.imshow('Bitwise NOT', res)

cv2.waitKey(0)
cv2.destroyAllWindows()