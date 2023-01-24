# How to use a linear_regression model to predict the average Total alcohol consumption per capita (SH_ALC_PCAP_LI) using BigQuery ML

This project used a linear regression model in BigQuery ML to to predict the average Total alcohol consumption per capita (SH.ALC.PCAP.LI) based on the WorldBank Health International Data.

## Dataset Details 

The dataset [`world_bank_health_population`](https://cloud.google.com/bigquery?sq=1057666841514:3bb229234d7f4b379098581f0101e923&_ga=2.81369303.-1379782407.1673021064&project=paulkamau&ws=!1m9!1m3!3m2!1sbigquery-public-data!2sworld_bank_health_population!1m4!4m3!1sbigquery-public-data!2sworld_bank_health_population!3scountry_series_definitions) combines key health statistics from a variety of sources to provide a look at global health and population trends. It includes information on nutrition, reproductive health, education, immunization, and diseases from over 200 countries.

Multiple tables have been used to compile the data. The data was flattened to create a single working set: 

- Country series definitions 
- Country summary 
- Health nutrition population
- International debt
- Series summary 
- Series times

## Objectives 
1. Create a linear regression model 
1. Evaluate the linear regression model 
1. Predict the average age average age of first marriage for females given certain factors based on the World Health Population Dataset

## Data Manipulation with SQL
- See the data_operations notebook

## steps
1. Create the dataset 
1. Use the SELECT statement to examine the data 
1. Use the CREATE VIEW statement to compile your training data
1. Use the CREATE MODEL statement to create your logistic regression model. 
1. Use the ML.EVALUATE function to evaluate the model data
1. Use the ML.PREDICT function to predict the income bracket for a given set of census participants.
1. Use the ML.EXPLAIN_PREDICT function to explain prediction results with explainable AI Methods. 
1. Use the ML.GLOBAL_EXPLAIN function to know which features are the most important to determine the income bracket. 


--------------------------------------------------------------------------------
_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._
Find all my social links here

#### All My Links
[BioLink](https://bio.link/paulkamau)


#### Buy Me Coffee
[Cashapp](https://bio.link/paulkamau)
[PayPal](https://paypal.me/paulkamau)
