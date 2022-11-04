#### Video Intelligence API
The Video Intelligence API allows developers to use Google video analysis technology as part of their applications. 
 
The REST API enables users to annotate videos stored locally or in Cloud Storage with contextual information at the level of the entire video, per segment, per shot, and per frame. Among its many features, the Video Intelligence API offers Person Detection which detects each person in the video and recognizes a large amount of body parts, facial features, and clothing.

#### Object Detection: 
AutoML Vision Object Detection enables developers to train custom machine learning models that are capable of detecting individual objects in a given image along with its bounding box and label.

#### TensorFlow 
TensorFlow provides a computational framework for building ML models. TensorFlow provides a variety of different toolkits that allow you to construct models at your preferred level of abstraction. 

#### Tf.keras
A high-level API to build and train a neural network for classifying images in TensorFlow. 

#### Neural Networks 
A neural network is a model inspired from the brain. It is composed of layers, at least one of which is hidden, that consists of simple connected units or neurons followed by nonlinearities. 

#### Activation Function 
A function (for example, ReLU or sigmoid) that takes in the weighted sum of all of the inputs from the previous layer and then generates and passes an output value (typically nonlinear) to the next layer.
#### Relu 
effectively means if X>0 return X, else return 0. It passes values 0 or greater to the next layer in the network.

#### Softmax 
takes a set of values, and effectively picks the biggest one so you don't have to sort to find the largest value. For example, if the output of the last layer looks like .1, 0.1, 0.05, 0.1, 9.5, 0.1, 0.05, 0.05, 0.05], it returns ,0,0,0,1,0,0,0,0].

#### Loss
Loss indicates the model's performance by a number. If the model is performing better, loss will be a smaller number. Otherwise loss will be a larger number.

#### Optimizer
An optimizer is one of the two arguments required for compiling a tf.keras model. An Optimizer is an algorithm that modifies the attributes of the neural network like weights and learning rate. This helps in reducing the loss and improving accuracy.

#### Transfer Learning 
Sophisticated deep learning models have millions of parameters (weights) and training them from scratch often requires large amounts of data of computing resources. Transfer learning is a technique that shortcuts much of this by taking a piece of a model that has already been trained on a related task and reusing it in a new model.

#### Coefficient 
The coefficient plays a major role in machine learning as the prediction of the machine is dependent on the coefficient. Coefficient indicates the direction of the relationship between a predictor variable and the response variable.
A positive sign indicates that as the predictor variable(y )increases, the response variable(X) also increases.
A negative sign indicates that as the predictor variable(y) increases, the response variable(x) decreases.
 

## BigQuery ML Terms
#### Time Series
Time series data is data collected on the same subject at different points in time, such as GDP of a country by year, a stock price of a particular company over a period of time, or your own heartbeat recorded at each second. Any data that you can capture continuously at different time-intervals is a form of time series data.
***Components***: 
- Trend: moves up or down in a reasonably predictable pattern
- Seasonal: repeats over a specific period such as a day, week, month, season, etc.
- Random: residual fluctuations
 
#### Types of Time Series Forecast: 
1. Single (Univariate) 
1. Multiple (Multivariate)
 
#### Single Time series: - 
A univariate time series, as the name suggests, is a series with a single time-dependent variable. For example, if you are tracking hourly temperature values for a given region and want to forecast the future temperature using historical temperatures, this is univariate time series forecasting. Your data may look like this: 

 
#### Multivariate Time Series 
A Multivariate time series has more than one time-dependent variable. Each variable depends not only on its past values but also has some dependency on other variables. This dependency is used for forecasting future values.

 
### Time Series Forecasting Methods
Time series forecasting can broadly be categorized into the following categories:
Classical / Statistical Models — Moving Averages, Exponential Smoothing, ARIMA, SARIMA, TBATS
Machine Learning — Linear Regression, XGBoost, Random Forest, or any ML model with reduction methods
Deep Learning — RNN, LSTM
 
### ARIMA
ARIMA is one of the most popular classical methods for time series forecasting. It stands for autoregressive integrated moving average and is a type of model that forecasts a given time series based on its own past values, that is, its own lags and the lagged forecast errors. ARIMA consists of three components:

**Autoregression (AR)**: refers to a model that shows a changing variable that regresses on its own lagged, or prior, values.

**Integrated (I):** represents the differencing of raw observations to allow for the time series to become stationary (i.e., data values are replaced by the difference between the data values and the previous values).

**Moving average (MA):** incorporates the dependency between an observation and a residual error from a moving average model applied to lagged observations.
 
The "AR" part of ARIMA indicates that the evolving variable of interest is regressed on its own lagged (i.e., prior observed) values. 

The "I" (for "integrated") indicates that the data values have been replaced with the difference between their values and the previous values (and this differencing process may have been performed more than once). The purpose of each of these features is to make the model fit the data as well as possible.
The "MA" part indicates that the regression error is actually a linear combination of error terms whose values occurred contemporaneously and at various times in the past. 
 
