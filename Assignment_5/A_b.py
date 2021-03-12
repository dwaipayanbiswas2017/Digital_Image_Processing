# Minimize Gaussian noise
import cv2
import numpy as np

def main():
	img = cv2.imread('resources/noise.jpeg')

	denoised = cv2.GaussianBlur(img, (5, 5), 0, borderType=cv2.BORDER_CONSTANT)

	cv2.imshow("Original Image",img)
	cv2.imshow("Denoised Image(Gaussian)",denoised)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()