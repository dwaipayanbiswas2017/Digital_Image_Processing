# Show that wavelet transform can be used to remove noise.
import cv2
from skimage.restoration import denoise_wavelet

def main():
	img = cv2.imread('resources/noise.jpg', 0)

	# Denoising using Byes
	denoised_img = denoise_wavelet(img, method='BayesShrink', mode='soft', wavelet_levels=5, wavelet='bior6.8', rescale_sigma=True)

	cv2.imshow('Original image', img)
	cv2.imshow('Denoise image using Byes', denoised_img)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()