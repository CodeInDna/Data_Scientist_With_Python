# You can use lists to select specific row and column labels with the .loc[] accessor. In this exercise, your job is to select the counties ['Philadelphia', 'Centre', 'Fulton'] and the columns ['winner','Obama','Romney'] from the election DataFrame, which has been pre-loaded for you with the index set to 'county'.
import pandas as pd

filename = '../Datasets/01_Manipulating_DataFrames_with_Pandas/pennsylvania2012_turnout.csv'
# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')
# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner','Obama','Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows,cols]

# Print the three_counties DataFrame
print(three_counties)

# If you know exactly which rows and columns are of interest to you, this is a useful approach for subselecting DataFrames.