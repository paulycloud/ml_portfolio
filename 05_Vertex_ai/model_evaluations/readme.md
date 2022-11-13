
# Model Evaluations
Vertex AI provides model evaluation metrics, such as precision and recall, to help you determine the performance of your models.

## Image Evaluations 
**AuPRC:** The area under the precision-recall (PR) curve, also referred to as average precision. This value ranges from zero to one, where a higher value indicates a higher-quality model.

**Log loss**: The cross-entropy between the model predictions and the target values. This ranges from zero to infinity, where a lower value indicates a higher-quality model.

**Confidence threshold**: A confidence score that determines which predictions to return. A model returns predictions that are at this value or higher. A higher confidence threshold increases precision but lowers recall. Vertex AI returns confidence metrics at different threshold values to show how the threshold affects precision and recall.

**Recall**: The fraction of predictions with this class that the model correctly predicted. Also called true positive rate.

**Precision**: The fraction of classification predictions produced by the model that were correct.

**Confusion matrix:** A confusion matrix shows how often a model correctly predicted a result. For incorrectly predicted results, the matrix shows what the model predicted instead. The confusion matrix helps you understand where your model is "confusing" two results.

## Tabular Evaluations

### Classification 
**AuPRC**: The area under the precision-recall (PR) curve, also referred to as average precision. This value ranges from zero to one, where a higher value indicates a higher-quality model.

**AuROC**: The area under receiver operating characteristic curve. This ranges from zero to one, where a higher value indicates a higher-quality model.

Log loss: The cross-entropy between the model predictions and the target values. This ranges from zero to infinity, where a lower value indicates a higher-quality model.

Confidence threshold: A confidence score that determines which predictions to return. A model returns predictions that are at this value or higher. A higher confidence threshold increases precision but lowers recall. Vertex AI returns confidence metrics at different threshold values to show how the threshold affects precision and recall.

**Recall**: The fraction of predictions with this class that the model correctly predicted. Also called true positive rate.

***Recall at 1***: The recall (true positive rate) when only considering the label that has the highest prediction score and not below the confidence threshold for each example.

**Precision:** The fraction of classification predictions produced by the model that were correct.

***Precision at 1***: The precision when only considering the label that has the highest prediction score and not below the confidence threshold for each example.

**F1 score**: The harmonic mean of precision and recall. F1 is a useful metric if you're looking for a balance between precision and recall and there's an uneven class distribution.

***F1 score at 1***: The harmonic mean of recall at 1 and precision at 1.

**Confusion matrix**: A confusion matrix shows how often a model correctly predicted a result. For incorrectly predicted results, the matrix shows what the model predicted instead. The confusion matrix helps you understand where your model is "confusing" two results.

***True negative count***: The number of times a model correctly predicted a negative class.

***True positive count:*** The number of times a model correctly predicted a positive class.

***False negative count:*** The number of times a model mistakenly predicted a negative class.

***False positive count:*** The number of times a model mistakenly predicted a positive class.

***False positive rate:*** The fraction of incorrectly predicted results out of all predicted results.

***False positive rate at 1:*** The false positive rate when only considering the label that has the highest prediction score and not below the confidence threshold for each example.

**Model feature attributions:** Vertex AI shows you how much each feature impacts a model. The values are provided as a percentage for each feature: the higher the percentage, the more impact the feature had on model training. Review this information to ensure that all of the most important features make sense for your data and business problem.

### Regression 

**MAE**: The mean absolute error (MAE) is the average absolute difference between the target values and the predicted values. This metric ranges from zero to infinity; a lower value indicates a higher quality model.

**RMSE**: The root-mean-squared error is the square root of the average squared difference between the target and predicted values. RMSE is more sensitive to outliers than MAE,so if you're concerned about large errors, then RMSE can be a more useful metric to evaluate. Similar to MAE, a smaller value indicates a higher quality model (0 represents a perfect predictor).

**RMSLE**: The root-mean-squared logarithmic error metric is similar to RMSE, except that it uses the natural logarithm of the predicted and actual values plus 1. RMSLE penalizes under-prediction more heavily than over-prediction. It can also be a good metric when you don't want to penalize differences for large prediction values more heavily than for small prediction values. This metric ranges from zero to infinity; a lower value indicates a higher quality model. The RMSLE evaluation metric is returned only if all label and predicted values are non-negative.

***r^2***: r squared (r^2) is the square of the Pearson correlation coefficient between the labels and predicted values. This metric ranges between zero and one; a higher value indicates a higher quality model.
MAPE: Mean absolute percentage error (MAPE) is the average absolute percentage difference between the labels and the predicted values. This metric ranges between zero and infinity; a lower value indicates a higher quality model.

**MAPE** is not shown if the target column contains any 0 values. In this case, MAPE is undefined.
Model feature attributions: Vertex AI shows you how much each feature impacts a model. The values are provided as a percentage for each feature: the higher the percentage, the more impact the feature had on model training. Review this information to ensure that all of the most important features make sense for your data and business problem.

### Forecasting 

MAE: The mean absolute error (MAE) is the average absolute difference between the target values and the predicted values. This metric ranges from zero to infinity; a lower value indicates a higher quality model.

RMSE: The root-mean-squared error is the square root of the average squared difference between the target and predicted values. RMSE is more sensitive to outliers than MAE,so if you're concerned about large errors, then 

RMSE can be a more useful metric to evaluate. Similar to MAE, a smaller value indicates a higher quality model (0 represents a perfect predictor).

RMSLE: The root-mean-squared logarithmic error metric is similar to RMSE, except that it uses the natural logarithm of the predicted and actual values plus 1. RMSLE penalizes under-prediction more heavily than over-prediction. It can also be a good metric when you don't want to penalize differences for large prediction values more heavily than for small prediction values. This metric ranges from zero to infinity; a lower value indicates a higher quality model. The RMSLE evaluation metric is returned only if all label and predicted values are non-negative.

r^2: r squared (r^2) is the square of the Pearson correlation coefficient between the labels and predicted values. This metric ranges between zero and one; a higher value indicates a higher quality model.

MAPE: Mean absolute percentage error (MAPE) is the average absolute percentage difference between the labels and the predicted values. This metric ranges between zero and infinity; a lower value indicates a higher quality model.

MAPE is not shown if the target column contains any 0 values. In this case, MAPE is undefined.

WAPE: Weighted absolute percentage error (WAPE) is the overall difference between the value predicted by a model and the values observed over the values observed. Compared to RMSE, WAPE is weighted towards the overall differences rather than individual differences, which can be highly influenced by low or intermittent values. A lower value indicates a higher quality model.

RMSPE: Root mean squared percentage error (RMPSE) shows RMSE as a percentage of the actual values instead of an absolute number. A lower value indicates a higher quality model.

Quantile: The percent quantile, which indicates the probability that an observed value will be below the predicted value. For example, at the 0.5 quantile, the observed values are expected to be lower than the predicted values 50% of the time.

Observed quantile: Shows the percentage of true values that were less than the predicted value for a given quantile.

Scaled pinball loss: The scaled pinball loss at a particular quantile. A lower value indicates a higher quality model at the given quantile.

## Text Evaluations


## Video Evaluations



--------------------------------------------------------------------------------

_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._
Find all my social links here

#### All My Links
[BioLink](https://bio.link/paulkamau)


#### Buy Me Coffee
[Cashapp](https://bio.link/paulkamau)
[PayPal](https://paypal.me/paulkamau)