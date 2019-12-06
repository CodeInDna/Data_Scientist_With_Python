# Loading rainfall data
import pandas as pd

file1 = 'q1_rainfall_2013.csv'

rain2013 = pd.read_csv(file1, index_col='Month', parse_dates=True)

file2 = 'q1_rainfall_2014.csv'

rain2014 = pd.read_csv(file2, index_col='Month', parse_dates=True)

# Examining Rainfall Data
print(rain2013)

print(rain2014)

# Concatenating Rows
pd.concat([rain2013, rain2014], axis = 0)

# Using Multi-Index on Rows
rain1314 = pd.concat([rain2013, rain2014], keys=[2013, 2014], axis = 0)

# Concatenating Columns
rain1314 = pd.concat([rain2013, rain2014], axis = 1)

# Using Multi-Index on Columns
rain1314 = pd.concat([rain2013, rain2014], keys=[2013, 2014], axis = 1)

# pd.concat() with dict
rain_dict = {2013: rain2013, 2014: rain2014}
rain1314 = pd.concat(rain_dict, axis='columns')
print(rain1314)

# Concatenating vertically to get MultiIndexed rows
# When stacking a sequence of DataFrames vertically, it is sometimes desirable to construct a MultiIndex to indicate the DataFrame from which each row originated. This can be done by specifying the keys parameter in the call to pd.concat(), which generates a hierarchical index with the labels from keys as the outermost index label. So you don't have to rename the columns of each DataFrame as you load it. Instead, only the Index column needs to be specified.
# Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset. Once again, pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.
for medal in medal_types:

    file_name = "%s_top5.csv" % medal
    
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')
    
    # Append medal_df to medals
    medals.append(medal_df)
    
# Concatenate medals: medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'], axis= 0)

# Print medals in entirety
print(medals)