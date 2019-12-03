# Given a pair of label-based indices, sometimes it's necessary to find the corresponding positions. In this exercise, you will use the Pennsylvania election results again. The DataFrame is provided for you as election.
# Find x and y such that election.iloc[x, y] == election.loc['Bedford', 'winner']. That is, what is the row position of 'Bedford', and the column position of 'winner'? Remember that the first position in Python is 0, not 1!
# To answer this question, first explore the DataFrame using election.head() in the IPython Shell and inspect it with your eyes.
# This course introduces a lot of new concepts, so if you ever need a quick refresher, download the Pandas Cheat Sheet and keep it handy!
# Import pandas
import pandas as pd

filename = '../Datasets/01_Manipulating_DataFrames_with_Pandas/pennsylvania2012_turnout.csv'
# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')

# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])

# Indexing and column rearrangement
# There are circumstances in which it's useful to modify the order of your DataFrame columns. We do that now by extracting just two columns from the Pennsylvania election results DataFrame.
# Your job is to read the CSV file and set the index to 'county'. You'll then assign a new DataFrame by selecting the list of columns ['winner', 'total', 'voters']. The CSV file is provided to you in the variable filename.



# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())

# The original election DataFrame had 6 columns, but as you can see, your results DataFrame now has just the 3 columns: 'winner', 'total', and 'voters'.