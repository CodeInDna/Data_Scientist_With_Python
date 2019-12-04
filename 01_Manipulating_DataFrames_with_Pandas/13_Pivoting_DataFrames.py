# Clinical Trials Data
import pandas as pd

trials = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/trials_01.csv')

print(trials)
#    id treatment gender  response
# 0   1         A      F         5
# 1   2         A      M         3
# 2   3         B      F         8
# 3   4         B      M         9

# Reshaping by pivoting
trials = trials.pivot(index='treatment', columns='gender', values='response')
print(trials)
# gender     F  M
# treatment
# A          5  3
# B          8  9

# Pivoting a single variable
# Suppose you started a blog for a band, and you would like to log how many visitors you have had, and how many signed-up for your newsletter. To help design the tours later, you track where the visitors are. A DataFrame called users consisting of this information has been pre-loaded for you.

# Inspect users in the IPython Shell and make a note of which variable you want to use to index the rows ('weekday'), which variable you want to use to index the columns ('city'), and which variable will populate the values in the cells ('visitors'). Try to visualize what the result should be.

# For example, in the video, Dhavide used 'treatment' to index the rows, 'gender' to index the columns, and 'response' to populate the cells. Prior to pivoting, the DataFrame looked like this:

#    id treatment gender  response
# 0   1         A      F         5
# 1   2         A      M         3
# 2   3         B      F         8
# 3   4         B      M         9
# After pivoting:

# gender     F  M
# treatment      
# A          5  3
# B          8  9
# In this exercise, your job is to pivot users so that the focus is on 'visitors', with the columns indexed by 'city' and the rows indexed by 'weekday'.

users = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/users.csv')

# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index='weekday', columns='city', values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)
# city     Austin  Dallas
# weekday
# Mon         326     456
# Sun         139     237

# Pivoting all variables
# If you do not select any particular variables, all of them will be pivoted. In this case - with the users DataFrame - both 'visitors' and 'signups' will be pivoted, creating hierarchical column labels.
# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday',columns='city',values='signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday',columns='city')

# Print the pivoted DataFrame
print(pivot)