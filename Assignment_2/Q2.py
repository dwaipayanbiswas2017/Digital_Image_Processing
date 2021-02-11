# Subtract one image from other image
import cv2

img1 = cv2.imread('resources/image-square.jpeg', cv2.IMREAD_COLOR)
img2 = cv2.imread('resources/TestSqaureBlue.png', cv2.IMREAD_COLOR)

res = cv2.subtract(img1, img2)

cv2.imshow('Test Image 1',img1)
cv2.imshow('Test Image 2',img2)
cv2.imshow('Image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()