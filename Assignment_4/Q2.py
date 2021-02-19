# Scaling of an image
import cv2
import numpy as np

image = cv2.imread('resources/image-square.jpeg')

print(image.shape)

scalled_img = cv2.resize(image, (600, 600))

cv2.imshow("Original image", image)
cv2.imshow('Scalled image', scalled_img)
cv2.waitKey()

cv2.destroyAllWindows()
