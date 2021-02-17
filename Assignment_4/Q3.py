# Rotation of an image
import cv2
import numpy as np

img = cv2.imread('resources/image-square.jpeg')
num_rows, num_cols = img.shape[:2]

angel = 210

rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), angel, 1)
img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
cv2.imshow('Rotate : '+str(angel), img_rotation)
cv2.waitKey()