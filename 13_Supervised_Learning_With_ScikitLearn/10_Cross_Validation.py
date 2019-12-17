# Cross-Validation Motivation
# Model performance is dependent on way the data in split
# Not representative of the model's ability to generalize
# Solution: Cross-Validation
# Cross-Validation and Model Performance
	# 5 Folds = 5-Fold CV
	# 10 Folds = 10-Fold CV
	# k Folds = k-Fold CV
	# More Folds = More Computationally Expensive

# 5-fold cross-validation
# Cross-validation is a vital step in evaluating a model. It maximizes the amount of data that is used to train the model, as during the course of training, the model is not only trained, but also tested on all of the available data.

# In this exercise, you will practice 5-fold cross validation on the Gapminder data. By default, scikit-learn's cross_val_score() function uses R2 as the metric of choice for regression. Since you are performing 5-fold cross-validation, the function will return 5 scores. Your job is to compute these 5 scores and then take their average.

# The DataFrame has been loaded as df and split into the feature/target variable arrays X and y. The modules pandas and numpy have been imported as pd and np, respectively.

# FOLDS    FOLD01 FOLD02 FOLD03 FOLD04 FOLD05
# SPLIT01  TEST   TRAIN TRAIN  TRAIN TRAIN 	METRIC_01
# SPLIT02  TRAIN  TEST	TRAIN  TRAIN TRAIN 	METRIC_02
# SPLIT03  TRAIN  TRAIN TEST   TRAIN TRAIN 	METRIC_03
# SPLIT04  TRAIN  TRAIN TRAIN  TEST  TRAIN 	METRIC_04
# SPLIT05  TRAIN  TRAIN TRAIN  TRAIN TEST 	METRIC_05

# Import the necessary modules
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg, X, y, cv=5)

# Print the 5-fold cross-validation scores
print(cv_scores)

print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))
# [0.81720569 0.82917058 0.90214134 0.80633989 0.94495637]
# Average 5-Fold CV Score: 0.8599627722793232
# Now that you have cross-validated your model, you can more confidently evaluate its predictions.
# K-Fold CV comparison
# Cross validation is essential but do not forget that the more folds you use, the more computationally expensive cross-validation becomes. In this exercise, you will explore this for yourself. Your job is to perform 3-fold cross-validation and then 10-fold cross-validation on the Gapminder dataset.
# In the IPython Shell, you can use %timeit to see how long each 3-fold CV takes compared to 10-fold CV by executing the following cv=3 and cv=10:
# %timeit cross_val_score(reg, X, y, cv = ____)
# pandas and numpy are available in the workspace as pd and np. The DataFrame has been loaded as df and the feature/target variable arrays X and y have been created.
# Import necessary modules
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Create a linear regression object: reg
reg = LinearRegression()

# Perform 3-fold CV
cvscores_3 = cross_val_score(reg,X,y,cv=3)
print(np.mean(cvscores_3))

# Perform 10-fold CV
cvscores_10 = cross_val_score(reg,X,y,cv=10)
print(np.mean(cvscores_10))