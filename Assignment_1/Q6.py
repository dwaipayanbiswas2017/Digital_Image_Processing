# Create color image using R, G and B three separate
# planesCreate color image using R, G and B three separate planes
import cv2 as cv

img = cv.imread("resources/TestRGB.jpeg")
b,g,r = cv.split(img)

merge1 = cv.merge((b,g,r))
merge2 = cv.merge((b,r,g))
merge3 = cv.merge((g,b,r))
merge4 = cv.merge((g,r,b))
merge5 = cv.merge((r,b,g))
merge6 = cv.merge((r,g,b))

cv.imshow("1",merge1)
cv.imshow("2",merge2)
cv.imshow("3",merge3)
cv.imshow("4",merge4)
cv.imshow("5",merge5)
cv.imshow("6",merge6)

cv.waitKey(0)
cv.destroyAllWindows()