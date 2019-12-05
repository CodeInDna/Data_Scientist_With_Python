import pandas as pd

auto_mpg = pd.read_csv('../Dataset/Manipulating DataFrames with Pandas/auto-mpg.csv')
print(auto_mpg.head())
splitting = auto_mpg.groupby('yr')

print(type(splitting)) # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

print(type(splitting.groups)) # <class 'dict'>

print(splitting.groups.keys()) # dict_keys([70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82])

# groupby object: iteration
for group_name, group in splitting:
	avg = group['mpg'].mean()
	print(group_name, avg)

# groupby object: iteration and filtering
for group_name, group in splitting:
	avg = group.loc[group['name'].str.contains('chevrolet'), 'mpg'].mean()
	print(group_name, avg)

# groupby object: comprehension
chevy_means = {year:group.loc[group['name'].str.contains('chevrolet'),'mpg'].mean() for year,group in splitting}

# Boolean Groupby
chevy = auto_mpg['name'].str.contains('chevrolet')
print(auto_mpg.groupby(['yr', chevy])['mpg'].mean())

# yr  name
# 70  False    17.923077
#     True     15.666667
# 71  False    21.260870
#     True     20.250000
# 72  False    19.120000
#     True     15.333333
# 73  False    17.500000
#     True     14.833333
# 74  False    23.304348
#     True     18.666667
# 75  False    20.555556
#     True     17.666667
# 76  False    21.350000
#     True     23.250000
# 77  False    23.895833
#     True     20.250000
# 78  False    24.136364
#     True     23.233333
# 79  False    25.488462
#     True     21.666667
# 80  False    34.104000
#     True     30.050000
# 81  False    30.433333
#     True     23.500000
# 82  False    32.461538
#     True     29.000000
# Name: mpg, dtype: float64

# Grouping and filtering with .apply()

# By using .apply(), you can write functions that filter rows within groups. The .apply() method will handle the iteration over individual groups and then re-combine them back into a Series or DataFrame.
# In this exercise you'll take the Titanic data set and analyze survival rates from the 'C' deck, which contained the most passengers. To do this you'll group the dataset by 'sex' and then use the .apply() method on a provided user defined function which calculates the mean survival rates on the 'C' deck:

def c_deck_survival(gr):

    c_passengers = gr['cabin'].str.startswith('C').fillna(False)

    return gr.loc[c_passengers, 'survived'].mean()
# The DataFrame has been pre-loaded as titanic.

# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')

# Call by_sex.apply with the function c_deck_survival
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)

# sex
# female    0.913043
# male      0.312500
# dtype: float64
#  It looks like female passengers on the 'C' deck had a much higher chance of surviving!

# Grouping and filtering with .filter()
# You can use groupby with the .filter() method to remove whole groups of rows from a DataFrame based on a boolean condition.

# In this exercise, you'll take the February sales data and remove entries from companies that purchased less than or equal to 35 Units in the whole month.

# First, you'll identify how many units each company bought for verification. Next you'll use the .filter() method after grouping by 'Company' to remove all rows belonging to companies whose sum over the 'Units' column was less than or equal to 35. Finally, verify that the three companies whose total Units purchased were less than or equal to 35 have been filtered out from the DataFrame.
# Read the CSV file into a DataFrame: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)

# Group sales by 'Company': by_company
by_company = sales.groupby('Company')

# Compute the sum of the 'Units' of by_company: by_com_sum
by_com_sum = by_company['Units'].sum()
print(by_com_sum)

# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
print(by_com_filt)

# Filtering and grouping with .map()

# You have seen how to group by a column, or by multiple columns. Sometimes, you may instead want to group by a function/transformation of a column. The key here is that the Series is indexed the same way as the DataFrame. You can also mix and match column grouping with Series grouping.

# In this exercise your job is to investigate survival rates of passengers on the Titanic by 'age' and 'pclass'. In particular, the goal is to find out what fraction of children under 10 survived in each 'pclass'. You'll do this by first creating a boolean array where True is passengers under 10 years old and False is passengers over 10. You'll use .map() to change these values to strings.

# Finally, you'll group by the under 10 series and the 'pclass' column and aggregate the 'survived' column. The 'survived' column has the value 1 if the passenger survived and 0 otherwise. The mean of the 'survived' column is the fraction of passengers who lived.

# The DataFrame has been pre-loaded for you as titanic.
# Create the Boolean Series: under10
under10 = (titanic['age'] < 10).map({True:'under 10', False: 'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)

# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10,'pclass'])['survived'].mean()
print(survived_mean_2)

# ! It looks like passengers under the age of 10 had a higher survival rate than those above the age of 10.