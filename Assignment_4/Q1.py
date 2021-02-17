# Translation of an image
import cv2
import numpy as np

image = cv2.imread('resources/image-square.jpeg')

height, width = image.shape[:2]
quarter_height, quarter_width = height / 8, width / 8

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
translated_img = cv2.warpAffine(image, T, (width, height))

cv2.imshow("Original image", image)
cv2.imshow('Translation', translated_img)
cv2.waitKey()

cv2.destroyAllWindows()
