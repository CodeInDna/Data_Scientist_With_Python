# Merging DataFrames
pd.merge(broze,gold, on=['NOC','Country'])

pd.merge(broze,gold, on=['NOC','Country'], suffixes = ['_bronze','_gold'])

# Specifying Columns to Merge
pd.merge(countries, cities, left_on ='CITY NAME', right_on='City')

# Merging on a specific column
# This exercise follows on the last one with the DataFrames revenue and managers for your company. You expect your company to grow and, eventually, to operate in cities with the same name on different states. As such, you decide that every branch should have a numerical branch identifier. Thus, you add a branch_id column to both DataFrames. Moreover, new cities have been added to both the revenue and managers DataFrames as well. pandas has been imported as pd and both DataFrames are available in your namespace.

# At present, there should be a 1-to-1 relationship between the city and branch_id fields. In that case, the result of a merge on the city columns ought to give you the same output as a merge on the branch_id columns. Do they? Can you spot an ambiguity in one of the DataFrames?
# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue,managers, on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue,managers, on='branch_id')

# Print merge_by_id
print(merge_by_id)
# Notice that when you merge on 'city', the resulting DataFrame has a peculiar result: In row 2, the city Springfield has two different branch IDs. This is because there are actually two different cities named Springfield - one in the State of Illinois, and the other in Missouri. The revenue DataFrame has the one from Illinois, and the managers DataFrame has the one from Missouri. Consequently, when you merge on 'branch_id', both of these get dropped from the merged DataFrame.

# Merging on columns with non-matching labels
# You continue working with the revenue & managers DataFrames from before. This time, someone has changed the field name 'city' to 'branch' in the managers table. Now, when you attempt to merge DataFrames, an exception is thrown:

# >>> pd.merge(revenue, managers, on='city')
# Traceback (most recent call last):
#     ... <text deleted> ...
#     pd.merge(revenue, managers, on='city')
#     ... <text deleted> ...
# KeyError: 'city'
# Given this, it will take a bit more work for you to join or merge on the city/branch name. You have to specify the left_on and right_on parameters in the call to pd.merge().

# As before, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace. They have been printed in the IPython Shell so you can examine the columns prior to merging.

# Are you able to merge better than in the last exercise? How should the rows with Springfield be handled?
# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue,managers, left_on='city', right_on='branch')

# Print combined
print(combined)

# Merging on multiple columns
# Another strategy to disambiguate cities with identical names is to add information on the states in which the cities are located. To this end, you add a column called state to both DataFrames from the preceding exercises. Again, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace.

# Your goal in this exercise is to use pd.merge() to merge DataFrames using multiple columns (using 'branch_id', 'city', and 'state' in this case).

# Are you able to match all your company's branches correctly?
# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers, on=['branch_id','city','state'])

# Print combined
print(combined)
#         city  branch_id  revenue state   manager
# 0     Austin         10      100    TX  Charlers
# 1     Denver         20       83    CO      Joel
# 2  Mendocino         47      200    CA     Brett