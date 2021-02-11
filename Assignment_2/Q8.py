# Water Marking using EX-OR operation
import cv2

img = cv2.imread('resources/image-square.jpeg')
logo_img = cv2.imread('resources/TestSqaureBlue.png')

res = cv2.addWeighted(img, 0.6, logo_img, 0.4, 0)

cv2.imshow('Image 1', img)
cv2.imshow('Image 2', logo_img)
cv2.imshow("Water marked result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()