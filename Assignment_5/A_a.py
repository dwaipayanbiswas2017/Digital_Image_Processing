# Remove Salt and Pepper Noise
import cv2
import numpy as np

def main():
	img = cv2.imread("resources/noise.jpeg", 1)

	denoised = cv2.medianBlur(img, 3)

	cv2.imshow("Salt & Pepper noised Image",img)
	cv2.imshow("Denoised Image",denoised)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()