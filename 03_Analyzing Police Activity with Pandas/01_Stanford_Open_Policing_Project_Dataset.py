# Introduction to the dataset
# Traffic Stops by Polic Officers for 31 State
# https://openpolicing.stanford.edu/

# Preparing the Data
	# Examine the Data
	# Clean the Data
import pandas as pd
ri = pd.read_csv('../Dataset/Analyzing Police Activity with Pandas/police.csv')
print(ri.head())

# Each row represents one traffic stop
# Nan Indicates a missing value

# Locating Missing Values
print(ri.isnull().head(5)) # Generate a boolean value gives True if the value is missing and False if not 

print(ri.isnull().sum()) # Indicates Number of missing values
# [91741 rows x 15 columns]
# state                     0
# stop_date                 0
# stop_time                 0
# county_name           91741
# driver_gender          5205
# driver_race            5202
# violation_raw          5202
# violation              5202
# search_conducted          0
# search_type           88434
# stop_outcome           5202
# is_arrested            5202
# stop_duration          5202
# drugs_related_stop        0
# district                  0
# dtype: int64

print(ri.shape) # County_name column only contains missing values
# Drop county_name using the drop() method
ri.drop('county_name', axis='columns', inplace=True)
print(ri)

# Dropping Rows
# dropna(): Drop rows based on the presence of missing values
ri.dropna(subset=['stop_date','stop_time'], inplace=True)

# Examining the dataset
# Throughout this course, you'll be analyzing a dataset of traffic stops in Rhode Island that was collected by the Stanford Open Policing Project.

# Before beginning your analysis, it's important that you familiarize yourself with the dataset. In this exercise, you'll read the dataset into pandas, examine the first few rows, and then count the number of missing values.

# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('police.csv')

# Examine the head of the DataFrame
print(ri.head())

# Count the number of missing values in each column
print(ri.isnull().sum())

# Dropping columns
# Often, a DataFrame will contain columns that are not useful to your analysis. Such columns should be dropped from the DataFrame, to make it easier for you to focus on the remaining columns.
# In this exercise, you'll drop the county_name column because it only contains missing values, and you'll drop the state column because all of the traffic stops took place in one state (Rhode Island). Thus, these columns can be dropped because they contain no useful information. The number of missing values in each column has been printed to the console for you.
# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(['county_name', 'state'], axis='columns', inplace=True)

# Examine the shape of the DataFrame (again)
print(ri.shape)

# Dropping rows
# When you know that a specific column will be critical to your analysis, and only a small fraction of rows are missing a value in that column, it often makes sense to remove those rows from the dataset.

# During this course, the driver_gender column will be critical to many of your analyses. Because only a small fraction of rows are missing driver_gender, we'll drop those rows from the dataset.
# Count the number of missing values in each column
print(ri.isnull().sum())

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Count the number of missing values in each column (again)
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

# stop_date                 0
# stop_time                 0
# driver_gender          5205
# driver_race            5202
# violation_raw          5202
# violation              5202
# search_conducted          0
# search_type           88434
# stop_outcome           5202
# is_arrested            5202
# stop_duration          5202
# drugs_related_stop        0
# district                  0
# dtype: int64

# stop_date                 0
# stop_time                 0
# driver_gender             0
# driver_race               0
# violation_raw             0
# violation                 0
# search_conducted          0
# search_type           83229
# stop_outcome              0
# is_arrested               0
# stop_duration             0
# drugs_related_stop        0
# district                  0
# dtype: int64

# (86536, 13)

# Examining the Data Types
# ri.dtypes

# stop_date             object
# stop_time             object
# driver_gender         object
# driver_race           object
# violation_raw         object
# violation             object
# search_conducted        bool
# search_type           object
# stop_outcome          object
# is_arrested           object
# stop_duration         object
# drugs_related_stop      bool
# district              object

# Why do data types matter?
# Affects which operations you can perform
# Avoid storing data as strings (when possible)
# int, float: enables mathematical operations
# datetime: enables date-based attributes and methods
# category: uses less memory and runs faster
# bool: enables logical and mathematical operations

# Fixing a Data Type
# apple

#       date   time   price
# 0  2/13/18  16:00  164.34
# 1  2/14/18  16:00  167.37
# 2  2/15/18  16:00  172.99
# apple.price.dtype
# dtype('O')
# apple['price'] = apple.price.astype('float')
# apple.price.dtype
# dtype('float64')
# Dot notation: apple.price
# Bracket notation: apple['price']

# Fixing a data type
# We saw in the previous exercise that the is_arrested column currently has the object data type. In this exercise, we'll change the data type to bool, which is the most suitable type for a column containing True and False values.

# Fixing the data type will enable us to use mathematical operations on the is_arrested column that would not be possible otherwise.
# Examine the head of the 'is_arrested' column
print(ri.is_arrested.head())

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype('bool')

# Check the data type of 'is_arrested' 
print(ri.is_arrested.dtype)