# Using datetime format
# ri.head()

#     stop_date stop_time driver_gender driver_race
# 0  2005-01-04     12:55             M       White
# 1  2005-01-23     23:15             M       White
# 2  2005-02-17     04:15             M       White
# 3  2005-02-20     17:15             M       White
# 4  2005-02-24     01:20             F       White
# ...
# ri.dtypes

# stop_date             object
# stop_time             object
# driver_gender         object
# driver_race           object
# ...
 
# Combine stop_date and stop_time into one column
# Convert it to datetime format

# Combining object columns
# apple

#       date   time   price
# 0  2/13/18  16:00  164.34
# 1  2/14/18  16:00  167.37
# 2  2/15/18  16:00  172.99
# apple.date.str.replace('/', '-')

# 0    2-13-18
# 1    2-14-18
# 2    2-15-18
# Name: date, dtype: object
# combined = apple.date.str.cat(apple.time, sep=' ')
# combined

# 0    2/13/18 16:00
# 1    2/14/18 16:00
# 2    2/15/18 16:00
# Name: date, dtype: object

# Converting to datetime format
# apple['date_and_time'] = pd.to_datetime(combined)
# apple

#       date   time   price       date_and_time
# 0  2/13/18  16:00  164.34 2018-02-13 16:00:00
# 1  2/14/18  16:00  167.37 2018-02-14 16:00:00
# 2  2/15/18  16:00  172.99 2018-02-15 16:00:00
# apple.dtypes

# date                     object
# time                     object
# price                   float64
# date_and_time    datetime64[ns]
# dtype: object

# Setting the index
# apple.set_index('date_and_time', inplace=True)
# apple

#                         date   time   price
# date_and_time                              
# 2018-02-13 16:00:00  2/13/18  16:00  164.34
# 2018-02-14 16:00:00  2/14/18  16:00  167.37
# 2018-02-15 16:00:00  2/15/18  16:00  172.99
# apple.index

# DatetimeIndex(['2018-02-13 16:00:00', '2018-02-14 16:00:00',
#                '2018-02-15 16:00:00'],
#               dtype='datetime64[ns]', name='date_and_time', freq=None)
# apple.columns
# Index(['date', 'time', 'price'], dtype='object')

# Combining object columns
# Currently, the date and time of each traffic stop are stored in separate object columns: stop_date and stop_time.

# In this exercise, you'll combine these two columns into a single column, and then convert it to datetime format. This will enable convenient date-based attributes that we'll use later in the course.
# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Examine the data types of the DataFrame
print(ri.dtypes)

# Setting the index
# The last step that you'll take in this chapter is to set the stop_datetime column as the DataFrame's index. By replacing the default index with a DatetimeIndex, you'll make it easier to analyze the dataset by date and time, which will come in handy later in the course!
# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)