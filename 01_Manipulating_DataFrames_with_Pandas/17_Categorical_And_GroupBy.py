# Sales Data
import pandas as pd
sales = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/sales_grocery.csv')

# Boolean Filter and Count
print(sales.loc[sales['weekday'] == 'Sun'].count())

# Groupby and Count
print(sales.groupby('weekday').count())

# Split-apply-combine
# sales.groupby('weekday').count()
	# Split by 'weekday'
	# apply count() function on each group
	# combine counts per group

# Groupby and sum
print(sales.groupby('weekday')['bread'].sum())

print(sales.groupby('weekday')['bread', 'butter'].sum())

print(sales.groupby(['city','weekday']).mean())

# Customers
customers = pd.Series(['Dave', 'Alice', 'Bob', 'Alice'])

# Groupby and sum: by series
print(sales.groupby(customers)['bread'].sum())

# Categorical Data
print(sales['weekday'].unique())

sales['weekday'] = sales['weekday'].astype('category')
sales['weekday']
# Computations are faster and categorical data require less space in memory.

# Grouping by multiple columns
# In this exercise, you will return to working with the Titanic dataset from Chapter 1 and use .groupby() to analyze the distribution of passengers who boarded the Titanic.

# The 'pclass' column identifies which class of ticket was purchased by the passenger and the 'embarked' column indicates at which of the three ports the passenger boarded the Titanic. 'S' stands for Southampton, England, 'C' for Cherbourg, France and 'Q' for Queenstown, Ireland.

# Your job is to first group by the 'pclass' column and count the number of rows in each class using the 'survived' column. You will then group by the 'embarked' and 'pclass' columns and count the number of passengers.

# The DataFrame has been pre-loaded as titanic.

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked','pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)

# Grouping your data by certain columns like this and aggregating them by another column, in this case, 'survived', allows you to carefully examine your data for interesting insights.

# Grouping by another series
# In this exercise, you'll use two data sets from Gapminder.org to investigate the average life expectancy (in years) at birth in 2010 for the 6 continental regions. To do this you'll read the life expectancy data per country into one pandas DataFrame and the association between country and region into another.

# By setting the index of both DataFrames to the country name, you'll then use the region information to group the countries in the life expectancy DataFrame and compute the mean value for 2010.

# The life expectancy CSV file is available to you in the variable life_fname and the regions filename is available in the variable regions_fname.
# Read life_fname into a DataFrame: life
life = pd.read_csv(life_fname, index_col='Country')

# Read regions_fname into a DataFrame: regions
regions = pd.read_csv(regions_fname, index_col='Country')

# Group life by regions['region']: life_by_region
life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
print(life_by_region['2010'].mean())

# It looks like the average life expectancy (in years) at birth in 2010 was highest in Europe & Central Asia and lowest in Sub-Saharan Africa.

# Multiple aggregation
sales.groupby('city')[['bread','butter']].agg(['max','sum'])

# Custom Aggregation
def data_range(series):
	return series.max() - series.min()

sales.groupby('city')[['bread','butter']].agg(data_range)

# Custom Aggregation : Dictionaries
sales.groupby('city')[['bread','butter']].agg({'bread':'sum','butter':data_range})