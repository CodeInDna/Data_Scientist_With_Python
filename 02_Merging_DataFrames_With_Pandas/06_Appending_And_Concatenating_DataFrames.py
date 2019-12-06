# Appending DataFrames with ignore_index
# In this exercise, you'll use the Baby Names Dataset (from data.gov) again. This time, both DataFrames names_1981 and names_1881 are loaded without specifying an Index column (so the default Indexes for both are RangeIndexes).
# You'll use the DataFrame .append() method to make a DataFrame combined_names. To distinguish rows from the original two DataFrames, you'll add a 'year' column to each with the year (1881 or 1981 in this case). In addition, you'll specify ignore_index=True so that the index values are not used along the concatenation axis. The resulting axis will instead be labeled 0, 1, ..., n-1, which is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information.
# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981

# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981, ignore_index=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

# Print all rows that contain the name 'Morgan'
print(combined_names.loc[combined_names['name'] == 'Morgan'])

# Concatenating pandas DataFrames along column axis
# The function pd.concat() can concatenate DataFrames horizontally as well as vertically (vertical is the default). To make the DataFrames stack horizontally, you have to specify the keyword argument axis=1 or axis='columns'.

# In this exercise, you'll use weather data with maximum and mean daily temperatures sampled at different rates (quarterly versus monthly). You'll concatenate the rows of both and see that, where rows are missing in the coarser DataFrame, null values are inserted in the concatenated DataFrame. This corresponds to an outer join (which you will explore in more detail in later exercises).

# The files 'quarterly_max_temp.csv' and 'monthly_mean_temp.csv' have been pre-loaded into the DataFrames weather_max and weather_mean respectively, and pandas has been imported as pd.

# Create a list of weather_max and weather_mean
weather_list = [weather_max, weather_mean]

# Concatenate weather_list horizontally
weather = pd.concat(weather_list, axis = 1)

# Print weather
print(weather)

#      Max TemperatureF  Mean TemperatureF
# Apr              89.0          53.100000
# Aug               NaN          70.000000
# Dec               NaN          34.935484
# Feb               NaN          28.714286
# Jan              68.0          32.354839
# Jul              91.0          72.870968
# Jun               NaN          70.133333
# Mar               NaN          35.000000
# May               NaN          62.612903
# Nov               NaN          39.800000
# Oct              84.0          55.451613
# Sep               NaN          63.766667