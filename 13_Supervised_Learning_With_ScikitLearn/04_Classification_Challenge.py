# The Classification Challenge
# Already labeled data is referred as Training Data

# k-Nearest Neighbors
#  The basic idea of K-NN is to predict the label of any data point by looking at the K.
# What the KNN algorithm essentially does is create a set of decision boundaries

# Scikit-learn fit and predict
# All machine learning models implemented as Python classes.
# These classes serve two purposes: They implement the algo for learning a model and predicting, while also storing all the information that is learned from the data.

# Training a model on the data = "fitting" a model to the data
	# .fit() method
# To predict the labels of new data: .predict() method

# Using scikit-learn to fit a classifier
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

iris = datasets.load_iris()

knn = KNeighborsClassifier(n_neighbors = 6)
# Then we fit this classifier to our training set, the labeled data
print(knn.fit(iris['data'], iris['target']))
# It Returns the Classifier Itself, and modified it to fit our data.

# KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#                      metric_params=None, n_jobs=None, n_neighbors=6, p=2,
#                      weights='uniform')

# Predicting on Unlabeled Data
# prediction = knn.predict(X_new)
# X_new.shape (3,4)
# print(f'Prediction {prediction}')
# Prediction: [1 1 0] # 1-Versicolor, 0- Setosa

# k-Nearest Neighbors: Fit
# Having explored the Congressional voting records dataset, it is time now to build your first classifier. In this exercise, you will fit a k-Nearest Neighbors classifier to the voting dataset, which has once again been pre-loaded for you into a DataFrame df.

# In the video, Hugo discussed the importance of ensuring your data adheres to the format required by the scikit-learn API. The features need to be in an array where each column is a feature and each row a different observation or data point - in this case, a Congressman's voting record. The target needs to be a single column with the same number of observations as the feature data. We have done this for you in this exercise. Notice we named the feature array X and response variable y: This is in accordance with the common scikit-learn practice.

# Your job is to create an instance of a k-NN classifier with 6 neighbors (by specifying the n_neighbors parameter) and then fit it to the data. The data has been pre-loaded into a DataFrame called df.

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors = 6)

# Fit the classifier to the data
knn.fit(X,y)

# KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=1, n_neighbors=6, p=2, weights='uniform')
# Now that your k-NN classifier with 6 neighbors has been fit to the data, it can be used to predict the labels of new data points.

# k-Nearest Neighbors: Predict
# Having fit a k-NN classifier, you can now use it to predict the label of a new data point. However, there is no unlabeled data available since all of it was used to fit the model! You can still use the .predict() method on the X that was used to fit the model, but it is not a good indicator of the model's ability to generalize to new, unseen data.

# In the next video, Hugo will discuss a solution to this problem. For now, a random unlabeled data point has been generated and is available to you as X_new. You will use your classifier to predict the label for this new data point, as well as on the training data X that the model has already seen. Using .predict() on X_new will generate 1 prediction, while using it on X will generate 435 predictions: 1 for each sample.

# The DataFrame has been pre-loaded as df. This time, you will create the feature array X and target variable array y yourself.

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier 

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors = 6)

# Fit the classifier to the data
knn.fit(X,y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))

# id your model predict 'democrat' or 'republican'? How sure can you be of its predictions? In other words, how can you measure its performance? This is what you will learn in the next video.

