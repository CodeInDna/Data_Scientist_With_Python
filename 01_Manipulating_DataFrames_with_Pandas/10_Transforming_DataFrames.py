import pandas as pd
import numpy as np

df = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/sales.csv', index_col='month')

print(df.head())

# DataFrame Vectorized Methods
print(df.floordiv(12)) # Convert to Dozen Units

# NumPy Vectorized Functions
print(np.floor_divide(df, 12)) # Convert to Dozens Unit

# Plain Python Functions:
def dozens(n):
	return n//12

df.apply(dozens) # Convert to Dozens Unit

# Python Lambda Functions:
df.apply(lambda x:x//12)

# Storing a Transformation
df['dozens_of_eggs'] = df.eggs.floordiv(12)
print(df.head())

# The DataFrame Index
print(df.index)

# Working with String Values
df.index = df.index.str.upper()
print(df)
#        eggs  salt  spam  dozens_of_eggs
# month
# JAN      47  12.0    17               3
# FEB     110  50.0    31               9
# MAR     221  89.0    72              18
# APR      77  87.0    20               6
# MAY     132   NaN    52              11
# JUN     205  60.0    55              17

# Working with String Values
df.index = df.index.map(str.lower)
print(df)

# Defining columns using other columns
df['salty_eggs'] = df.salt + df.dozens_of_eggs
print(df)

# Using apply() to transform a column
# The .apply() method can be used on a pandas DataFrame to apply an arbitrary Python function to every element. In this exercise you'll take daily weather data in Pittsburgh in 2013 obtained from Weather Underground.
# A function to convert degrees Fahrenheit to degrees Celsius has been written for you. Your job is to use the .apply() method to perform this conversion on the 'Mean TemperatureF' and 'Mean Dew PointF' columns of the weather DataFrame.

weather = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/pittsburgh2013.csv')
# Write a function to convert degrees Fahrenheit to degrees Celsius: to_celsius
def to_celsius(F):
    return 5/9*(F - 32)

# Apply the function over 'Mean TemperatureF' and 'Mean Dew PointF': df_celsius
df_celsius = weather[['Mean TemperatureF', 'Mean Dew PointF']].apply(to_celsius)

# Reassign the column labels of df_celsius
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

# Print the output of df_celsius.head()
print(df_celsius.head())

#    Mean TemperatureC  Mean Dew PointC
# 0          -2.222222        -2.777778
# 1          -6.111111       -11.111111
# 2          -4.444444        -9.444444
# 3          -2.222222        -7.222222
# 4          -1.111111        -6.666667

# Using .map() with a dictionary
# The .map() method is used to transform values according to a Python dictionary look-up. In this exercise you'll practice this method while returning to working with the election DataFrame, which has been pre-loaded for you.
# Your job is to use a dictionary to map the values 'Obama' and 'Romney' in the 'winner' column to the values 'blue' and 'red', and assign the output to the new column 'color'.

election = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/pennsylvania2012_turnout.csv')
# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue', 'Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election.winner.map(red_vs_blue)

# Print the output of election.head()
print(election.head())
#       county state   total      Obama     Romney  winner  voters    turnout     margin color
# 0      Adams    PA   41973  35.482334  63.112001  Romney   61156  68.632677  27.629667   red
# 1  Allegheny    PA  614671  56.640219  42.185820   Obama  924351  66.497575  14.454399  blue
# 2  Armstrong    PA   28322  30.696985  67.901278  Romney   42147  67.198140  37.204293   red
# 3     Beaver    PA   80015  46.032619  52.637630  Romney  115157  69.483401   6.605012   red
# 4    Bedford    PA   21444  22.057452  76.986570  Romney   32189  66.619031  54.929118   red

# Using vectorized functions
# When performance is paramount, you should avoid using .apply() and .map() because those constructs perform Python for-loops over the data stored in a pandas Series or DataFrame. By using vectorized functions instead, you can loop over the data at the same speed as compiled code (C, Fortran, etc.)! NumPy, SciPy and pandas come with a variety of vectorized functions (called Universal Functions or UFuncs in NumPy).
# You can even write your own vectorized functions, but for now we will focus on the ones distributed by NumPy and pandas.
# In this exercise you're going to import the zscore function from scipy.stats and use it to compute the deviation in voter turnout in Pennsylvania from the mean in fractions of the standard deviation. In statistics, the z-score is the number of standard deviations by which an observation is above the mean - so if it is negative, it means the observation is below the mean.
# Instead of using .apply() as you did in the earlier exercises, the zscore UFunc will take a pandas Series as input and return a NumPy array. You will then assign the values of the NumPy array to a new column in the DataFrame. You will be working with the election DataFrame - it has been pre-loaded for you.
# Import zscore from scipy.stats
from scipy.stats import zscore

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore = zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))

# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore

# Print the output of election.head()
print(election.head())
# Using vectorized functions like this fully leverages the power of pandas.