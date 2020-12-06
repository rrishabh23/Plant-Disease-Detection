# Plant-Disease-Detection



### Plant Disease Detection System
=====================================

Contents:
- Introduction
- Libraries Used
- Working

### Introduction
=====================================

The project aims at identifying Plant disease through the help of captured images,
by identifying the leaf's pigmentation and color. Traditionally, plant disease is
identfied manually by farmers, which takes enough time that it can potentially cause
a lot damage to the produce. Identifing every plant on the farm is not a task than can be 
performed by a farmer. By employing image processing techniques, these mishaps
can be effectively minimized or maybe even removed altogether. This can also help 
reducing the amount of chemicals used to keep the plants healthy and free from disease,
minimizing costs and increasing profits.


### Libraries Used
======================================
1. Pandas
2. XGBoost
3. Scikit-learn
4. OpenCV
5. Matplotlib
6. Numpy


### Working
=======================================

The Test Image.py script, applies the segmentation operation on a test image, and seperates the diseased
part of the leaf and the healthy part of the leaf. <br /> 
<p align="center">
  <img src="https://github.com/rrishabh23/Plant-Disease-Detection/blob/master/Docs/seg.jpg" />
</p>
<br /> 

First, the image is converted to the HSV model, and 
a hue seperating masked is used to segment the diseased part of the leaf from the healthy part (green in
color). A histogram is then plotted which consists of 16 bins, representing the various differentiable
colors in the image of the leaf. <br /> 
<p align="center">
  <img src="https://github.com/rrishabh23/Plant-Disease-Detection/blob/master/Docs/Apple%20Healthy.png" /><br /> 
Histogram of a Healthy Leaf
</p> 

<br /> 
<p align="center">
  <img src="https://github.com/rrishabh23/Plant-Disease-Detection/blob/master/Docs/Apple%20Infected.png" /><br /> 
Histogram of an Infected Leaf
</p> 

<br /> 
Percentage of the colors yellow (representing the diseased part), green
(representing the healthy part), cyan, blue and magenta are calculated and displayed using the histogram.
Then the percentage is used as the feature for classification between Diseased and Healthy leaves. The features
are saved to a csv file. The dataset is imported and XGBoost model is trained in classifier.py. The results are 
displayed in the console. 
The script Color_feature_extractor.py is used to generate features for every image present in a directory making 
the task of creating the data to train classifier easier.



This project uses the cropped and masked images of leaves to detect plant diseases. The dataset can be found [here.](https://github.com/johri002/Automatic-leaf-infection-identifier/tree/master/Image%20Dataset)

This project uses image segmmentation by color and makes a color histogram of 16 bins to get information about the color of the leaf, after that color features are extracted and used for training a classifier. The accuracy achieved with detection of diseases in Apple leaves, from the dataset, is 88% using around 2000 images.

The dataset can be trained for more images with the help of ```Color_feature_extractor.py```



.
===========================================



Refrences: 
[Feasibility Study on Plant Chili Disease Detection Using Image Processing Techniques](https://ieeexplore.ieee.org/document/6169716)
