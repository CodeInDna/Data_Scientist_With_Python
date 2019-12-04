# Creating a multi-level index
import pandas as pd

trials = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/trials_01.csv')

print(trials)

trials = trials.set_index(['treatment', 'gender'])

print(trials)

# Pivot table won't work with the above dataframe, because of the multilevel index
# Unstacking a Multi-Index
# trials = trials.unstack(level = 'gender')
#OR
# trials = trials.unstack(level = 1)
# print(trials)

# Stacking DataFrames
trials_by_gender = trials.unstack(level = 'gender')
print(trials_by_gender)

trials_by_gender = trials_by_gender.stack(level = 'gender')
print(trials_by_gender)
#                   id  response
# treatment gender
# A         F        1         5
#           M        2         3
# B         F        3         8
#           M        4         9
# Swapping Levels
swapped = trials_by_gender.swaplevel(0, 1)
print(swapped)
#                   id  response
# gender treatment
# F      A           1         5
# M      A           2         3
# F      B           3         8
# M      B           4         9

# Sorting Rows
sorted_trials = swapped.sort_index()
print(sorted_trials)
#                   id  response
# gender treatment
# F      A           1         5
#        B           3         8
# M      A           2         3
#        B           4         9

# Stacking & unstacking I

# You are now going to practice stacking and unstacking DataFrames. The users DataFrame you have been working with in this chapter has been pre-loaded for you, this time with a MultiIndex. Explore it in the IPython Shell to see the data layout. Pay attention to the index, and notice that the index levels are ['city', 'weekday']. So 'weekday' - the second entry - has position 1. This position is what corresponds to the level parameter in .stack() and .unstack() calls. Alternatively, you can specify 'weekday' as the level instead of its position.

# Your job in this exercise is to unstack users by 'weekday'. You will then use .stack() on the unstacked DataFrame to see if you get back the original layout of users.

users = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/users.csv')

# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))

# You are now going to continue working with the users DataFrame. As always, first explore it in the IPython Shell to see the layout and note the index.

# Your job in this exercise is to unstack and then stack the 'city' level, as you did previously for 'weekday'. Note that you won't get the same DataFrame.

# Unstack users by 'city': bycity
bycity = users.unstack(level='city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))

# Restoring the index order
# Continuing from the previous exercise, you will now use .swaplevel(0, 1) to flip the index levels. Note they won't be sorted. To sort them, you will have to follow up with a .sort_index(). You will then obtain the original DataFrame. Note that an unsorted index leads to slicing failures.
# To begin, print both users and bycity in the IPython Shell. The goal here is to convert bycity back to something that looks like users.
# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0,1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))