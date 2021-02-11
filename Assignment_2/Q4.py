# Different Brightness by changing mean value
import cv2

def increase_brightness(img, value=30):
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h, s, v = cv2.split(hsv)

	lim = 255 - value
	v[v > lim] = 255
	v[v <= lim] += value

	final_hsv = cv2.merge((h, s, v))
	img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
	return img

img = cv2.imread('resources/image-square.jpeg', cv2.IMREAD_COLOR)

res = increase_brightness(img, value=80)

cv2.imshow('Image',img)
cv2.imshow('Result',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
