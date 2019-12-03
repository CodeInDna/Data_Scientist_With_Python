import pandas as pd

df = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/sales.csv', index_col='month')

print(df['eggs'])
print(type(df['eggs'])) # <class 'pandas.core.series.Series'>

# Series is a one-dimensional array with labelled index
# Another way to think of a dataframe is a labelled two-dimensional array with series for column, sharing common row-labels.

# Slicing and Indexing Series
print(df['eggs'][1:4]) # Part of the eggs column
print(df['eggs'][4]) # The value associated with May

# Using .loc[]
print(df.loc[:, 'eggs':'salt']) # All rows, some columns

# Using .loc[]
print(df.loc['Jan':'Apr', :]) # Some rows, all columns
# month   eggs  salt  spam
# Jan      47  12.0    17
# Feb     110  50.0    31
# Mar     221  89.0    72
# Apr      77  87.0    20

# Using .loc[]
print(df.loc['Mar':'May', 'salt':'spam'])

# Using iloc[]
print(df.iloc[2:5, 1:]) # A block from middle of the DataFrame

# Using lists rather than slices
print(df.loc['Jan':'May', ['eggs','spam']])