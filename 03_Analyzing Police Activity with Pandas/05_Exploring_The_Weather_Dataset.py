# Examining the columns
weather = pd.read_csv('../Dataset/Analyzing Police Activity with Pandas/weather.csv')
weather.head()
#        STATION        DATE  TAVG  TMIN  TMAX  AWND  WSF2  WT01  WT02  WT03   
# 0  USW00014765  2005-01-01  44.0    35    53  8.95  25.1   1.0   NaN   NaN   
# 1  USW00014765  2005-01-02  36.0    28    44  9.40  14.1   NaN   NaN   NaN   
# 2  USW00014765  2005-01-03  49.0    44    53  6.93  17.0   1.0   NaN   NaN   
# 3  USW00014765  2005-01-04  42.0    39    45  6.93  16.1   1.0   NaN   NaN   
# 4  USW00014765  2005-01-05  36.0    28    43  7.83  17.0   1.0   NaN   NaN   

#    ...   WT11  WT13  WT14  WT15  WT16  WT17  WT18  WT19  WT21  WT22  
# 0  ...    NaN   1.0   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN  
# 1  ...    NaN   NaN   NaN   NaN   1.0   NaN   1.0   NaN   NaN   NaN  
# 2  ...    NaN   1.0   NaN   NaN   1.0   NaN   NaN   NaN   NaN   NaN  
# 3  ...    NaN   1.0   1.0   NaN   1.0   NaN   NaN   NaN   NaN   NaN  
# 4  ...    NaN   1.0   NaN   NaN   1.0   NaN   1.0   NaN   NaN   NaN
 
# TAVG, TMIN, TMAX: Temperature
# AWND, WSF2: Wind speed
# WT01 ... WT22: Bad weather conditions

# AWND - Average Wind Speed Miles Per Hour
# WSF2 - Fastest Wind Speed in Any 2 Minutes
# Examining wind speed
weather[['AWND', 'WSF2']].head()

#    AWND  WSF2
# 0  8.95  25.1
# 1  9.40  14.1
# 2  6.93  17.0
# 3  6.93  16.1
# 4  7.83  17.0

weather[['AWND', 'WSF2']].describe()

#               AWND         WSF2
# count  4017.000000  4017.000000
# mean      8.593707    19.274782
# std       3.364601     5.623866
# min       0.220000     4.900000
# 25%       6.260000    15.000000
# 50%       8.050000    17.900000
# 75%      10.290000    21.900000
# max      26.840000    48.100000

# Creating a box plot
weather[['AWND', 'WSF2']].plot(kind='box')
plt.show()

# Creating a histogram (1)
weather['WDIFF'] = weather.WSF2 - weather.AWND #  To Determine, If Fast Wind Speed is greater that Average Wind Speed, i.e. Just to Validate Data
weather.WDIFF.plot(kind='hist')
plt.show()

weather.WDIFF.plot(kind='hist', bins=20)
plt.show()

# Plotting the temperature
# In this exercise, you'll examine the temperature columns from the weather dataset to assess whether the data seems trustworthy. First you'll print the summary statistics, and then you'll visualize the data using a box plot.

# When deciding whether the values seem reasonable, keep in mind that the temperature is measured in degrees Fahrenheit, not Celsius!

# Read 'weather.csv' into a DataFrame named 'weather'
weather = pd.read_csv('weather.csv')

# Describe the temperature columns
print(weather[['TMIN','TAVG','TMAX']].describe())

# Create a box plot of the temperature columns
weather[['TMIN','TAVG','TMAX']].plot(kind='box')

# Display the plot
plt.show()

# The temperature data looks good so far: the TAVG values are in between TMIN and TMAX, and the measurements and ranges seem reasonable.

# Plotting the temperature difference
# In this exercise, you'll continue to assess whether the dataset seems trustworthy by plotting the difference between the maximum and minimum temperatures.

# What do you notice about the resulting histogram? Does it match your expectations, or do you see anything unusual?

# Create a 'TDIFF' column that represents temperature difference
weather['TDIFF'] = weather['TMAX'] - weather['TMIN']

# Describe the 'TDIFF' column
print(weather['TDIFF'].describe())

# Create a histogram with 20 bins to visualize 'TDIFF'
weather['TDIFF'].plot(kind='hist', bins=20)

# Display the plot
plt.show()
# The TDIFF column has no negative values and its distribution is approximately normal, both of which are signs that the data is trustworthy.

# Categorizing the weather

# Selecting the DataFrame with Slice
weather.shape
# (4017, 28)
weather.columns
# Index(['STATION', 'DATE', 'TAVG', 'TMIN', 'TMAX', 'AWND', 'WSF2', 'WT01',
#        'WT02', 'WT03', 'WT04', 'WT05', 'WT06', 'WT07', 'WT08', 'WT09',
#        'WT10', 'WT11', 'WT13', 'WT14', 'WT15', 'WT16', 'WT17', 'WT18',
#        'WT19', 'WT21', 'WT22', 'TDIFF'],
#       dtype='object')
temp = weather.loc[:, 'TAVG':'TMAX']
temp.shape
# (4017, 3)
temp.columns
# Index(['TAVG', 'TMIN', 'TMAX'], dtype='object')

# DataFrame operations
temp.head()

#    TAVG  TMIN  TMAX
# 0  44.0    35    53
# 1  36.0    28    44
# 2  49.0    44    53
# 3  42.0    39    45
# 4  36.0    28    43

temp.sum()

# TAVG     63884.0
# TMIN    174677.0
# TMAX    246116.0

temp.sum(axis='columns').head()

# 0    132.0
# 1    108.0
# 2    146.0
# 3    126.0
# 4    107.0

# Mapping one set of values to another
ri.stop_duration.unique()
array(['0-15 Min', '16-30 Min', '30+ Min'], dtype=object)
mapping = {'0-15 Min':'short', '16-30 Min':'medium', '30+ Min':'long'}
ri['stop_length'] = ri.stop_duration.map(mapping)
ri.stop_length.dtype
# dtype('O')

# Changing data type from object to category
ri.stop_length.unique()
# array(['short', 'medium', 'long'], dtype=object)

# Category type stores the data more efficiently
# Allows you to specify a logical order for the categories
 
ri.stop_length.memory_usage(deep=True)
# 8689481 # Over 8MB
cats = ['short', 'medium', 'long']
ri['stop_length'] = ri.stop_length.astype('category', ordered=True,
                                          categories=cats)

ri.stop_length.memory_usage(deep=True)
# 3400602

Using ordered categories
ri.stop_length.head()

# stop_datetime
# 2005-01-04 12:55:00     short
# 2005-01-23 23:15:00     short
# 2005-02-17 04:15:00     short
# 2005-02-20 17:15:00    medium
# 2005-02-24 01:20:00     short
# Name: stop_length, dtype: category
# Categories (3, object): [short < medium < long]

ri[ri.stop_length > 'short'].shape
# (16959, 16)

ri.groupby('stop_length').is_arrested.mean()

stop_length
# short     0.013654
# medium    0.093595
# long      0.261572
# Name: is_arrested, dtype: float64

# Counting bad weather conditions
# The weather DataFrame contains 20 columns that start with 'WT', each of which represents a bad weather condition. For example:

# WT05 indicates "Hail"
# WT11 indicates "High or damaging winds"
# WT17 indicates "Freezing rain"
# For every row in the dataset, each WT column contains either a 1 (meaning the condition was present that day) or NaN (meaning the condition was not present).

# In this exercise, you'll quantify "how bad" the weather was each day by counting the number of 1 values in each row.

# Copy 'WT01' through 'WT22' to a new DataFrame
WT = weather.loc[:,'WT01':'WT22']

# Calculate the sum of each row in 'WT'
weather['bad_conditions'] = WT.sum(axis='columns')

# Replace missing values in 'bad_conditions' with '0'
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

# Create a histogram to visualize 'bad_conditions'
weather['bad_conditions'].plot(kind='hist')

# Display the plot
plt.show()

#  It looks like many days didn't have any bad weather conditions, and only a small portion of days had more than four bad weather conditions.

# # Rating the weather conditions
# In the previous exercise, you counted the number of bad weather conditions each day. In this exercise, you'll use the counts to create a rating system for the weather.

# The counts range from 0 to 9, and should be converted to ratings as follows:

# Convert 0 to 'good'
# Convert 1 through 4 to 'bad'
# Convert 5 through 9 to 'worse'

# Count the unique values in 'bad_conditions' and sort the index
print(weather.bad_conditions.value_counts().sort_index())

# Create a dictionary that maps integers to strings
mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad',4:'bad',5:'worse',6:'worse',7:'worse',8:'worse',9:'worse'}

# Convert the 'bad_conditions' integers to strings using the 'mapping'
weather['rating'] = weather.bad_conditions.map(mapping)

# Count the unique values in 'rating'
print(weather.rating.value_counts())
# bad      1836
# good     1749
# worse     432
# Name: rating, dtype: int64

# This rating system should make the weather condition data easier to understand.

# Changing the data type to category
# Since the rating column only has a few possible values, you'll change its data type to category in order to store the data more efficiently. You'll also specify a logical order for the categories, which will be useful for future exercises.

# Create a list of weather ratings in logical order
cats = ['good','bad','worse']

# Change the data type of 'rating' to category
weather['rating'] = weather.rating.astype('category', ordered=True, categories=cats)

# Examine the head of 'rating'
print(weather.rating.head())

# You'll use the rating column in future exercises to analyze the effects of weather on police behavior.