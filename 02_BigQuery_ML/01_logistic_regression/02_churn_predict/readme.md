
### 08: How to use a logistic classification model to predict Churn on pre-processed Google Analytics 4 data using  BigQueryML

[original source](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/bigquery_ml/bqml-online-prediction.ipynb)

### Objective

In this tutorial, you learn how to train and deploy a churn prediction model for real-time inference, with the data in BigQuery and model trained using BigQuery ML, registered to Vertex AI Model Registry, and deployed to an endpoint on Vertex AI for online predictions.

This tutorial uses the following Google Cloud data analytics and ML services:

- BigQuery
- BigQuery ML
- Vertex AI Model Registry
- Vertex endpoints

### Dataset

The dataset, <a href="https://console.cloud.google.com/bigquery?project=bigquery-public-data&d=ga4_obfuscated_sample_ecommerce&p=bigquery-public-data&page=dataset" target="_blank">available publicly on BigQuery</a>, comes from obfuscated <a href="https://support.google.com/analytics/answer/10937659" target="_blank">Google Analytics 4 data</a> from the <a href="https://shop.googlemerchandisestore.com/" target="_blank">Google Merchandise Store</a>).

The steps performed include:
- Using Python & SQL to query the public data in BigQuery
- Preparing the data for modeling
- Training a classification model using BigQuery ML and registering it to Vertex AI Model Registry
- Inspecting the model on Vertex AI Model Registry
- Deploying the model to an endpoint on Vertex AI
- Making sample online predictions to the model endpoint

