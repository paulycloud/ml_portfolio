
# 07: Multiple time-series forecasting with a single query for NYC Citi Bike trips

This project used the ARIMA Time Series Model in BigQuery ML to perform multiple time-series forecasts with a single query. Different fast training strategies were applied to significantly speed up the query and evaluate forecasting accuracy. 

## Dataset 
The Dataset used was the new_york.citibike_trips data. This data contains information about Citi Bike trips in New York City.

## Objective 
1. Create a time series model using the CREATE MODEL statement.
1. Use the ML.ARIMA_EVALUATE function to evaluate the ML Models. 
1. Use the ML.ARIMA_COEFFCIENTS function to inspect the model coefficients.
1. Use the ML.FORECAST function to forecast daily total bike trips. 
1. Use the ML.EXPLAIN_FORECAST function to retrieve the various components of the timeseries (e.g. seasonality & trends) that can be used to explain the forecast results. 
1. Use Google Data Studio to visualize the forecasting results.  

## Key Concepts
1. ARIMA Time Series Model
1. ML.ARIMA_EVALUATE
1. ML.ARIMA_COEFFICIENTS
1. ML.FORECAST 
1. ML.EXPLAIN_FORECAST
1. ML.WEIGHTS

## steps
1. Create the dataset & load the dataset into BQ
1. Use the SELECT statement to examine the data 
1. Use Google Data Studio to visualize the forecasting results.  
1. Use the CREATE MODEL statement to create the time series model. 
1. Use the ML.EVALUATE function to inspect the evaluation metrics of all evaluated models.
1. Use the ML.ARIMA_COEFFICIENTS function to retrieve the models coefficients of your ARIMA_PLUS model 
1. Use the ML.FORECAST function to to forecast the future time series values with a prediction interval using the generated model 
1. Use the ML.EXPLAIN_FORECAST function to visualize the forecasting results of all the separate components to understand the forecast. 
1. Use the decompose_time_series option to concatenate the history time series and the forecasted time series using the UNION_ALL clause and the ML.FORECAST function. 

--------------------------------------------------------------------------------

_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._

[![](https://github.com/paulycloud/paulycloud/blob/main/assets/twitter.png)](https://twitter.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/linkedin.png)](https://www.linkedin.com/in/paulmkamau/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/insta.png)](https://www.instagram.com/paulykamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/behance.png)](https://www.behance.net/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dribbble.png)](https://dribbble.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/facebook.png)](https://www.facebook.com/paul.m.kamau.3/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/github.png)](https://github.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/medium.png)](https://medium.com/@paulkamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dev.png)](https://dev.to/paulycloud)