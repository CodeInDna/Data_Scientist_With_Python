import pandas as pd
sales = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/sales.csv')
print(sales.head())

# Setting Index
sales = sales.set_index(['state','month'])
print(sales)
#              eggs  salt  spam
# state month
# CA    1        47  12.0    17
#       2       110  50.0    31
# NY    1       221  89.0    72
#       2        77  87.0    20
# TX    1       132   NaN    52
#       2       205  60.0    55
print(sales.index)
# MultiIndex([('CA', 1),
#             ('CA', 2),
#             ('NY', 1),
#             ('NY', 2),
#             ('TX', 1),
#             ('TX', 2)],
#            names=['state', 'month'])
print(sales.index.name) # None
print(sales.index.names) # ['state', 'month']

# Sorting Index
sales = sales.sort_index()
print(sales)

# Extracting data with a MultiIndex
# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA', 'TX']])
#              eggs  salt  spam
# state month
# CA    1        47  12.0    17
#       2       110  50.0    31
# TX    1       132   NaN    52
#       2       205  60.0    55

# Print sales['CA':'TX']
print(sales['CA':'TX'])
#              eggs  salt  spam
# state month
# CA    1        47  12.0    17
#       2       110  50.0    31
# NY    1       221  89.0    72
#       2        77  87.0    20
# TX    1       132   NaN    52
#       2       205  60.0    55

# Using .loc[] with nonunique indexes
# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])

# Indexing multiple levels of a MultiIndex

# Looking up indexed data is fast and efficient. And you have already seen that lookups based on the outermost level of a MultiIndex work just like lookups on DataFrames that have a single-level Index.
# Looking up data based on inner levels of a MultiIndex can be a bit trickier. The trickiest of all these lookups are when you want to access some inner levels of the index. In this case, you need to use slice(None) in the slicing parameter for the outermost dimension(s) instead of the usual :, or use pd.IndexSlice. You can refer to the pandas documentation for more details. For example, in the video, Dhavide used the following code to extract rows from all Symbols for the dates Oct. 3rd through 4th inclusive:
# stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]
# Pay particular attention to the tuple (slice(None), slice('2016-10-03', '2016-10-04')).
# In this exercise, you will use your sales DataFrame to do some increasingly complex lookups. Remember that you can type sales.head() in the console to review the structure of the DataFrame!
# Look up data for NY in month 1 in sales: NY_month1
NY_month1 = sales.loc['NY',1]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA','TX'],2),:]

# Access the inner month index and look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2), :]