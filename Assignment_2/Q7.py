# Calculate intersection of two images
import cv2

img1 = cv2.imread('resources/image-square.jpeg')
img2 = cv2.imread('resources/TestSqaureBlue.png')

img_bwa = cv2.bitwise_and(img1,img2)
img_bwo = cv2.bitwise_or(img1,img2)
img_bwx = cv2.bitwise_xor(img1,img2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow("Bitwise AND", img_bwa)
cv2.imshow("Bitwise OR", img_bwo)
cv2.imshow("Bitwise XOR", img_bwx)

cv2.waitKey(0)
cv2.destroyAllWindows()