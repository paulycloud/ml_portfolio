# 02: How to use a logistic classification regression model to to predict the outstanding debt value for a country given certain factors based on the World Bank International Debt Dataset. 

This project used a binary logistic regression model in BigQuery ML to predict the outstanding debt value for a country given certain factors based on the World Bank International Debt Dataset. 

## Dataset Details 

The dataset [`International Debt`](https://cloud.google.com/marketplace/product/the-world-bank/international-debt) contains both national and regional debt statistics captured by over 200 economic indicators. Time series data is available for those indicators from 1970 to 2015 for reporting countries. 

Multiple tables have been used to compile the data. The data was flattened to create a single working set: 
- Country series definitions 
- Country summary 
- International debt
- Series summary (496 series codes)
- Series times

## Objective 
1. Create a logisitic regression model 
1. Evaluate the logistic regression model 
1. Predict the debt value for a given country from the "international_debt" table using the logistic regression model. 

## Key Concepts
1. Logistic regression 
1. Explainable AI
1. ML.EVALUATE
1. ML PREDICT

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
