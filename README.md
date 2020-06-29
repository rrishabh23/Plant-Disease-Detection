# Plant-Disease-Detection

This project uses the cropped and masked images of leaves to detect plant diseases. The dataset can be found [here.](https://github.com/johri002/Automatic-leaf-infection-identifier/tree/master/Image%20Dataset)

This project uses image segmmentation by color and makes a color histogram of 16 bins to get information about the color of the leaf, after that color features are extracted and used for training a classifier. The accuracy achieved with detection of diseases in Apple leaves, from the dataset, is 88% using around 2000 images.

The dataset can be trained for more images with the help of ```Color_feature_extractor.py```


Refrences: 
[Feasibility Study on Plant Chili Disease Detection Using Image Processing Techniques](https://ieeexplore.ieee.org/document/6169716)
