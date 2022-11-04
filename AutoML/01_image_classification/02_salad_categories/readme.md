# 02 Classify salad categories with AutoML

The purpose of this project is to use AutoML image object detection model from a Python script, and then do a batch prediction using the Vertex AI SDK. 

The steps performed include:

- Create a Vertex `Dataset` resource.
- Train the model.
- View the model evaluation.
- Make a batch prediction.


### Dataset

The dataset used for this tutorial is the Salads category of the [OpenImages dataset](https://www.tensorflow.org/datasets/catalog/open_images_v4) from [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/overview). This dataset does not require any feature engineering. The version of the dataset you will use in this tutorial is stored in a public Cloud Storage bucket. The trained model predicts the bounding box locations and the corresponding type of salad items in an image from a class of five items: salad, seafood, tomato, baked goods, or cheese.

--------------------------------------------------------------------------------

_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._

[![](https://github.com/paulycloud/paulycloud/blob/main/assets/twitter.png)](https://twitter.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/linkedin.png)](https://www.linkedin.com/in/paulmkamau/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/insta.png)](https://www.instagram.com/paulykamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/behance.png)](https://www.behance.net/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dribbble.png)](https://dribbble.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/facebook.png)](https://www.facebook.com/paul.m.kamau.3/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/github.png)](https://github.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/medium.png)](https://medium.com/@paulkamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dev.png)](https://dev.to/paulycloud)