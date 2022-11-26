# 06: Single time-series forecasting from Google Analytics data

This project used the ARIMA time series model in BigQuery ML to perform a single forecast of daily total visits  using the google analytics sample ga_sessions dataset. The ga_sessions table contains information about a slice of session data collected by Google Analytics 360 and sent to BigQuery.

## Key Concepts: 
- ML.ARIMA_EVALUATE
- ML.ARIMA_COEFFICIENTS
- ML.FORECAST 
- ML.EXPLAIN_FORECAST
- ML.WEIGHTS

## Objectives
1. Create a time series model using the CREATE MODEL statement.
1. Use the ML.ARIMA_EVALUATE function to evaluate the ML Models. 
1. Use the ML.ARIMA_COEFFCIENTS function to inspect the model coefficients.
1. Use the ML.FORECAST function to forecast daily total visits. 
1. Use the ML.EXPLAIN_FORECAST function to retrieve the various components of the time series (e.g. seasonality & trends) that can be used to explain the forecast results. 
1. Use Google Data Studio to visualize the forecasting results.  


## Steps
1. Create the dataset & load the dataset into BQ
1. Use the ```SELECT``` statement to examine the data 
1. Use ```Google Data Studio``` to visualize the forecasting results.  
1. Use the ```CREATE MODEL``` statement to create the time series model. 
1. Use the ```ML.EVALUATE``` function to inspect the evaluation metrics of all evaluated models.
1. Use the ```ML.ARIMA_COEFFICIENTS``` function to retrieve the models coefficients of your ARIMA_PLUS model 
1. Use the ```ML.FORECAST``` function to to forecast the future time series values with a prediction interval using the generated model 
1. Use the ```ML.EXPLAIN_FORECAST```function to visualize the forecasting results of all the separate components to understand the forecast. 
1. Use the decompose_time_series option to concatenate the history time series and the forecasted time series using the UNION_ALL clause and the ML.FORECAST function. 

--------------------------------------------------------------------------------

_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._

[![](https://github.com/paulycloud/paulycloud/blob/main/assets/twitter.png)](https://twitter.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/linkedin.png)](https://www.linkedin.com/in/paulmkamau/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/insta.png)](https://www.instagram.com/paulykamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/behance.png)](https://www.behance.net/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dribbble.png)](https://dribbble.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/facebook.png)](https://www.facebook.com/paul.m.kamau.3/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/github.png)](https://github.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/medium.png)](https://medium.com/@paulkamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dev.png)](https://dev.to/paulycloud)