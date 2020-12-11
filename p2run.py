####################################################################
# EE104 Super Project Option 4 Prediction Test using Model
# Author: Qien Qien Lee
####################################################################
import os
import time
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# load model (paste .h5 file into same folder as project)
model = load_model('final_model.h5')

# folder containing 32x32 images
folder = "C:\\Users\\qienq\\Desktop\\9 - Fall 2020\\EE104\\Projects\\Super Project\\images\\resized images"
os.chdir(folder)

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(32, 32))
	# convert image to array
	img_arr = img_to_array(img)
	# reshape into a single sample with 3 channels
	img_arr = img_arr.reshape(1, 32, 32, 3)
	# prepare pixel data
	img_arr = img_arr.astype('float32')
	img_arr = img_arr / 255.0
	return img_arr

# to predict the class
def run(imgfilename):
	# load image and predict the class
	result = model.predict_classes(load_image(imgfilename))
	key = int(result[0])
	if key == int(0):
		detected = "airplane"
	elif key == int(1):
		detected = "automobile"
	elif key == int(2):
		detected = "bird"
	elif key == int(3):
		detected = "cat"
	elif key == int(4):
		detected = "deer"
	elif key == int(5):
		detected = "dog"
	elif key == int(6):
		detected = "frog"
	elif key == int(7):
		detected = "horse"
	elif key == int(8):
		detected = "ship"
	elif key == int(9):
		detected = "truck"
	else:
		detected ="error"
	print(key," - ", detected)
	return detected

match = 0
num_of_images = 20
outlier_list = []
# run the loop for prediction of images in folder
for x in range(1,num_of_images+1):
	# include answer key for stats
	answer = ["airplane", "airplane", "automobile", "dog", "dog", "bird", "bird", "cat", "cat", "deer",
			  "deer", "horse", "horse", "frog", "frog", "ship", "ship", "truck", "truck", "automobile"]
	imgfilename = "Fig"+str(x)+".jpg"
	print(imgfilename, ":", answer[x-1])
	start_time = time.time()  # get start time
	detected = run(imgfilename) # run the prediction
	print("Time used: %s seconds" % (time.time() - start_time))

	if detected == answer[x-1]:
		# count for images detected correctly
		match += 1
		print("match! :)\n")
	else:
		# append to list for outliers
		outlier_list.append(imgfilename)
		print("did not match :(\n")

	# to skip plots may comment out this blocK
	# """
	img = mpimg.imread(imgfilename)  # load image for plot using matplotlib
	plt.clf()  # clear fig, just in case
	plt.imshow(img)  # plot raw pixel data
	plt.title(detected)  # add detected class title to figure
	subfolder = "Plots"
	if not os.path.exists(subfolder):
		os.mkdir(subfolder)
	plt.savefig("Plots\\"+imgfilename+"_pixel plot.png")
	# plt.show()  # show plot
	# """

# print summary
print("Detected " + str(match) + " images correctly out of a total of " + str(num_of_images))
print("Outliers were ", outlier_list)