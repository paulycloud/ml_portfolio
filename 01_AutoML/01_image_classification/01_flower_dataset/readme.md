# 01 Classify images with AutoML using Vertex AI

Key Concepts: 
- AutoML 
- Image Classification
- Vertex AI

# Objective 
Use an Image flower dataset to train an AutoML model that classifies image data.

# Dataset
The image files used are from the flower dataset. These input images are stored in a public GCS bucket with a CSV file for data import. This file has two columns: the first column lists an image's URI in GCS, and the second column contains the image's label. 

On the autoML console, “create dataset” and set the import file path to the CSV file.

```bash
gs://cloud-samples-data/ai-platform/flowers/flowers.csv 
``` 

## Training an AutoML Image Classification Model 
The AutoML training method allows the user to train the model with minimal effort and ML expertise.

Node budget was set to 8 hours and training took several hours and a notification was sent after. Training completed in 30 minutes with an accuracy score of 0.98

## Deployment
After the AutoML image classification model completed training, the next step was to create an endpoint and deploy the model to the endpoint.  

Endpoints can be created from the evaluation tab on the training page. This was named “automl_image”. The Model settings accepted the traffic split of 100% and 1 node was deployed to serve the endpoint prediction. 

After the model was deployed to this new endpoint, the next step was to send an image to the model for label prediction.

## Prediction
After the endpoint creation process finished, we sent a single image annotation (prediction) request in the console. This was done by using the “Test the model” section and uploading a picture for prediction. 

The precision recall value was 94.8%, Recall 93.7%, Confidence threshold score = 0.5. 

Each prediction was assigned a confidence score, which is an assessment of the model’s certainty that the predicted label is correct (positive). The confidence threshold returns predictions as positive if their confidence score is the selected value or higher. A higher confidence threshold increases precision but lowers recall, and vice versa.


--------------------------------------------------------------------------------

_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._

[![](https://github.com/paulycloud/paulycloud/blob/main/assets/twitter.png)](https://twitter.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/linkedin.png)](https://www.linkedin.com/in/paulmkamau/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/insta.png)](https://www.instagram.com/paulykamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/behance.png)](https://www.behance.net/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dribbble.png)](https://dribbble.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/facebook.png)](https://www.facebook.com/paul.m.kamau.3/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/github.png)](https://github.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/medium.png)](https://medium.com/@paulkamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dev.png)](https://dev.to/paulycloud)