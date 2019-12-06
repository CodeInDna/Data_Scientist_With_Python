# Using with Arrays
import numpy as np
import pandas as pd

A = np.arange(8).reshape(2,4) + 0.1
print(A)
# [[0.1 1.1 2.1 3.1]
# [4.1 5.1 6.1 7.1]]

B = np.arange(6).reshape(2,3) + 0.2
print(B)
# [[0.2 1.2 2.2]
# [3.2 4.2 5.2]]

C = np.arange(12).reshape(3,4) + 0.3
print(C)
# [[ 0.3  1.3  2.3  3.3]
 # [ 4.3  5.3  6.3  7.3]
 # [ 8.3  9.3 10.3 11.3]]

print(np.hstack([B,A]))
# [[0.2 1.2 2.2 0.1 1.1 2.1 3.1]
#  [3.2 4.2 5.2 4.1 5.1 6.1 7.1]]
print(np.concatenate([B,A], axis=1))
# [[0.2 1.2 2.2 0.1 1.1 2.1 3.1]
#  [3.2 4.2 5.2 4.1 5.1 6.1 7.1]]

# Stacking Arrays Vertically
print(np.vstack([A,C]))
# [[ 0.1  1.1  2.1  3.1]
#  [ 4.1  5.1  6.1  7.1]
#  [ 0.3  1.3  2.3  3.3]
#  [ 4.3  5.3  6.3  7.3]
#  [ 8.3  9.3 10.3 11.3]]
print(np.concatenate([A,C], axis=0))
# [[ 0.1  1.1  2.1  3.1]
#  [ 4.1  5.1  6.1  7.1]
#  [ 0.3  1.3  2.3  3.3]
#  [ 4.3  5.3  6.3  7.3]
#  [ 8.3  9.3 10.3 11.3]]

# Joins
# Joining Tables: Combining Rows of Multiple Tables
# Outer Join
	# Union of Index Sets (All Labels, No repetition)
	# Missing Fields Filled with NaN
# Inner Join
	# Intersection of Index Sets(Only Common Labels)

# Concatenation and Inner Join
pd.concat([population, unemployment], axis=1, join = 'inner')
pd.concat([population, unemployment], axis=1, join = 'outer')

# Concatenating DataFrames with inner join
# Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset.

# The DataFrames bronze, silver, and gold have been pre-loaded for you.

# Your task is to compute an inner join.

# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, keys= ['bronze', 'silver', 'gold'], axis=1, join='inner')

# Print medals
print(medals)
#                 bronze  silver    gold
#                  Total   Total   Total
# Country                               
# United States   1052.0  1195.0  2088.0
# Soviet Union     584.0   627.0   838.0
# United Kingdom   505.0   591.0   498.0
# France, Italy, and Germany got dropped as part of the join since they are not present in each of bronze, silver, and gold. Therefore, the final DataFrame has only the United States, Soviet Union, and United Kingdom.


# Resampling & concatenating DataFrames with inner join
# In this exercise, you'll compare the historical 10-year GDP (Gross Domestic Product) growth in the US and in China. The data for the US starts in 1947 and is recorded quarterly; by contrast, the data for China starts in 1961 and is recorded annually.

# You'll need to use a combination of resampling and an inner join to align the index labels. You'll need an appropriate offset alias for resampling, and the method .resample() must be chained with some kind of aggregation method (.pct_change() and .last() in this case).

# pandas has been imported as pd, and the DataFrames china and us have been pre-loaded, with the output of china.head() and us.head() printed in the IPython Shell.
# Resample and tidy china: china_annual
china_annual = china.resample('A').last().pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').last().pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual],axis=1,join='inner')

# Resample gdp and print
print(gdp.resample('10A').last())

#                China        US
# Year                          
# 1971-12-31  0.988860  1.052270
# 1981-12-31  0.972048  1.750922
# 1991-12-31  0.962528  0.912380
# 2001-12-31  2.492511  0.704219
# 2011-12-31  4.623958  0.475082
# 2021-12-31  3.789936  0.361780

#  It looks like the 10 year GDP growth of China has been higher than the US since the 1990s.