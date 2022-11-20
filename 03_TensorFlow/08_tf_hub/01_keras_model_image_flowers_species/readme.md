# Use TFHub Pretrained Keras Model with image feature extraction to classify 5 Flower Species 

This project shows how to use images of flowers using a `tf.keras.Sequential` model and load data using `tf.keras.utils.image_dataset_from_directory`.

# Objective 
This project demonstrates how to build a ** Keras model** for classifying five species of flowers by using a pre-trained TF2 SavedModel from TensorFlow Hub for image feature extraction, trained on the much larger and more general ImageNet dataset. 


## Dataset 
Inputs are suitably resized for the selected module. Dataset augmentation (i.e., random distortions of an image each time it is read) improves training, esp. when fine-tuning.


The [Flowers Species Dataset](https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz) dataset contains 3670 color images in 5 classes. The dataset is divided into 2936 training images and 734 testing images. The classes are mutually exclusive and there is no overlap between them.

## Key Concepts: 
1. Transfer Learning
1. Linear classifier 

## Steps
1. Import TensorFlow 
1. Examine and understand data 
1. Set up the Flowers Dataset 
1. Build the model 
1. Train the model 
1. Test the model 
1. Deploy a saved model to a TensorFlow Lite model 


In addition, the notebook demonstrates how to convert a [saved model](../../../guide/saved_model.ipynb) to a [TensorFlow Lite](https://www.tensorflow.org/lite/) model for on-device machine learning on mobile, embedded, and IoT devices.

[Original Source](https://github.com/tensorflow/hub/blob/master/examples/colab/tf2_image_retraining.ipynb)