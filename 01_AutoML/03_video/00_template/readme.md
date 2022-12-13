# Classify video features specifies using data from Google's Flower dataset with AutoML Image

##### Copyright 
**Author - GUI Tutorial :** [Google  Kamau](https://cloud.google.com)<br>
**Author Notebook Version:** [Paul Kamau](https://paulkamau.com)<br>
**Project Type:** AutoML<br>
**Last modified:** 11/26/2022<br>
**Description:** Using TFHub Model Audio Event classifier called Yamnett Model, to classify UK & Ireland accents using feature extraction from [Yamnet Model](https://tfhub.dev/google/yamnet/1). 

**Dataset** Feature extraction and training will use the [Crowdsourced HQ UK &Ireland English Dialect Speeh Speech Data set](https://openslr.org/83/) which consists of a total of 17,877 audio wav files. 


Original Source: 

Key Concepts: 
- AutoML 
- text Classification
- Vertex AI

# Objective 
This project demonstrates how to create a model for classifying content using Vertex AI. The project trains an AutoML model by using a set of videos on GCS.

# Dataset


```bash
gsutil -m cp -R gs://automl-video-demo-data/hmdb_split1_5classes_all.csv gs://auto-ml-tutorials/video/
``` 

This file has two columns: the first column lists the video source GCS, and the second column contains the video label. 

On the autoML console, “create dataset” named “auto_ml_video_classification” set the “Data type” and “objective” with the “video” tab and select the radio button “video classification” and set the import file path to the CSV file

```bash
 gs://auto-ml-tutorials/video/hmdb_split1_5classes_all.csv 
``` 

## Training an AutoML Video Classification Model 
After the AutoML video classification model completed training, the next step was to create an endpoint and deploy the model to the endpoint.  The model average Precision & Recall were 100%. The Confusion matrix true label vs predicted label was 100%. 

Endpoints can be created from the evaluation tab on the training page. This was named “automl_video”. 

## Batch Prediction 
Model predictions will be done in batch format.  The batch name, “demo_data_predictions” , source path & destination was set. The prediction results are stored on the GCS bucket. 

## Viewing the results. 

In the results for the video annotation, Vertex AI provides three types of information:

- Video labels are under the Segment tab, Shot Labels within the video are under the Shot tab.
- The 1 Second Interval contains the second by second labeling.
- Changing the threshold allowed me to see more labels. AutoML video only displays the labels that are above the specified threshold. Failed predictions are on the Recent Predictions list.

--------------------------------------------------------------------------------
