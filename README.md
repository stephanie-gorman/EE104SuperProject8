# EE104SuperProject8
Contains files for Super Project Group 8 for EE 104 at SJSU  
Using CNN (Convolutional Neural Network) for Photo Classification  
Reference: https://machinelearningmastery.com/how-to-develop-a-cnn-from-scratch-for-cifar-10-photo-classification/  
  
Part 1 is located under main branch  
Part 2 and 3 is under a branch "part2and3"  
  
# Part 1
Develop a convolutional neural network model from scratch for object photo classification  
- test harness for developing evaluation of a model and establish a baseline of performance for a classification task  
- explore extensions to a baseline model to improve learning and model capacity  
- develop a finalized model, evaluate the performance of the final model, and use it to make predictions on new images  
  
please install the following:  
pip install keras  
pip install tensorflow  
conda install h5py  
pip install matplotlib   
  
# Part 2 and 3
Using our final model, 'final_model.h5' from the previous part, prediction test is run on 20 images  
imageresizing.py : resizes the images in a folder to 32x32 and saves resized images to a subfolder  
p2run.py : runs the model to predict the class of images and saves resulting plots in a subfolder  
  
please install the following:  
pip install opencv-python  
pip install tensorflow  
pip install matplotlib  
