# Merging with Left Join
# Keeps all rows of the left DF in the merged DF
# For rows in the left DF with matches in the right DF
	# Non-Joining Columns of the right DF are appended to left DF
# For rows in the left DF with no matches in the right DF
	# Non-Joining columns are filled with Nulls
# Merging with left join
pd.merge(bronze, gold, on = ['NOC', 'Country'], suffixes = ['_bronze','_gold'], how='left')

pd.merge(bronze, gold, on = ['NOC', 'Country'], suffixes = ['_bronze','_gold'], how='right')

# Using .join(how='left')
population.join(unemployment, how='left') # Default
# Using .join(how='right')
population.join(unemployment, how='right')
population.join(unemployment, how='inner')
population.join(unemployment, how='outer')

# Which Should you use?
# df1.append(df2) : Stacked Vertically
# pd.concat([df1,df2]):
	# Stacking many horizontally or vertically
	# Simple inner/outer joins on Indexes
# df1.join(df2): inner/outer/left/right joins on Indexes
# pd.merge([df1,df2]): Many Joins on Multiple Columns

#QUIZ
# Joining by Index
# The DataFrames revenue and managers are displayed in the IPython Shell. Here, they are indexed by 'branch_id'.

# Choose the function call below that will join the DataFrames on their indexes and return 5 rows with index labels [10, 20, 30, 31, 47]. Explore each of them in the IPython Shell to get a better understanding of their functionality.
                  # city state  revenue
# branch_id                            
# 10              Austin    TX      100
# 20              Denver    CO       83
# 30         Springfield    IL        4
# 47           Mendocino    CA      200
# 
#                 branch state   manager
# branch_id                             
# 10              Austin    TX  Charlers
# 20              Denver    CO      Joel
# 47           Mendocino    CA     Brett
# 31         Springfield    MO     Sally

In [1]: revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer')
Out[1]: 
#                   city state_rev  revenue       branch state_mng   manager
# branch_id                                                                 
# 10              Austin        TX    100.0       Austin        TX  Charlers
# 20              Denver        CO     83.0       Denver        CO      Joel
# 30         Springfield        IL      4.0          NaN       NaN       NaN
# 31                 NaN       NaN      NaN  Springfield        MO     Sally
# 47           Mendocino        CA    200.0    Mendocino        CA     Brett

In [2]: managers.join(revenue, lsuffix='_mgn', rsuffix='_rev', how='left')
Out[2]: 
#                 branch state_mgn   manager       city state_rev  revenue
# branch_id                                                               
# 10              Austin        TX  Charlers     Austin        TX    100.0
# 20              Denver        CO      Joel     Denver        CO     83.0
# 47           Mendocino        CA     Brett  Mendocino        CA    200.0
# 31         Springfield        MO     Sally        NaN       NaN      NaN
In [3]: pd.merge(revenue, managers, on='branch_id')
# Out[3]: 
#                 city state_x  revenue     branch state_y   manager
# branch_id                                                         
# 10            Austin      TX      100     Austin      TX  Charlers
# 20            Denver      CO       83     Denver      CO      Joel
# 47         Mendocino      CA      200  Mendocino      CA     Brett

In [4]: pd.merge(managers, revenue, how='left')
# Out[4]: 
#         branch state   manager       city  revenue
# 0       Austin    TX  Charlers     Austin    100.0
# 1       Denver    CO      Joel     Denver     83.0
# 2    Mendocino    CA     Brett  Mendocino    200.0
# 3  Springfield    MO     Sally        NaN      NaN

# Left & right merging on multiple columns
# You now have, in addition to the revenue and managers DataFrames from prior exercises, a DataFrame sales that summarizes units sold from specific branches (identified by city and state but not branch_id).

# Once again, the managers DataFrame uses the label branch in place of city as in the other two DataFrames. Your task here is to employ left and right merges to preserve data and identify where data is missing.

# By merging revenue and sales with a right merge, you can identify the missing revenue values. Here, you don't need to specify left_on or right_on because the columns to merge on have matching labels.

# By merging sales and managers with a left merge, you can identify the missing manager. Here, the columns to merge on have conflicting labels, so you must specify left_on and right_on. In both cases, you're looking to figure out how to connect the fields in rows containing Springfield.

# pandas has been imported as pd and the three DataFrames revenue, managers, and sales have been pre-loaded. They have been printed for you to explore in the IPython Shell.

# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue,sales,on=['city', 'state'], how='right')

# Print revenue_and_sales
print(revenue_and_sales)
#           city  branch_id state  revenue  units
# 0       Austin       10.0    TX    100.0      2
# 1       Denver       20.0    CO     83.0      4
# 2  Springfield       30.0    IL      4.0      1
# 3    Mendocino       47.0    CA    200.0      1
# 4  Springfield        NaN    MO      NaN      5
# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales,managers,how='left',left_on=['city', 'state'], right_on=['branch', 'state'])

# Print sales_and_managers
print(sales_and_managers)
#           city state  units       branch  branch_id   manager
# 0    Mendocino    CA      1    Mendocino       47.0     Brett
# 1       Denver    CO      4       Denver       20.0      Joel
# 2       Austin    TX      2       Austin       10.0  Charlers
# 3  Springfield    MO      5  Springfield       31.0     Sally
# 4  Springfield    IL      1          NaN        NaN       NaN

# Merging DataFrames with outer join
# This exercise picks up where the previous one left off. The DataFrames revenue, managers, and sales are pre-loaded into your namespace (and, of course, pandas is imported as pd). Moreover, the merged DataFrames revenue_and_sales and sales_and_managers have been pre-computed exactly as you did in the previous exercise.

# The merged DataFrames contain enough information to construct a DataFrame with 5 rows with all known information correctly aligned and each branch listed only once. You will try to merge the merged DataFrames on all matching keys (which computes an inner join by default). You can compare the result to an outer join and also to an outer join with restricted subset of columns as keys.
# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers,revenue_and_sales)

# Print merge_default
print(merge_default)
#         city state  units     branch  branch_id   manager  revenue
# 0  Mendocino    CA      1  Mendocino       47.0     Brett    200.0
# 1     Denver    CO      4     Denver       20.0      Joel     83.0
# 2     Austin    TX      2     Austin       10.0  Charlers    100.0
# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers,revenue_and_sales,how='outer')

# Print merge_outer
print(merge_outer)
#           city state  units       branch  branch_id   manager  revenue
# 0    Mendocino    CA      1    Mendocino       47.0     Brett    200.0
# 1       Denver    CO      4       Denver       20.0      Joel     83.0
# 2       Austin    TX      2       Austin       10.0  Charlers    100.0
# 3  Springfield    MO      5  Springfield       31.0     Sally      NaN
# 4  Springfield    IL      1          NaN        NaN       NaN      NaN
# 5  Springfield    IL      1          NaN       30.0       NaN      4.0
# 6  Springfield    MO      5          NaN        NaN       NaN      NaN
# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers,revenue_and_sales, on=['city','state'], how='outer')

# Print merge_outer_on
print(merge_outer_on)
#           city state  units_x       branch  branch_id_x   manager  branch_id_y  revenue  units_y
# 0    Mendocino    CA        1    Mendocino         47.0     Brett         47.0    200.0        1
# 1       Denver    CO        4       Denver         20.0      Joel         20.0     83.0        4
# 2       Austin    TX        2       Austin         10.0  Charlers         10.0    100.0        2
# 3  Springfield    MO        5  Springfield         31.0     Sally          NaN      NaN        5
# 4  Springfield    IL        1          NaN          NaN       NaN         30.0      4.0        1

# Notice how the default merge drops the Springfield rows, while the default outer merge includes them twice.

# Using merge_ordered()
# This exercise uses pre-loaded DataFrames austin and houston that contain weather data from the cities Austin and Houston respectively. They have been printed in the IPython Shell for you to examine.

# Weather conditions were recorded on separate days and you need to merge these two DataFrames together such that the dates are ordered. To do this, you'll use pd.merge_ordered(). After you're done, note the order of the rows before and after merging.
# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin,houston)

# Print tx_weather
print(tx_weather)
#         date ratings
# 0 2016-01-01  Cloudy
# 1 2016-01-04   Rainy
# 2 2016-01-17   Sunny
# 3 2016-02-08  Cloudy
# 4 2016-03-01   Sunny

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin,houston,on='date',suffixes=['_aus','_hus'])

# Print tx_weather_suff
print(tx_weather_suff)

#         date ratings_aus ratings_hus
# 0 2016-01-01      Cloudy      Cloudy
# 1 2016-01-04         NaN       Rainy
# 2 2016-01-17       Sunny         NaN
# 3 2016-02-08      Cloudy         NaN
# 4 2016-03-01         NaN       Sunny

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin,houston,on='date',suffixes=['_aus','_hus'],fill_method='ffill')

# Print tx_weather_ffill
print(tx_weather_ffill)

#        date ratings_aus ratings_hus
# 0 2016-01-01      Cloudy      Cloudy
# 1 2016-01-04      Cloudy       Rainy
# 2 2016-01-17       Sunny       Rainy
# 3 2016-02-08      Cloudy       Rainy
# 4 2016-03-01      Cloudy       Sunny

# Using merge_asof()
# Similar to pd.merge_ordered(), the pd.merge_asof() function will also merge values in order using the on column, but for each row in the left DataFrame, only rows from the right DataFrame whose 'on' column values are less than the left value will be kept.

# This function can be used to align disparate datetime frequencies without having to first resample.

# Here, you'll merge monthly oil prices (US dollars) into a full automobile fuel efficiency dataset. The oil and automobile DataFrames have been pre-loaded as oil and auto. The first 5 rows of each have been printed in the IPython Shell for you to explore.

# These datasets will align such that the first price of the year will be broadcast into the rows of the automobiles DataFrame. This is considered correct since by the start of any given year, most automobiles for that year will have already been manufactured.

# You'll then inspect the merged DataFrame, resample by year and compute the mean 'Price' and 'mpg'. You should be able to see a trend in these two columns, that you can confirm by computing the Pearson correlation between resampled 'Price' and 'mpg'.

# Merge auto and oil: merged
merged = pd.merge_asof(auto,oil,left_on='yr',right_on='Date')

# Print the tail of merged
print(merged.tail())
#       mpg  cyl  displ  hp  weight  ...         yr  origin             name       Date  Price
# 387  27.0    4  140.0  86    2790  ... 1982-01-01      US  ford mustang gl 1982-01-01  33.85
# 388  44.0    4   97.0  52    2130  ... 1982-01-01  Europe        vw pickup 1982-01-01  33.85
# 389  32.0    4  135.0  84    2295  ... 1982-01-01      US    dodge rampage 1982-01-01  33.85
# 390  28.0    4  120.0  79    2625  ... 1982-01-01      US      ford ranger 1982-01-01  33.85
# 391  31.0    4  119.0  82    2720  ... 1982-01-01      US       chevy s-10 1982-01-01  33.85

# [5 rows x 11 columns]
# Resample merged: yearly
yearly = merged.resample('A', on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)
#                   mpg  Price
# Date                        
# 1970-12-31  17.689655   3.35
# 1971-12-31  21.111111   3.56
# 1972-12-31  18.714286   3.56
# 1973-12-31  17.100000   3.56
# 1974-12-31  22.769231  10.11
# 1975-12-31  20.266667  11.16
# 1976-12-31  21.573529  11.16
# 1977-12-31  23.375000  13.90
# 1978-12-31  24.061111  14.85
# 1979-12-31  25.093103  14.85
# 1980-12-31  33.803704  32.50
# 1981-12-31  30.185714  38.00
# 1982-12-31  32.000000  33.85

# print yearly.corr()
print(yearly.corr())
#             mpg     Price
# mpg    1.000000  0.948677
# Price  0.948677  1.000000

# It looks like there is a strong correlation between miles per gallon and the price of oil!