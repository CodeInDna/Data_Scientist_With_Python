import pandas as pd

filename = '../Datasets/01_Manipulating_DataFrames_with_Pandas/sales.csv'
# Read in filename and set the index: election
df = pd.read_csv(filename, index_col='month')
print(df.salt > 60)

# When making selection, boolean series is called a filter

print(df[df.salt > 60])

# Combining Filters
print(df[(df.salt >= 50) & (df.eggs < 200)])
#        eggs  salt  spam
# month
# Feb     110  50.0    31
# Apr      77  87.0    20
       
print(df[(df.salt >= 50) | (df.eggs < 200)])
#        eggs  salt  spam
# month
# Jan      47  12.0    17
# Feb     110  50.0    31
# Mar     221  89.0    72
# Apr      77  87.0    20
# May     132   NaN    52
# Jun     205  60.0    55

# DataFrames with zeros and NaNs
df2 = df.copy()
df2['bacon'] = [0, 0, 50, 60, 70, 80]
print(df2)

# Select Columns with all nonzeroes
print(df2.loc[:, df2.all()])

# Select Columns with any nonzeroes
print(df2.loc[:, df2.any()])

# Select Columns with any NaNs
print(df.loc[:, df.isnull().any()])
#        salt
# month
# Jan    12.0
# Feb    50.0
# Mar    89.0
# Apr    87.0
# May     NaN
# Jun    60.0

# Select Columns without NaNs
print(df.loc[:, df.notnull().all()])
#        eggs  spam
# month
# Jan      47    17
# Feb     110    31
# Mar     221    72
# Apr      77    20
# May     132    52
# Jun     205    55

# Drop Rows with any NaNs
print(df.dropna(how='any'))
#        eggs  salt  spam
# month
# Jan      47  12.0    17
# Feb     110  50.0    31
# Mar     221  89.0    72
# Apr      77  87.0    20
# Jun     205  60.0    55