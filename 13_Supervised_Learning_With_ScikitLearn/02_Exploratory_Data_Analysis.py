# EDA
# THE IRIS DATASET
# Features:
	# Petal length
	# Petal Width
	# Sepal Length
	# Sepal Width

# Target Variable: Species
	# Versicolor
	# Virginica
	# Setosa

# The Iris Dataset in Scikit-learn
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

iris = datasets.load_iris()

print(type(iris)) # <class 'sklearn.utils.Bunch'> # Set of Key-Value Pairs, Dictionary

print(iris.keys()) # dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])

print(type(iris.data), type(iris.target)) # <class 'numpy.ndarray'> <class 'numpy.ndarray'>

print(iris.data.shape) # (150, 4)

# Samples are in rows, features are in Columns

print(iris.target_names) # ['setosa' 'versicolor' 'virginica']
print(iris.target) # [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2]

X = iris.data
Y = iris.target
df = pd.DataFrame(X, columns= iris.feature_names)
print(df.head())
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# 0                5.1               3.5                1.4               0.2
# 1                4.9               3.0                1.4               0.2
# 2                4.7               3.2                1.3               0.2
# 3                4.6               3.1                1.5               0.2
# 4                5.0               3.6                1.4               0.2

pd.plotting.scatter_matrix(df, c = Y, figsize=[8,8], s=150, marker='D')
plt.show()