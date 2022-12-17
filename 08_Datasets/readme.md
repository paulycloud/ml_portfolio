# Dataset Sources

1. TensorFlow Datasets | [Source](https://www.tensorflow.org/datasets)
1. Open ML Datasets | [Source](https://www.openml.org/search?type=data&status=active&sort=runs)
1. Google Dataset Search | [Source](https://datasetsearch.research.google.com/)
1. Google Cloud Marketplace Datasets | [Source](https://cloud.google.com/marketplace/browse?filter=solution-type:dataset&_ga=2.117206726.1548303019.1669322993-270543887.1669322993)
1. UCI Machine Learning Repository | [Source](https://archive.ics.uci.edu/ml/datasets.php)
1. [Grouplens](https://grouplens.org/about/what-is-grouplens/)

## TensorFlow Datasets
TensorFlow Datasets is a collection of datasets ready to use, with TensorFlow or other Python ML frameworks, such as Jax. All datasets are exposed as `tf.data.Datasets` , enabling easy-to-use and high-performance input pipelines. To get started see the guide and our list of datasets.

```python
import tensorflow as tf
import tensorflow_datasets as tfds

# Construct a tf.data.Dataset
ds = tfds.load('mnist', split='train', shuffle_files=True)

# Build your input pipeline
ds = ds.shuffle(1024).batch(32).prefetch(tf.data.AUTOTUNE)
for example in ds.take(1):
  image, label = example["image"], example["label"]
```

## OpenML Datasets
Datasets provide training data for machine learning models. OpenML datasets are uniformly formatted and come with rich meta-data to allow automated processing. You can sort or filter them by a range of different properties. Learn more.


## Google Dataset Search


## Google Cloud Marketplace Datasets 


## UCI Machine Learning Repository
The UCI Machine Learning Repository is a collection of databases, domain theories, and data generators that are used by the machine learning community for the empirical analysis of machine learning algorithms.



