# Loading Weather Data
import pandas as pd
weather = pd.read_csv('../Datasets/Merging DataFrames with Pandas/pittsburgh2013.csv', index_col= 'Date', parse_dates=True)
print(weather.loc['2013-7-1':'2013-7-7', 'PrecipitationIn'])

# Date
# 2013-07-01    0.18
# 2013-07-02    0.14
# 2013-07-03    0.00
# 2013-07-04    0.25
# 2013-07-05    0.02
# 2013-07-06    0.06
# 2013-07-07    0.10
# Name: PrecipitationIn, dtype: float64

# Scalar Multiplication
print(weather.loc['2013-7-1':'2013-7-7', 'PrecipitationIn'] * 2.54)
# Date
# 2013-07-01    0.4572
# 2013-07-02    0.3556
# 2013-07-03    0.0000
# 2013-07-04    0.6350
# 2013-07-05    0.0508
# 2013-07-06    0.1524
# 2013-07-07    0.2540
# Name: PrecipitationIn, dtype: float64

# Absolute Temperature Range
week1_range = weather.loc['2013-7-1':'2013-7-7', ['Min TemperatureF', 'Max TemperatureF']] 
print(week1_range)
#             Min TemperatureF  Max TemperatureF
# Date
# 2013-07-01                66                79
# 2013-07-02                66                84
# 2013-07-03                71                86
# 2013-07-04                70                86
# 2013-07-05                69                86
# 2013-07-06                70                89
# 2013-07-07                70                77

# Average Temperature
week1_mean = weather.loc['2013-7-1':'2013-7-7', 'Mean TemperatureF'] 

# Relative Temperature Range
print(week1_range.divide(week1_mean, axis=0))
#             Min TemperatureF  Max TemperatureF
# Date
# 2013-07-01          0.916667          1.097222
# 2013-07-02          0.891892          1.135135
# 2013-07-03          0.910256          1.102564
# 2013-07-04          0.909091          1.116883
# 2013-07-05          0.907895          1.131579
# 2013-07-06          0.897436          1.141026
# 2013-07-07          0.972222          1.069444

# Percentage Changes
print(week1_mean.pct_change() * 100)
# Date
# 2013-07-01         NaN
# 2013-07-02    2.777778
# 2013-07-03    5.405405
# 2013-07-04   -1.282051
# 2013-07-05   -1.298701
# 2013-07-06    2.631579
# 2013-07-07   -7.692308
# Name: Mean TemperatureF, dtype: float64

# Using a fill_value
bronze.add(silver, fill_value = 0)

# Chaining .add()
bronze.add(silver, fill_value = 0).add(gold, fill_value=0)

# Broadcasting in arithmetic formulas

# In this exercise, you'll work with weather data pulled from wunderground.com. The DataFrame weather has been pre-loaded along with pandas as pd. It has 365 rows (observed each day of the year 2013 in Pittsburgh, PA) and 22 columns reflecting different weather measurements each day.
# You'll subset a collection of columns related to temperature measurements in degrees Fahrenheit, convert them to degrees Celsius, and relabel the columns of the new DataFrame to reflect the change of units.
# Remember, ordinary arithmetic operators (like +, -, *, and /) broadcast scalar values to conforming DataFrames when combining scalars & DataFrames in arithmetic expressions. Broadcasting also works with pandas Series and NumPy arrays.
# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace('F','C')

# Print first 5 rows of temps_c
print(temps_c.head())
# In only three lines of code, you converted the units of 365 data points (over three columns) from degrees Fahrenheit to degrees Celsius.

# Computing percentage growth of GDP
# Your job in this exercise is to compute the yearly percent-change of US GDP (Gross Domestic Product) since 2008.

# The data has been obtained from the Federal Reserve Bank of St. Louis and is available in the file GDP.csv, which contains quarterly data; you will resample it to annual sampling and then compute the annual growth of GDP. For a refresher on resampling, check out the relevant material from pandas Foundations.
import pandas as pd

# Read 'GDP.csv' into a DataFrame: gdp
gdp = pd.read_csv('GDP.csv', index_col = 'DATE', parse_dates = True)

# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp['2008':]

# Print the last 8 rows of post2008
print(post2008.tail(8))

# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)

# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change() * 100

# Print yearly again
print(yearly)

# Fantastic! Note that the first column of the 'growth' column is NaN because there is no data for the year 2007.

# Converting currency of stocks
# In this exercise, stock prices in US Dollars for the S&P 500 in 2015 have been obtained from Yahoo Finance. The files sp500.csv for sp500 and exchange.csv for the exchange rates are both provided to you.
# Using the daily exchange rate to Pounds Sterling, your task is to convert both the Open and Close column prices.
# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv', index_col= 'Date', parse_dates=True)

# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv', index_col= 'Date', parse_dates=True)

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open','Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'], axis=0)

# Print the head of pounds
print(pounds.head())

# Now that you've become familiar with how to share information between DataFrames, you'll learn about concatenating DataFrames in the next chapter.