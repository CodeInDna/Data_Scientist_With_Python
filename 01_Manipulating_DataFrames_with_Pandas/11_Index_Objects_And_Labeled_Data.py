# Pandas Data Structures
# Key Building Blocks
	# Indexes: Sequence of labels
	# Series: 1D array with Index
	# DataFrames: 2D array with Series as columns
# Indexes
	# Immutable (Like Dictionary Keys)
	# Homogenous in Data Type (Like NumPy Arrays)
# Creating a Series
import pandas as pd
prices = [10.70, 10.86, 10.74, 10.71, 10.79]
shares = pd.Series(prices)
print(shares)
# 0    10.70
# 1    10.86
# 2    10.74
# 3    10.71
# 4    10.79
# dtype: float64
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
shares = pd.Series(prices, index = days)
print(shares)
# Mon     10.70
# Tue     10.86
# Wed     10.74
# Thur    10.71
# Fri     10.79
# dtype: float64
print(shares.index)
# Index(['Mon', ' Tue', 'Wed', 'Thur', 'Fri'], dtype='object')

print(shares.index[2])
# Wed

print(shares.index[:2])
# Index(['Mon', ' Tue'], dtype='object')

print(shares.index[-2:])
# Index(['Thur', 'Fri'], dtype='object')

print(shares.index.name)
# None

shares.index.name = 'Weekday'
print(shares)
# weekday
# Mon     10.70
# Tue     10.86
# Wed     10.74
# Thur    10.71
# Fri     10.79
# dtype: float64

sales = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/sales.csv', index_col='month')
# Modifying Index Entries
# shares.index[2] = 'Wednesday'
# TypeError("Index does not support mutable operations")

# Changing index of a DataFrame
# As you saw in the previous exercise, indexes are immutable objects. This means that if you want to change or modify the index in a DataFrame, then you need to change the whole index. You will do this now, using a list comprehension to create the new index.

# A list comprehension is a succinct way to generate a list in one line. For example, the following list comprehension generates a list that contains the cubes of all numbers from 0 to 9: cubes = [i**3 for i in range(10)]. This is equivalent to the following code:

# cubes = []
# for i in range(10):
#     cubes.append(i**3)
# Before getting started, print the sales DataFrame in the IPython Shell and verify that the index is given by month abbreviations containing lowercase characters.

# By the way, if you haven't downloaded it already, check out the Pandas Cheat Sheet. It includes an overview of the most important concepts, functions and methods and might come in handy if you ever need a quick refresher!

# Create the list of new indexes: new_idx
new_idx = [sale.upper() for sale in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)

# Changing index name labels
# Notice that in the previous exercise, the index was not labeled with a name. In this exercise, you will set its name to 'MONTHS'.

# Similarly, if all the columns are related in some way, you can provide a label for the set of columns.

# To get started, print the sales DataFrame in the IPython Shell and verify that the index has no name, only its data (the month names).
# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)

# Notice how in the first DataFrame, the index has a label, and in the second DataFrame, both the index as well as the columns have labels.

# Building an index, then a DataFrame
# You can also build the DataFrame and index independently, and then put them together. If you take this route, be careful, as any mistakes in generating the DataFrame or the index can cause the data and the index to be aligned incorrectly.
# In this exercise, the sales DataFrame has been provided for you without the month index. Your job is to build this index separately and then assign it to the sales DataFrame. Before getting started, print the sales DataFrame in the IPython Shell and note that it's missing the month information.
# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)