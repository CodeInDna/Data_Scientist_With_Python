# Slicing MultiIndexed DataFrames
# This exercise picks up where the last ended (again using The Guardian's Olympic medal dataset).

# You are provided with the MultiIndexed DataFrame as produced at the end of the preceding exercise. Your task is to sort the DataFrame and to use the pd.IndexSlice to extract specific slices. Check out this exercise from Manipulating DataFrames with pandas to refresh your memory on how to deal with MultiIndexed DataFrames.

# pandas has been imported for you as pd and the DataFrame medals is already in your namespace.
# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:,'United Kingdom'], :])

# It looks like only the United States and the Soviet Union have won more Silver medals than the United Kingdom.
#            Total
# Country              
# bronze United Kingdom  505.0
# gold   United Kingdom  498.0
# silver United Kingdom  591.0		

# Concatenating horizontally to get MultiIndexed columns
# It is also possible to construct a DataFrame with hierarchically indexed columns. For this exercise, you'll start with pandas imported and a list of three DataFrames called dataframes. All three DataFrames contain 'Company', 'Product', and 'Units' columns with a 'Date' column as the index pertaining to sales transactions during the month of February, 2015. The first DataFrame describes Hardware transactions, the second describes Software transactions, and the third, Service transactions.
# Your task is to concatenate the DataFrames horizontally and to create a MultiIndex on the columns. From there, you can summarize the resulting DataFrame and slice some information from it.
# Concatenate dataframes: february
february = pd.concat(dataframes, axis=1, keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['Feb. 2, 2015':'Feb. 8, 2015', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)

# Concatenating DataFrames from a dict
# You're now going to revisit the sales data you worked with earlier in the chapter. Three DataFrames jan, feb, and mar have been pre-loaded for you. Your task is to aggregate the sum of all sales over the 'Company' column into a single DataFrame. You'll do this by constructing a dictionary of these DataFrames and then concatenating them.
# Make the list of tuples: month_list
month_list = [('january', jan),('february', feb),('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)
#                           Units
#          Company               
# february Acme Coporation     34
#          Hooli               30
#          Initech             30
#          Mediacore           45
#          Streeplex           37
# january  Acme Coporation     76
#          Hooli               70
#          Initech             37
#          Mediacore           15
#          Streeplex           50
# march    Acme Coporation      5
#          Hooli               37
#          Initech             68
#          Mediacore           68
#          Streeplex           40

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])

#                     Units
#          Company         
# february Mediacore     45
# january  Mediacore     15
# march    Mediacore     68