# Regression Mechanics
# y = ax + b
	# y = target
	# x = single feature
	# a,b = parameters of model
# How do we choose a and b?
# Define an error functions for any given line
	# Choose the line that minimizes the error function
	# The loss function: We minimize the sum of the squares of the residual.
	# OLS (Ordinary Least Squares): Minimize Sum of Squares of Residuals

# Fit & predict for regression
# Now, you will fit a linear regression and predict life expectancy using just one feature. You saw Andy do this earlier using the 'RM' feature of the Boston housing dataset. In this exercise, you will use the 'fertility' feature of the Gapminder dataset. Since the goal is to predict life expectancy, the target variable here is 'life'. The array for the target variable has been pre-loaded as y and the array for 'fertility' has been pre-loaded as X_fertility.
# A scatter plot with 'fertility' on the x-axis and 'life' on the y-axis has been generated. As you can see, there is a strongly negative correlation, so a linear regression should be able to capture this trend. Your job is to fit a linear regression and then predict the life expectancy, overlaying these predicted values on the plot to generate a regression line. You will also compute and print the R2 score using sckit-learn's .score() method.
# Import numpy and pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('../Dataset/Supervised Learning with scikit-learn/gm_2008_region.csv')

# # Create arrays for features and target variable
# y = df.life.values
# X = df.fertility.values

# # Print the dimensions of X and y before reshaping
# print("Dimensions of y before reshaping: {}".format(y.shape))
# print("Dimensions of X before reshaping: {}".format(X.shape))
# # Dimensions of y before reshaping: (139,)
# # Dimensions of X before reshaping: (139,)

# # Reshape X and y
# y = y.reshape(-1,1)
# X_fertility = X.reshape(-1,1)

# # Print the dimensions of X and y after reshaping
# print("Dimensions of y after reshaping: {}".format(y.shape))
# print("Dimensions of X after reshaping: {}".format(X_fertility.shape))

# # Import LinearRegression
# from sklearn.linear_model import LinearRegression

# # Create the regressor: reg
# reg = LinearRegression()

# # Create the prediction space
# prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

# # Fit the model to the data
# reg.fit(X_fertility,y)

# # Compute predictions over the prediction space: y_pred
# y_pred = reg.predict(prediction_space)
# # print(y_pred)
# # Print R^2 
# print(reg.score(X_fertility,y))

# # Plot regression line
# plt.scatter(X_fertility,y,color='blue')
# plt.plot(prediction_space, y_pred, color='black', linewidth=3)
# plt.show()
# Notice how the line captures the underlying trend in the data. And the performance is quite decent for this basic regression model with only one feature!

# Train/test split for regression
# As you learned in Chapter 1, train and test sets are vital to ensure that your supervised learning model is able to generalize well to new data. This was true for classification models, and is equally true for linear regression models.
# In this exercise, you will split the Gapminder dataset into training and testing sets, and then fit and predict a linear regression over all features. In addition to computing the R2 score, you will also compute the Root Mean Squared Error (RMSE), which is another commonly used metric to evaluate regression models. The feature array X and target variable array y have been pre-loaded for you from the DataFrame df.
# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
X = df.drop(['life', 'Region'], axis=1).values
# X = df.fertility.values
y = df.life.values

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# X_train = X_train.reshape(-1,1)
# X_test = X_test.reshape(-1,1)
# y_train = y_train.reshape(-1,1)
# y_test = y_test.reshape(-1,1)
# Create the regressor: reg_all
reg_all = LinearRegression()

# Fit the regressor to the training data
reg_all.fit(X_train,y_train)

# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)

# print(np.sum((y_test - X_test) ** 2)/len(X_test))
# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test))) # R^2: 0.8380468731430135
rmse = np.sqrt(mean_squared_error(y_test,y_pred)) # Root Mean Squared Error: 3.2476010800369455
print("Root Mean Squared Error: {}".format(rmse))

# Using all features has improved the model score. This makes sense, as the model has more information to learn from. However, there is one potential pitfall to this process.