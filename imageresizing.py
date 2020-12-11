##########################################################################
# EE104 Super Project Option 4 Part 2 Resizing Images and Save to Folder
# Author: Qien Qien Lee
##########################################################################
import cv2  # pip install opencv-python
import os

# Enter path for folder containing the images
folder = "C:\\Users\\qienq\\Desktop\\9 - Fall 2020\\EE104\\Projects\\Super Project\\images\\"

# Number of images
num = 20

for x in range(1, num+1):
	# Name of image files were manually standardised in the format of Fig[Number].jpg
	os.chdir(folder)
	filename = "Fig" + str(x) + ".jpg"
	img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
	print(filename)
	print('Original Dimensions: ', img.shape)

	# resize image
	w = 32  # in unit of pixels
	h = 32
	dim = (w, h)
	resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
	print('Resized Dimensions: ', resized.shape)

	"""
	# to show images as pop-up windows
	cv2.imshow("Resized image", resized)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	"""

	# Save resized images to subdirectory
	subfolder = "resized images"
	if not os.path.exists(subfolder):
		os.mkdir(subfolder)
	os.chdir(folder+subfolder)
	status = cv2.imwrite(filename, resized)
	print("Image written to file-system : ", status, "\n")