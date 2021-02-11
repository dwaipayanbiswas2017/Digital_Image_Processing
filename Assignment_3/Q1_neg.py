# Implement basic gray level transformation for the Negetive
import cv2
import numpy as np

img = cv2.imread('resources/gray.jpg')

L = img.max()
img_neg = L - img

cv2.imshow("Original Image", img)
cv2.imshow("Negative Image", img_neg)

cv2.waitKey(0)
cv2.destroyAllWindows()
