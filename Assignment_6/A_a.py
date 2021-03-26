# Apply FFT on a given image of your choice.
import numpy as np
import cv2

def main():
	img = cv2.imread('resources/image-square.jpeg', 0)

	# DFT
	dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
	dft = np.fft.fftshift(dft)

	# Magnitude spectrum
	magnitude_data = cv2.magnitude(dft[:, :, 0], dft[:, :, 1])
	magnitude_spectrum = 20 * np.log(magnitude_data)
	magnitude_spectrum = np.uint8(magnitude_spectrum)

	cv2.imshow('Original image', img)
	cv2.imshow('FFT result', magnitude_spectrum)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()