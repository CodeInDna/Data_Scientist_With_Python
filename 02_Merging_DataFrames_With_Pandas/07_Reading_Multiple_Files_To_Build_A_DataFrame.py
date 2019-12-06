# Reading multiple files to build a DataFrame
# It is often convenient to build a large DataFrame by parsing many files as DataFrames and concatenating them all at once. You'll do this here with three files, but, in principle, this approach can be used to combine data from dozens or hundreds of files.

# Here, you'll work with DataFrames compiled from The Guardian's Olympic medal dataset.

# pandas has been imported as pd and the list medal_types has been pre-loaded for you, which contains the strings 'bronze', 'silver', and 'gold'.
#Initialize an empyy list: medals
medals =[]

for medal in medal_types:
    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    # Create list of column names: columns
    columns = ['Country', medal]
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, header = 0, index_col='Country', names = columns)
    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals_df
medals_df = pd.concat(medals, axis = 1)

# Print medals_df
print(medals_df)
#                 bronze  silver    gold
# France           475.0   461.0     NaN
# Germany          454.0     NaN   407.0
# Italy              NaN   394.0   460.0
# Soviet Union     584.0   627.0   838.0
# United Kingdom   505.0   591.0   498.0
# United States   1052.0  1195.0  2088.0