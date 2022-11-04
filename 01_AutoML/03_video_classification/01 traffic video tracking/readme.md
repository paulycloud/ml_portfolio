# 03 Classify Video with AutoML using Vertex AI

Key Concepts: 
- AutoML 
- text Classification
- Vertex AI

# Objective 
This project demonstrates how to create a model for classifying content using Vertex AI. The project trains an AutoML model by using a set of videos on GCS.


# Dataset
The text files used are from the HappyDB dataset with 24,528 rows. Copy the data from the ml GCS bucket into your own bucket. 

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

_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._

[![](https://github.com/paulycloud/paulycloud/blob/main/assets/twitter.png)](https://twitter.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/linkedin.png)](https://www.linkedin.com/in/paulmkamau/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/insta.png)](https://www.instagram.com/paulykamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/behance.png)](https://www.behance.net/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dribbble.png)](https://dribbble.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/facebook.png)](https://www.facebook.com/paul.m.kamau.3/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/github.png)](https://github.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/medium.png)](https://medium.com/@paulkamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dev.png)](https://dev.to/paulycloud)