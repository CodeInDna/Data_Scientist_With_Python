# In order to measure performance, we need to find accuracy is a equal to commonly-used metric
# The accuracy of a classifier is defined as the number of correct predictions divided by the total number of data-points.
# Which data should be used to compute accuracy?
# What we are interesting in is, How well will the model perform on new data ?
# Could compute accuracy on data used to fit classifier
# NOT indicative of ability to generalize
# Split data into Training and Test Set
# You train or fit the classifier on the Training Set
# Then you make predictions on the labeled test set and compare these predictions with the known labels.
# Compare predictions with the known labels

# TRAIN/ TEST SPLIT
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=21,stratify=y)
# The test_size keyword argument specifies what proportion of the original data is used for the test set.
# The random state kwarg sets a seed for the random number generator that splits the data into train and test.
# Setting the seed with same argument later will allow you to reproduce the exact split downstream.
# By Default 75% Training Data and 25% Test Data
# It is also best practice to perform your split so that the split reflects the labels on your data. That is, you want the labels to be distributed in train and test sets as they are in the original dataset. To achieve this, we use the keyword argument stratify equals y, where y the list of array containing the labels.
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)
y_pred  = knn.predict(X_test)
print(f"Test set predictions: {y_pred}")
knn.score(X_test, y_test) # 95%
# Model Complexity
# Larger k = smoother decision boundary = less complex model
# Smaller k = more complex model = can lead to overfitting
# <- Overfitting k Underfitting ->