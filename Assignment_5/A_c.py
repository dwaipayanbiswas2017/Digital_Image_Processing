# Median filter
import cv2
import numpy as np

def main():
	img = cv2.imread('resources/noise.jpeg')
	median = cv2.medianBlur(img, 3)

	cv2.imshow('Noisy Image', img)
	cv2.imshow("Denoised Image", median)
	cv2.waitKey(0)
	cv2.destroyAllWindows

if __name__ == "__main__":
	main()