# Using .value_counts() for ranking
# For this exercise, you will use the pandas Series method .value_counts() to determine the top 15 countries ranked by total number of medals.

# Notice that .value_counts() sorts by values by default. The result is returned as a Series of counts indexed by unique entries from the original Series with values (counts) ranked in descending order.

# The DataFrame has been pre-loaded for you as medals.

# Select the 'NOC' column of medals: country_names
country_names = medals['NOC']

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))

# OR

# print(sorted(medals.groupby('NOC')['Medal'].count(),reverse=True)[:15])

# It looks like the top 5 countries here are USA, URS, GBR, FRA, and ITA.

# Using .pivot_table() to count medals by type
# Rather than ranking countries by total medals won and showing that list, you may want to see a bit more detail. You can use a pivot table to compute how many separate bronze, silver and gold medals each country won. That pivot table can then be used to repeat the previous computation to rank by total medals won.

# In this exercise, you will use .pivot_table() first to aggregate the total medals by type. Then, you can use .sum() along the columns of the pivot table to produce a new column. When the modified pivot table is sorted by the total medals column, you can display the results from the last exercise with a bit more detail.

# Construct the pivot table: counted
counted = medals.pivot_table(index='NOC', columns='Medal', values = 'Athlete', aggfunc='count')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')

# Sort counted by the 'totals' column
counted = counted.sort_values(by='totals',ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))

# Medal  Bronze    Gold  Silver  totals
# NOC                                  
# USA    1052.0  2088.0  1195.0  4335.0
# URS     584.0   838.0   627.0  2049.0
# GBR     505.0   498.0   591.0  1594.0
# FRA     475.0   378.0   461.0  1314.0
# ITA     374.0   460.0   394.0  1228.0
# GER     454.0   407.0   350.0  1211.0
# AUS     413.0   293.0   369.0  1075.0
# HUN     345.0   400.0   308.0  1053.0
# SWE     325.0   347.0   349.0  1021.0
# GDR     225.0   329.0   271.0   825.0
# NED     320.0   212.0   250.0   782.0
# JPN     270.0   206.0   228.0   704.0
# CHN     193.0   234.0   252.0   679.0
# RUS     240.0   192.0   206.0   638.0
# ROU     282.0   155.0   187.0   624.0

# Applying .drop_duplicates()
# What could be the difference between the 'Event_gender' and 'Gender' columns? You should be able to evaluate your guess by looking at the unique values of the pairs (Event_gender, Gender) in the data. In particular, you should not see something like (Event_gender='M', Gender='Women'). However, you will see that, strangely enough, there is an observation with (Event_gender='W', Gender='Men').

# The duplicates can be dropped using the .drop_duplicates() method, leaving behind the unique observations. The DataFrame has been loaded as medals.

# Select columns: ev_gen
ev_gen = medals[['Event_gender','Gender']]

# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)

#       Event_gender Gender
# 0                M    Men
# 348              X    Men
# 416              W  Women
# 639              X  Women
# 23675            W    Men

# Finding possible errors with .groupby()
# You will now use .groupby() to continue your exploration. Your job is to group by 'Event_gender' and 'Gender' and count the rows.

# You will see that there is only one suspicious row: This is likely a data error.

# The DataFrame is available to you as medals.

# Group medals by the two columns: medals_by_gender
medals_by_gender = medals.groupby(['Event_gender','Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medal_count_by_gender = medals_by_gender.count()

# Print medal_count_by_gender
print(medal_count_by_gender)

#                       City  Edition  Sport  Discipline  Athlete    NOC  Event  Medal
# Event_gender Gender                                                                 
# M            Men     20067    20067  20067       20067    20067  20067  20067  20067
# W            Men         1        1      1           1        1      1      1      1
#              Women    7277     7277   7277        7277     7277   7277   7277   7277
# X            Men      1653     1653   1653        1653     1653   1653   1653   1653
#              Women     218      218    218         218      218    218    218    218

# You're close to identifying the suspicious data point.

# Locating suspicious data
# You will now inspect the suspect record by locating the offending row.

# You will see that, according to the data, Joyce Chepchumba was a man that won a medal in a women's event. That is a data error as you can confirm with a web search.
# Create the Boolean Series: sus
sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')

# Create a DataFrame with the suspicious row: suspect
suspect = medals[sus]

# Print suspect
print(suspect)

# TWO NEW DATAFRAME METHODS
#idxmax(): Row or column label where maximum value is located
#idxmin(): Row or column label where minimum value is located

# Using .nunique() to rank by distinct sports
# You may want to know which countries won medals in the most distinct sports. The .nunique() method is the principal aggregation here. Given a categorical Series S, S.nunique() returns the number of distinct categories.

# Group medals by 'NOC': country_grouped
country_grouped = medals.groupby('NOC')

# Compute the number of distinct sports in which each country won medals: Nsports
Nsports = country_grouped['Sport'].nunique()

# Sort the values of Nsports in descending order
Nsports = Nsports.sort_values(ascending=False)

# Print the top 15 rows of Nsports
print(Nsports.head(15))

# Interestingly, the USSR is not in the top 5 in this category, while the USA continues to remain on top. What could be the cause of this? You'll compare the medal counts of USA vs. USSR more closely in the next two exercises to find out!


# Counting USA vs. USSR Cold War Olympic Sports
# The Olympic competitions between 1952 and 1988 took place during the height of the Cold War between the United States of America (USA) & the Union of Soviet Socialist Republics (USSR). Your goal in this exercise is to aggregate the number of distinct sports in which the USA and the USSR won medals during the Cold War years.

# The construction is mostly the same as in the preceding exercise. There is an additional filtering stage beforehand in which you reduce the original DataFrame medals by extracting data from the Cold War period that applies only to the US or to the USSR. The relevant country codes in the DataFrame, which has been pre-loaded as medals, are 'USA' & 'URS'.

# Create a Boolean Series that is True when 'Edition' is between 1952 and 1988: during_cold_war
during_cold_war = (medals.Edition >= 1952) & (medals.Edition <= 1988)

# Extract rows for which 'NOC' is either 'USA' or 'URS': is_usa_urs
is_usa_urs = medals.NOC.isin(['USA','URS'])

# Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
cold_war_medals = medals.loc[during_cold_war & is_usa_urs]

# Group cold_war_medals by 'NOC'
country_grouped = cold_war_medals.groupby('NOC')

# Create Nsports
Nsports = country_grouped['Sport'].nunique().sort_values(ascending=False)

# Print Nsports
print(Nsports)
# <script.py> output:
# NOC
# URS    21
# USA    20
# Name: Sport, dtype: int64
# As you can see, the USSR is actually higher than the US when you look only at the Olympic competitions between 1952 and 1988!

# Counting USA vs. USSR Cold War Olympic Medals
# For this exercise, you want to see which country, the USA or the USSR, won the most medals consistently over the Cold War period.

# There are several steps involved in carrying out this computation.

# You'll need a pivot table with years ('Edition') on the index and countries ('NOC') on the columns. The entries will be the total number of medals each country won that year. If the country won no medals in a given edition, expect a NaN in that entry of the pivot table.
# You'll need to slice the Cold War period and subset the 'USA' and 'URS' columns.
# You'll need to make a Series from this slice of the pivot table that tells which country won the most medals in that edition using .idxmax(axis='columns'). If .max() returns the maximum value of Series or 1D array, .idxmax() returns the index of the maximizing element. The argument axis=columns or axis=1 is required because, by default, this aggregation would be done along columns for a DataFrame.
# The final Series contains either 'USA' or 'URS' according to which country won the most medals in each Olympic edition. You can use .value_counts() to count the number of occurrences of each.

# Create the pivot table: medals_won_by_country
medals_won_by_country = medals.pivot_table(index='Edition',columns='NOC',values='Athlete', aggfunc='count')

# Slice medals_won_by_country: cold_war_usa_urs_medals
cold_war_usa_urs_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]

# Create most_medals 
most_medals = cold_war_usa_urs_medals.idxmax(axis=1)

# Print most_medals.value_counts()
print(most_medals.value_counts())

# URS    8
# USA    2
# dtype: int64

# Here, once again, the USSR comes out on top.

# Grouping the data
france = medals.NOC == 'FRA' # Boolean Series for France
france_grps = medals[france].groupby(['Edition','Medal'])
france_grps['Athlete'].count().head(10)

# Reshaping the data
france_medals = france_grps['Athlete'].count().unstack()

# Visualizing USA Medal Counts by Edition: Line Plot
# Your job in this exercise is to visualize the medal counts by 'Edition' for the USA. The DataFrame has been pre-loaded for you as medals.
# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
plt.show()

# It's difficult to gain too much insight from this visualization, however. An area plot, which you'll construct in the next exercise, may be more helpful.

# Visualizing USA Medal Counts by Edition: Area Plot
# As in the previous exercise, your job in this exercise is to visualize the medal counts by 'Edition' for the USA. This time, you will use an area plot to see the breakdown better. The usa DataFrame has been created and all reshaping from the previous exercise has been done. You need to write the plotting command.
# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by 'Edition', 'Medal', and 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Create an area plot of usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()

# Visualizing USA Medal Counts by Edition: Area Plot with Ordered Medals
# You may have noticed that the medals are ordered according to a lexicographic (dictionary) ordering: Bronze < Gold < Silver. However, you would prefer an ordering consistent with the Olympic rules: Bronze < Silver < Gold.

# You can achieve this using Categorical types. In this final exercise, after redefining the 'Medal' column of the DataFrame medals, you will repeat the area plot from the previous exercise to see the new ordering.
# Redefine 'Medal' as an ordered categorical
medals.Medal = pd.Categorical(values=medals.Medal, categories = ['Bronze','Silver','Gold'], ordered=True)

# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by 'Edition', 'Medal', and 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Create an area plot of usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()