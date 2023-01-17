# 05: How to use a logistic classification regression model to predict arrests on Chicago Crime data using  BigQueryML

The pupose of this project is to use a binary logistic regression model in BigQuery ML to make a binary prediction (yes/no) for arrests in the Chicago Crime Data set Census Dataset from 2001 to 2023.

The model will predict whether a Crime resulted in an arrest using  the arrest falls into one of two ranges **(yes or no)** based on the respondent's demographic attributes.

### Dataset
The public dataset [`Chicago Crime`](https://cloud.google.com/bigquery?sq=1057666841514:f29282e50d984f96a6fa3395aa080abf&_ga=2.187413480.-1379782407.1673021064&project=paulkamau&ws=!1m4!1m3!3m2!1s1057666841514!2schicago_crime) has about 7,713,765 rows of data from 2001 to 2023. 

## Dataset Details 

The dataset [`Chicago Crime`](https://cloud.google.com/bigquery?sq=1057666841514:f29282e50d984f96a6fa3395aa080abf&_ga=2.187413480.-1379782407.1673021064&project=paulkamau&ws=!1m4!1m3!3m2!1s1057666841514!2schicago_crime) has about 7,713,765 rows of data from 2001 to 2023. 

Total columns = 22: 
[unique_key,case_number,date,block,iucr,primary_type,description,location_description,arrest,domestic,beat,district,ward,community_area,fbi_code,x_coordinate,y_coordinate,year,updated_on,latitude,longitude,location]

Dropped columns = 7
[case_number,unique_key,x_coordinate,y_coordinate,latitude,longitude,location]

Final Columns = 15 
[date,block,iucr,primary_type,description,location_description,arrest,domestic,beat,district,ward,community_area,fbi_code,year,updated_on]

## Objective 
1. Create a logisitic regression model 
1. Evaluate the logistic regression model 
1. Predict the arrest value for a given country from the "chicago crime" table using the logistic regression model. 

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
