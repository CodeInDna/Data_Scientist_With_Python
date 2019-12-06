# Loading Olympic edition DataFrame
# In this chapter, you'll be using The Guardian's Olympic medal dataset.

# Your first task here is to prepare a DataFrame editions from a tab-separated values (TSV) file.

# Initially, editions has 26 rows (one for each Olympic edition, i.e., a year in which the Olympics was held) and 7 columns: 'Edition', 'Bronze', 'Gold', 'Silver', 'Grand Total', 'City', and 'Country'.

# For the analysis that follows, you won't need the overall medal counts, so you want to keep only the useful columns from editions: 'Edition', 'Grand Total', City, and Country.
#Import pandas
import pandas as pd

# Create file path: file_path
file_path = '../Dataset/Merging DataFrames with Pandas/Summer Olympic medals/Summer Olympic medals/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv(file_path, sep='\t')

# Extract the relevant columns: editions
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Print editions DataFrame
print(editions)
#     Edition  Grand Total         City                     Country
# 0      1896          151       Athens                      Greece
# 1      1900          512        Paris                      France
# 2      1904          470    St. Louis               United States
# 3      1908          804       London              United Kingdom
# 4      1912          885    Stockholm                      Sweden
# 5      1920         1298      Antwerp                     Belgium
# 6      1924          884        Paris                      France
# 7      1928          710    Amsterdam                 Netherlands
# 8      1932          615  Los Angeles               United States
# 9      1936          875       Berlin                     Germany
# 10     1948          814       London              United Kingdom
# 11     1952          889     Helsinki                     Finland
# 12     1956          885    Melbourne                   Australia
# 13     1960          882         Rome                       Italy
# 14     1964         1010        Tokyo                       Japan
# 15     1968         1031  Mexico City                      Mexico
# 16     1972         1185       Munich  West Germany (now Germany)
# 17     1976         1305     Montreal                      Canada
# 18     1980         1387       Moscow       U.S.S.R. (now Russia)
# 19     1984         1459  Los Angeles               United States
# 20     1988         1546        Seoul                 South Korea
# 21     1992         1705    Barcelona                       Spain
# 22     1996         1859      Atlanta               United States
# 23     2000         2015       Sydney                   Australia
# 24     2004         1998       Athens                      Greece
# 25     2008         2042      Beijing                       China

# Loading IOC codes DataFrame
# Your task here is to prepare a DataFrame ioc_codes from a comma-separated values (CSV) file.

# Initially, ioc_codes has 200 rows (one for each country) and 3 columns: 'Country', 'NOC', & 'ISO code'.

# For the analysis that follows, you want to keep only the useful columns from ioc_codes: 'Country' and 'NOC' (the column 'NOC' contains three-letter codes representing each country).

# Import pandas
import pandas as pd

# Create the file path: file_path
file_path = '../Dataset/Merging DataFrames with Pandas/Summer Olympic medals/Summer Olympic medals/Summer Olympic medalists 1896 to 2008 - IOC COUNTRY CODES.csv'

# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv(file_path)

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country','NOC']]

# Print first and last 5 rows of ioc_codes
print(ioc_codes.head())
print(ioc_codes.tail())

# Building medals DataFrame
# Here, you'll start with the DataFrame editions from the previous exercise.

# You have a sequence of files summer_1896.csv, summer_1900.csv, ..., summer_2008.csv, one for each Olympic edition (year).

# You will build up a dictionary medals_dict with the Olympic editions (years) as keys and DataFrames as values.

# The dictionary is built up inside a loop over the year of each Olympic edition (from the Index of editions).

# Once the dictionary of DataFrames is built up, you will combine the DataFrames using pd.concat().

# Import pandas
import pandas as pd

# Create empty dictionary: medals_dict
medals_dict = {}

for year in editions['Edition']:

    # Create the file path: file_path
    file_path = 'summer_{:d}.csv'.format(year)
    
    # Load file_path into a DataFrame: medals_dict[year]
    medals_dict[year] = pd.read_csv(file_path)
    
    # Extract relevant columns: medals_dict[year]
    medals_dict[year] = medals_dict[year][['Athlete','NOC','Medal']]
    
    # Assign year to column 'Edition' of medals_dict
    medals_dict[year]['Edition'] = year
    
# Concatenate medals_dict: medals
medals = pd.concat(medals_dict, ignore_index=True)

# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())

# Counting medals by country/edition in a pivot table
# Here, you'll start with the concatenated DataFrame medals from the previous exercise.

# You can construct a pivot table to see the number of medals each country won in each year. The result is a new DataFrame with the Olympic edition on the Index and with 138 country NOC codes as columns. If you want a refresher on pivot tables, it may be useful to refer back to the relevant exercises in Manipulating DataFrames with pandas.
# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index='Edition', columns='NOC', values='Athlete', aggfunc='count')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())

# <script.py> output:
#     NOC      AFG  AHO  ALG   ANZ  ARG  ...  VIE  YUG  ZAM  ZIM   ZZX
#     Edition                            ...                          
#     1896     NaN  NaN  NaN   NaN  NaN  ...  NaN  NaN  NaN  NaN   6.0
#     1900     NaN  NaN  NaN   NaN  NaN  ...  NaN  NaN  NaN  NaN  34.0
#     1904     NaN  NaN  NaN   NaN  NaN  ...  NaN  NaN  NaN  NaN   8.0
#     1908     NaN  NaN  NaN  19.0  NaN  ...  NaN  NaN  NaN  NaN   NaN
#     1912     NaN  NaN  NaN  10.0  NaN  ...  NaN  NaN  NaN  NaN   NaN
    
#     [5 rows x 138 columns]
#     NOC      AFG  AHO  ALG  ANZ   ARG  ...  VIE   YUG  ZAM  ZIM  ZZX
#     Edition                            ...                          
#     1992     NaN  NaN  2.0  NaN   2.0  ...  NaN   NaN  NaN  NaN  NaN
#     1996     NaN  NaN  3.0  NaN  20.0  ...  NaN  26.0  1.0  NaN  NaN
#     2000     NaN  NaN  5.0  NaN  20.0  ...  1.0  26.0  NaN  NaN  NaN
#     2004     NaN  NaN  NaN  NaN  47.0  ...  NaN   NaN  NaN  3.0  NaN
#     2008     1.0  NaN  2.0  NaN  51.0  ...  1.0   NaN  NaN  4.0  NaN
    
#     [5 rows x 138 columns]
#  As you can see, the pivot table DataFrame has mostly NaN entries (because most countries do not win any medals in a given Olympic edition).

# Computing fraction of medals per Olympic edition
# In this exercise, you'll start with the DataFrames editions, medals, & medal_counts from prior exercises.

# You can extract a Series with the total number of medals awarded in each Olympic edition.

# The DataFrame medal_counts can be divided row-wise by the total number of medals awarded each edition; the method .divide() performs the broadcast as you require.

# This gives you a normalized indication of each country's performance in each edition.

# Set Index of editions: totals
totals = editions.set_index('Edition')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']

# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals, axis='rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())

# <script.py> output:
#     NOC      AFG  AHO  ALG       ANZ  ARG  ...  VIE  YUG  ZAM  ZIM       ZZX
#     Edition                                ...                              
#     1896     NaN  NaN  NaN       NaN  NaN  ...  NaN  NaN  NaN  NaN  0.039735
#     1900     NaN  NaN  NaN       NaN  NaN  ...  NaN  NaN  NaN  NaN  0.066406
#     1904     NaN  NaN  NaN       NaN  NaN  ...  NaN  NaN  NaN  NaN  0.017021
#     1908     NaN  NaN  NaN  0.023632  NaN  ...  NaN  NaN  NaN  NaN       NaN
#     1912     NaN  NaN  NaN  0.011299  NaN  ...  NaN  NaN  NaN  NaN       NaN
    
#     [5 rows x 138 columns]
#     NOC          AFG  AHO       ALG  ANZ       ARG  ...       VIE       YUG       ZAM       ZIM  ZZX
#     Edition                                         ...                                             
#     1992         NaN  NaN  0.001173  NaN  0.001173  ...       NaN       NaN       NaN       NaN  NaN
#     1996         NaN  NaN  0.001614  NaN  0.010758  ...       NaN  0.013986  0.000538       NaN  NaN
#     2000         NaN  NaN  0.002481  NaN  0.009926  ...  0.000496  0.012903       NaN       NaN  NaN
#     2004         NaN  NaN       NaN  NaN  0.023524  ...       NaN       NaN       NaN  0.001502  NaN
#     2008     0.00049  NaN  0.000979  NaN  0.024976  ...  0.000490       NaN       NaN  0.001959  NaN
    
#     [5 rows x 138 columns]

# Computing percentage change in fraction of medals won
# Here, you'll start with the DataFrames editions, medals, medal_counts, & fractions from prior exercises.

# To see if there is a host country advantage, you first want to see how the fraction of medals won changes from edition to edition.

# The expanding mean provides a way to see this down each column. It is the value of the mean with all the data available up to that point in time. If you are interested in learning more about pandas' expanding transformations, this section of the pandas documentation has additional information.
# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change() * 100

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())
# NOC  Edition  AFG  AHO  ALG        ANZ  ...  VIE  YUG  ZAM  ZIM        ZZX
# 0       1896  NaN  NaN  NaN        NaN  ...  NaN  NaN  NaN  NaN        NaN
# 1       1900  NaN  NaN  NaN        NaN  ...  NaN  NaN  NaN  NaN  33.561198
# 2       1904  NaN  NaN  NaN        NaN  ...  NaN  NaN  NaN  NaN -22.642384
# 3       1908  NaN  NaN  NaN        NaN  ...  NaN  NaN  NaN  NaN   0.000000
# 4       1912  NaN  NaN  NaN -26.092774  ...  NaN  NaN  NaN  NaN   0.000000

# [5 rows x 139 columns]
# NOC  Edition  AFG  AHO        ALG  ANZ  ...       VIE       YUG        ZAM        ZIM  ZZX
# 21      1992  NaN  0.0  -7.214076  0.0  ...       NaN  0.000000   0.000000   0.000000  0.0
# 22      1996  NaN  0.0   8.959211  0.0  ...       NaN -2.667732 -10.758472   0.000000  0.0
# 23      2000  NaN  0.0  19.762488  0.0  ...       NaN -2.696445   0.000000   0.000000  0.0
# 24      2004  NaN  0.0   0.000000  0.0  ...  0.000000  0.000000   0.000000 -43.491929  0.0
# 25      2008  NaN  0.0  -8.197807  0.0  ... -0.661117  0.000000   0.000000 -23.316533  0.0

# Building hosts DataFrame
# Your task here is to prepare a DataFrame hosts by left joining editions and ioc_codes.

# Once created, you will subset the Edition and NOC columns and set Edition as the Index.

# There are some missing NOC values; you will set those explicitly.

# Finally, you'll reset the Index & print the final DataFrame.

# Import pandas
import pandas as pd

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions,ioc_codes, how='left')

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition','NOC']].set_index('Edition')

# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)

# Reshaping for analysis
# This exercise starts off with fractions_change and hosts already loaded.

# Your task here is to reshape the fractions_change DataFrame for later analysis.

# Initially, fractions_change is a wide DataFrame of 26 rows (one for each Olympic edition) and 139 columns (one for the edition and 138 for the competing countries).

# On reshaping with pd.melt(), as you will see, the result is a tall DataFrame with 3588 rows and 3 columns that summarizes the fractional change in the expanding mean of the percentage of medals won for each country in blocks.

# Import pandas
import pandas as pd

# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)

# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped.loc[reshaped.NOC == 'CHN']

# Print last 5 rows of chn with .tail()
print(chn.tail())

#     Edition  NOC     Change
# 567     1992  CHN   4.240630
# 568     1996  CHN   7.860247
# 569     2000  CHN  -3.851278
# 570     2004  CHN   0.128863
# 571     2008  CHN  13.251332

 # On looking at the hosting countries from the last 5 Olympic editions and the fractional change of medals won by China the last 5 editions, you can see that China fared significantly better in 2008 (i.e., when China was the host country).

#  Merging to compute influence
# This exercise starts off with the DataFrames reshaped and hosts in the namespace.

# Your task is to merge the two DataFrames and tidy the result.

# The end result is a DataFrame summarizing the fractional change in the expanding mean of the percentage of medals won for the host country in each Olympic edition.
# Import pandas
import pandas as pd

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped,hosts,how='inner')

# Print first 5 rows of merged
print(merged.head())

# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head())

# <script.py> output:
#    Edition  NOC     Change
# 0     1956  AUS  54.615063
# 1     2000  AUS  12.554986
# 2     1920  BEL  54.757887
# 3     1976  CAN  -2.143977
# 4     2008  CHN  13.251332
#          NOC      Change
# Edition                 
# 1896     GRE         NaN
# 1900     FRA  198.002486
# 1904     USA  199.651245
# 1908     GBR  134.489218
# 1912     SWE   71.896226

# Plotting influence of host country
# This final exercise starts off with the DataFrames influence and editions in the namespace. Your job is to plot the influence of being a host country.
# Import pyplot
import matplotlib.pyplot as plt

# Extract influence['Change']: change
change = influence['Change']

# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()