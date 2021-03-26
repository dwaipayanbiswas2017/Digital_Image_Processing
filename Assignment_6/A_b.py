# Perform low pass and high pass filtering in frequency domain
import cv2
import numpy as np

def main():
	img = cv2.imread('resources/image-square.jpeg')

	dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
	dft_shift = np.fft.fftshift(dft)

	# Creating High pass filter
	row, col = img.shape
	r = 20
	center_row, center_col = int(row / 2), int(col / 2)
	mask = np.ones((row, col, 2), np.uint8)
	center = [center_row, center_col]
	x, y = np.ogrid[:row, :col]
	mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
	mask[mask_area] = 0
	high_pass_fshift = dft_shift * mask

	# Creating Low pass filter
	row, col = img.shape
	r = 80
	center_row, center_col = int(row / 2), int(col / 2)
	mask = np.zeros((row, col, 2), np.uint8)
	center = [center_row, center_col]
	x, y = np.ogrid[:row, :col]
	mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
	mask[mask_area] = 1
	low_pass_fshift = dft_shift * mask

	# Perform inverse fourier and inverse shift
	# Apply High pass filter
	filter_ishift = np.fft.ifftshift(high_pass_fshift)
	high_pass_img_res = cv2.idft(filter_ishift, flags=cv2.DFT_SCALE)
	high_pass_img_res = cv2.magnitude(high_pass_img_res[:, :, 0], high_pass_img_res[:, :, 1])
	high_pass_img_res = np.asarray(high_pass_img_res, dtype=np.uint8)

	# Apply Low pass filter
	filter_ishift = np.fft.ifftshift(low_pass_fshift)
	low_pass_img_res = cv2.idft(filter_ishift, flags=cv2.DFT_SCALE)
	low_pass_img_res = cv2.magnitude(low_pass_img_res[:, :, 0], low_pass_img_res[:, :, 1])
	low_pass_img_res = np.asarray(low_pass_img_res, dtype=np.uint8)

	cv2.imshow('Original', img)
	cv2.imshow('High pass filter output', high_pass_img_res)
	cv2.imshow('Low pass filter output', low_pass_img_res)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()