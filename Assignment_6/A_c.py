# Apply IFFT to reconstruct the image.
import cv2
import numpy as np

def main():
	img = cv2.imread('resources/image-square.jpeg', 0)

	dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
	dft_shift = np.fft.fftshift(dft)

	magnitude_data = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])
	magnitude_spectrum = 20 * np.log(magnitude_data)
	magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)

	# Apply IFFT
	f_ishift = np.fft.ifftshift(dft_shift)
	img_output = cv2.idft(f_ishift, flags=cv2.DFT_SCALE)
	img_output = cv2.magnitude(img_output[:, :, 0], img_output[:, :, 1])
	img_output = np.asarray(img_output, dtype=np.uint8)

	cv2.imshow('Original image', img)
	cv2.imshow('FFT', magnitude_spectrum)
	cv2.imshow('Output IFFT', img_output)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()