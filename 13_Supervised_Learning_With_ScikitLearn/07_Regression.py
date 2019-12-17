# In Regression, Target Variable is Continuous, like price of a house
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

boston = pd.read_csv('../Dataset/Supervised Learning with scikit-learn/boston.csv')

print(boston.head())

X = boston.drop('MEDV', axis=1).values
y = boston.MEDV.values # MEDV : Median values of Owner Occupied Home in Thousands.

# print(X)
# print(y)
print(X.shape) # 506,13
print(y.shape) # 506

# Task_01
# Predicting house value from a single feature
X_rooms = X[:,5]
print(type(X_rooms), type(y)) # <class 'numpy.ndarray'> <class 'numpy.ndarray'>
print(X_rooms.ndim, y.ndim) # 1  1
print(X_rooms.shape, y.shape) # (506,) (506,)
X_Reshape = X_rooms.reshape(-1,1) 
y_Reshape = y.reshape(-1,1)
# To Check the Dimension of the Array
print(X_Reshape.ndim, y_Reshape.ndim) # 2 2
print(X_Reshape.shape, y_Reshape.shape) # (506, 1) (506, 1)

# Fitting a Regression Model
reg = linear_model.LinearRegression()
reg.fit(X_Reshape, y_Reshape)
prediction_space = np.linspace(min(X_Reshape), max(X_Reshape)).reshape(-1,1)
plt.scatter(X_Reshape, y_Reshape, color='blue')
plt.plot(prediction_space, reg.predict(prediction_space))
plt.show()
# QUIZ

# Which of the following is a regression problem?
# Andy introduced regression to you using the Boston housing dataset. But regression models can be used in a variety of contexts to solve a variety of different problems.

# Given below are four example applications of machine learning. Your job is to pick the one that is best framed as a regression problem.
# An e-commerce company using labeled customer data to predict whether or not a customer will purchase a particular item.

# A healthcare company using data about cancer tumors (such as their geometric measurements) to predict whether a new tumor is benign or malignant.

# A restaurant using review data to ascribe positive or negative sentiment to a given review.

# A bike share company using time and weather data to predict the number of bikes being rented at any given hour. <- 
# The target variable here - the number of bike rentals at any given hour - is quantitative, so this is best framed as a regression problem.