# Merging Datasets
# Preparing the first DataFrame
apple

#                         date   time   price
# date_and_time                              
# 2018-02-14 09:30:00  2/14/18   9:30  163.04
# 2018-02-14 16:00:00  2/14/18  16:00  167.37
# 2018-02-15 09:30:00  2/15/18   9:30  169.79
# 2018-02-15 16:00:00  2/15/18  16:00  172.99
apple.reset_index(inplace=True)
apple

#         date_and_time     date   time   price
# 0 2018-02-14 09:30:00  2/14/18   9:30  163.04
# 1 2018-02-14 16:00:00  2/14/18  16:00  167.37
# 2 2018-02-15 09:30:00  2/15/18   9:30  169.79
# 3 2018-02-15 16:00:00  2/15/18  16:00  172.99

# Preparing the second DataFrame
high_low

#       DATE    HIGH     LOW
# 0  2/14/18  167.54  162.88
# 1  2/15/18  173.09  169.00
# 2  2/16/18  174.82  171.77
high = high_low[['DATE', 'HIGH']]
high

#       DATE    HIGH
# 0  2/14/18  167.54
# 1  2/15/18  173.09
# 2  2/16/18  174.82

# Merging the DataFrames
apple_high = pd.merge(left=apple, right=high, left_on='date',
                      right_on='DATE', how='left')
 
# left=apple: Left DataFrame
# right=high: Right DataFrame
# left_on='date': Key column in left DataFrame
# right_on='DATE': Key column in right DataFrame
# how='left': Type of join

# Comparing the DataFrames
# apple_high

#         date_and_time     date   time   price     DATE    HIGH
# 0 2018-02-14 09:30:00  2/14/18   9:30  163.04  2/14/18  167.54
# 1 2018-02-14 16:00:00  2/14/18  16:00  167.37  2/14/18  167.54
# 2 2018-02-15 09:30:00  2/15/18   9:30  169.79  2/15/18  173.09
# 3 2018-02-15 16:00:00  2/15/18  16:00  172.99  2/15/18  173.09
# apple

#         date_and_time     date   time   price
# 0 2018-02-14 09:30:00  2/14/18   9:30  163.04
# 1 2018-02-14 16:00:00  2/14/18  16:00  167.37
# 2 2018-02-15 09:30:00  2/15/18   9:30  169.79
# 3 2018-02-15 16:00:00  2/15/18  16:00  172.99
# high

#       DATE    HIGH
# 0  2/14/18  167.54
# 1  2/15/18  173.09
# 2  2/16/18  174.82

# Setting the index
apple_high.set_index('date_and_time', inplace=True)
apple_high

#                         date   time   price     DATE    HIGH
# date_and_time                                               
# 2018-02-14 09:30:00  2/14/18   9:30  163.04  2/14/18  167.54
# 2018-02-14 16:00:00  2/14/18  16:00  167.37  2/14/18  167.54
# 2018-02-15 09:30:00  2/15/18   9:30  169.79  2/15/18  173.09
# 2018-02-15 16:00:00  2/15/18  16:00  172.99  2/15/18  173.09

# Preparing the DataFrames
# In this exercise, you'll prepare the traffic stop and weather rating DataFrames so that they're ready to be merged:

# With the ri DataFrame, you'll move the stop_datetime index to a column since the index will be lost during the merge.
# With the weather DataFrame, you'll select the DATE and rating columns and put them in a new DataFrame.
# Reset the index of 'ri'
ri.reset_index(inplace=True)

# Examine the head of 'ri'
print(ri.head())

# Create a DataFrame from the 'DATE' and 'rating' columns
weather_rating = weather[['DATE','rating']]

# Examine the head of 'weather_rating'
print(weather_rating.head())

# The ri and weather_rating DataFrames are now ready to be merged.

# Merging the DataFrames
# In this exercise, you'll merge the ri and weather_rating DataFrames into a new DataFrame, ri_weather.

# The DataFrames will be joined using the stop_date column from ri and the DATE column from weather_rating. Thankfully the date formatting matches exactly, which is not always the case!

# Once the merge is complete, you'll set stop_datetime as the index, which is the column you saved in the previous exercise.

# Examine the shape of 'ri'
print(ri.shape)

# Merge 'ri' and 'weather_rating' using a left join
ri_weather = pd.merge(left=ri, right=weather_rating, left_on='stop_date', right_on='DATE', how='left')

# Examine the shape of 'ri_weather'
print(ri_weather.shape)

# Set 'stop_datetime' as the index of 'ri_weather'
ri_weather.set_index('stop_datetime', inplace=True)

# Does weather affect the arrest rate?

# Comparing arrest rates by weather rating
# Do police officers arrest drivers more often when the weather is bad? Find out below!

# First, you'll calculate the overall arrest rate.
# Then, you'll calculate the arrest rate for each of the weather ratings you previously assigned.
# Finally, you'll add violation type as a second factor in the analysis, to see if that accounts for any differences in the arrest rate.
# Since you previously defined a logical order for the weather categories, good < bad < worse, they will be sorted that way in the results.

# Calculate the overall arrest rate
print(ri_weather.is_arrested.mean())
# <script.py> output:
    # 0.0355690117407784

# Calculate the arrest rate for each 'rating'
print(ri_weather.groupby('rating').is_arrested.mean())

# rating
# good     0.033715
# bad      0.036261
# worse    0.041667
# Name: is_arrested, dtype: float64

# Calculate the arrest rate for each 'violation' and 'rating'
print(ri_weather.groupby(['violation','rating']).is_arrested.mean())

# violation            rating
# Equipment            good      0.059007
#                      bad       0.066311
#                      worse     0.097357
# Moving violation     good      0.056227
#                      bad       0.058050
#                      worse     0.065860
# Other                good      0.076966
#                      bad       0.087443
#                      worse     0.062893
# Registration/plates  good      0.081574
#                      bad       0.098160
#                      worse     0.115625
# Seat belt            good      0.028587
#                      bad       0.022493
#                      worse     0.000000
# Speeding             good      0.013405
#                      bad       0.013314
#                      worse     0.016886
# Name: is_arrested, dtype: float64

# The arrest rate increases as the weather gets worse, and that trend persists across many of the violation types. This doesn't prove a causal link, but it's quite an interesting result!

# Selecting from a multi-indexed Series
# The output of a single .groupby() operation on multiple columns is a Series with a MultiIndex. Working with this type of object is similar to working with a DataFrame:

# The outer index level is like the DataFrame rows.
# The inner index level is like the DataFrame columns.
# In this exercise, you'll practice accessing data from a multi-indexed Series using the .loc[] accessor.
# Save the output of the groupby operation from the last exercise
arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()

# Print the 'arrest_rate' Series
print(arrest_rate)

# Print the arrest rate for moving violations in bad weather
print(arrest_rate.loc['Moving violation', 'bad'])

# Print the arrest rates for speeding violations in all three weather conditions
print(arrest_rate.loc['Speeding'])

# Reshaping the arrest rate data
# In this exercise, you'll start by reshaping the arrest_rate Series into a DataFrame. This is a useful step when working with any multi-indexed Series, since it enables you to access the full range of DataFrame methods.

# Then, you'll create the exact same DataFrame using a pivot table. This is a great example of how pandas often gives you more than one way to reach the same result!
# Unstack the 'arrest_rate' Series into a DataFrame
print(arrest_rate.unstack())

# Create the same DataFrame using a pivot table
print(ri_weather.pivot_table(index='violation', columns='rating', values='is_arrested'))
# In the future, when you need to create a DataFrame like this, you can choose whichever method makes the most sense to you.