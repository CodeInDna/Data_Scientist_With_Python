# A Simple DataFrame
import pandas as pd

df = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/sales.csv', index_col='month')

print(df)
#        eggs  salt  spam
# month
# Jan      47  12.0    17
# Feb     110  50.0    31
# Mar     221  89.0    72
# Apr      77  87.0    20
# May     132   NaN    52
# Jun     205  60.0    55

# Indexing Using Square Brackets
print(df['salt']['Jan']) # 12.0

# Using column attribute and row label
print(df.eggs['Mar']) # 221

# Using the .loc accessor
print(df.loc['May', 'spam']) # 52 [RowSpecifier, ColumnSpecifier]

# Using the .iloc accessor
print(df.iloc[4, 2]) # 52 [RowSpecifier, ColumnSpecifier]

# Selecting only some columns
print(df[['salt', 'eggs']])