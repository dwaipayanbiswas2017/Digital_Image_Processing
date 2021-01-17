# Separate color image in three R G & B planes
import cv2 as cv

img=cv.imread("TestRGB.jpeg",cv.IMREAD_COLOR)
cv.imshow("Original",img)
greyscale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GreyScale",greyscale)
threshold,black_white=cv.threshold(greyscale,127,255,cv.THRESH_BINARY)
cv.imshow("Black & White",black_white)
cv.waitKey(0)
cv.destroyAllWindows()