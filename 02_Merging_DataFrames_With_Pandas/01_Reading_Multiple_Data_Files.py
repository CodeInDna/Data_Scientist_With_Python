# Tools for Pandas Data Import
# pd.read_csv() for CSV files
	# dataframe = pd.read_csv(filepath)
	# dozens of optional input parameters
# Other Data Import Tools:
	# pd.read_excel()
	# pd.read_html()
	# pd.read_json()

# Loading Separate Files
import pandas as pd
dataframe0 = pd.read_csv('sales-jan-2015.csv')
dataframe1 = pd.read_csv('sales-feb-2015.csv')

# Using a Loop
filesnames = ['sales-jan-2015.csv','sales-feb-2015.csv']

dataframes = []
for f in filesnames:
	dataframes.append(pd.read_csv(f))

# Using a Comprehension
dataframes = [pd.read_csv(f) for f in filesnames]

# Using GLOB
from glob import glob
filesnames = glob('sales*.csv')
dataframes = [pd.read_csv(f) for f in filesnames]

# Reading DataFrames from multiple files
# When data is spread among several files, you usually invoke pandas' read_csv() (or a similar data import function) multiple times to load the data into several DataFrames.
# The data files for this example have been derived from a list of Olympic medals awarded between 1896 & 2008 compiled by the Guardian.
# The column labels of each DataFrame are NOC, Country, & Total where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won (bronze, silver, or gold).
# This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Pandas Cheat Sheet and keep it handy!

# Import pandas
import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())

# Reading DataFrames from multiple files in a loop
# As you saw in the video, loading data from multiple files into DataFrames is more efficient in a loop or a list comprehension.

# Notice that this approach is not restricted to working with CSV files. That is, even if your data comes in other formats, as long as pandas has a suitable data import function, you can apply a loop or comprehension to generate a list of DataFrames imported from the source files.

# Here, you'll continue working with The Guardian's Olympic medal dataset.
# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())

# Combining DataFrames from multiple data files
# In this exercise, you'll combine the three DataFrames from earlier exercises - gold, silver, & bronze - into a single DataFrame called medals. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for concatenating or merging DataFrames.

# Remember, the column labels of each DataFrame are NOC, Country, and Total, where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won.

# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

# Print the head of medals
print(medals.head())