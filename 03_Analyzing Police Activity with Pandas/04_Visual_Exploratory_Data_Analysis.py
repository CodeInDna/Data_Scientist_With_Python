# Calculating the hourly arrest rate
# When a police officer stops a driver, a small percentage of those stops ends in an arrest. This is known as the arrest rate. In this exercise, you'll find out whether the arrest rate varies by time of day.

# First, you'll calculate the arrest rate across all stops. Then, you'll calculate the hourly arrest rate by using the hour attribute of the index. The hour ranges from 0 to 23, in which:

# 0 = midnight
# 12 = noon
# 23 = 11 PM

# Calculate the overall arrest rate
print(ri.is_arrested.mean())

# Calculate the hourly arrest rate
print(ri.groupby(ri.index.hour).is_arrested.mean())

# Save the hourly arrest rate
hourly_arrest_rate = ri.groupby(ri.index.hour).is_arrested.mean()

# Next you'll plot the data so that you can visually examine the arrest rate trends.

# Plotting the hourly arrest rate
# In this exercise, you'll create a line plot from the hourly_arrest_rate object. A line plot is appropriate in this case because you're showing how a quantity changes over time.

# This plot should help you to spot some trends that may not have been obvious when examining the raw numbers!
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Create a line plot of 'hourly_arrest_rate'
hourly_arrest_rate.plot()

# Add the xlabel, ylabel, and title
plt.xlabel('Hour')
plt.ylabel('Arrest Rate')
plt.title('Arrest Rate by Time of Day')

# Display the plot
plt.show()

# The arrest rate has a significant spike overnight, and then dips in the early morning hours.

# Resampling the price
apple
#                       price    volume
# date_and_time                        
# 2018-01-08 16:00:00  174.35  20567800
# 2018-01-09 16:00:00  174.33  21584000
# 2018-02-08 16:00:00  155.15  54390500
# 2018-02-09 16:00:00  156.41  70672600
# 2018-03-08 16:00:00  176.94  23774100
# 2018-03-09 16:00:00  179.98  32185200
apple.groupby(apple.index.month).price.mean()

# date_and_time
# 1    174.34
# 2    155.78
# 3    178.46
apple.price.resample('M').mean()

# date_and_time
# 2018-01-31    174.34
# 2018-02-28    155.78
# 2018-03-31    178.46

# Plotting drug-related stops
# In a small portion of traffic stops, drugs are found in the vehicle during a search. In this exercise, you'll assess whether these drug-related stops are becoming more common over time.

# The Boolean column drugs_related_stop indicates whether drugs were found during a given stop. You'll calculate the annual drug rate by resampling this column, and then you'll use a line plot to visualize how the rate has changed over time.
# Calculate the annual rate of drug-related stops
print(ri.drugs_related_stop.resample('A').mean())

# Save the annual rate of drug-related stops
annual_drug_rate = ri.drugs_related_stop.resample('A').mean()

# Create a line plot of 'annual_drug_rate'
annual_drug_rate.plot()

# Display the plot
plt.show()

# The rate of drug-related stops nearly doubled over the course of 10 years. Why might that be the case?

# Comparing drug and search rates
# As you saw in the last exercise, the rate of drug-related stops increased significantly between 2005 and 2015. You might hypothesize that the rate of vehicle searches was also increasing, which would have led to an increase in drug-related stops even if more drivers were not carrying drugs.
# You can test this hypothesis by calculating the annual search rate, and then plotting it against the annual drug rate. If the hypothesis is true, then you'll see both rates increasing over time.
# Calculate and save the annual search rate
annual_search_rate = ri.search_conducted.resample('A').mean()

# Concatenate 'annual_drug_rate' and 'annual_search_rate'
annual = pd.concat([annual_drug_rate,annual_search_rate], axis='columns')

# Create subplots from 'annual'
annual.plot(subplots = True)

# Display the subplots
plt.show()
# Wow! The rate of drug-related stops increased even though the search rate decreased, disproving our hypothesis.

# What violations are caught in each district?


# Computing a frequency table
pd.crosstab(ri.driver_race, ri.driver_gender)

# driver_gender      F      M
# driver_race                
# Asian            551   1838
# Black           2681   9604
# Hispanic        1953   7774
# Other             53    212
# White          18536  43334
 
# Frequency table: Tally of how many times each combination of values occurs
 
ri[(ri.driver_race == 'Asian') & (ri.driver_gender == 'F')].shape
# (551, 14)
 
# driver_race is along the index, driver_gender is along the columns
 
table = pd.crosstab(ri.driver_race, ri.driver_gender)

#loc accessor: Select from a DataFrame by label
 
# table

# driver_gender      F      M
# driver_race                
# Asian            551   1838
# Black           2681   9604
# Hispanic        1953   7774
# Other             53    212
# White          18536  43334
table.loc['Asian':'Hispanic']

# driver_gender     F     M
# driver_race              
# Asian           551  1838
# Black          2681  9604
# Hispanic       1953  7774
table = table.loc['Asian':'Hispanic']

# Creating a line plot
table.plot()
plt.show()

# Creating a bar plot # Much more appropriate to display categorical data
table.plot(kind='bar')
plt.show()

# Stacking the bars
table.plot(kind='bar', stacked=True)
plt.show()

# Tallying violations by district
# The state of Rhode Island is broken into six police districts, also known as zones. How do the zones compare in terms of what violations are caught by police?

# In this exercise, you'll create a frequency table to determine how many violations of each type took place in each of the six zones. Then, you'll filter the table to focus on the "K" zones, which you'll examine further in the next exercise.

# Create a frequency table of districts and violations
print(pd.crosstab(ri.district,ri.violation))

# Save the frequency table as 'all_zones'
all_zones = pd.crosstab(ri.district,ri.violation)

# Select rows 'Zone K1' through 'Zone K3'
print(all_zones.loc['Zone K1':'Zone K3'])

# Save the smaller table as 'k_zones'
k_zones = all_zones.loc['Zone K1':'Zone K3']

# Plotting violations by district
# Now that you've created a frequency table focused on the "K" zones, you'll visualize the data to help you compare what violations are being caught in each zone.

# First you'll create a bar plot, which is an appropriate plot type since you're comparing categorical data. Then you'll create a stacked bar plot in order to get a slightly different look at the data. Which plot do you find to be more insightful?
# Create a bar plot of 'k_zones'
k_zones.plot(kind='bar', stacked=True)

# Display the plot
plt.show()

# The vast majority of traffic stops in Zone K1 are for speeding, and Zones K2 and K3 are remarkably similar to one another in terms of violations.

# How long might you be stopped for a violation
# Analyzing an object column
# apple

#                       price    volume change
# date_and_time                               
# 2018-01-08 16:00:00  174.35  20567800   down
# 2018-01-09 16:00:00  174.33  21584000   down
# 2018-02-08 16:00:00  155.15  54390500   down
# 2018-02-09 16:00:00  156.41  70672600     up
# 2018-03-08 16:00:00  176.94  23774100     up
# 2018-03-09 16:00:00  179.98  32185200     up
 
# Create a Boolean column: True if the price went up, and False otherwise
# Calculate how often the price went up by taking the column mean
 
apple.change.dtype
# dtype('O')
 
# astype() can't be used in this case

# Mapping one set of values to another
# Dictionary maps the values you have to the values you want
 
mapping = {'up':True, 'down':False}
apple['is_up'] = apple.change.map(mapping)
apple

#                       price    volume change  is_up
# date_and_time                                      
# 2018-01-08 16:00:00  174.35  20567800   down  False
# 2018-01-09 16:00:00  174.33  21584000   down  False
# 2018-02-08 16:00:00  155.15  54390500   down  False
# 2018-02-09 16:00:00  156.41  70672600     up   True
# 2018-03-08 16:00:00  176.94  23774100     up   True
# 2018-03-09 16:00:00  179.98  32185200     up   True

# Calculating the search rate
# Visualize how often searches were performed after each type of violation
 
ri.groupby('violation').search_conducted.mean()

# violation
# Equipment              0.064280
# Moving violation       0.057014
# Other                  0.045362
# Registration/plates    0.093438
# Seat belt              0.031513
# Speeding               0.021560
# Name: search_conducted, dtype: float64
 
# Returns a Series sorted in alphabetical order
 
search_rate = ri.groupby('violation').search_conducted.mean()

search_rate.sort_values().plot(kind='bar')
plt.show()

# Rotating the bars
search_rate.sort_values().plot(kind='barh')
plt.show()

# Converting stop durations to numbers
# In the traffic stops dataset, the stop_duration column tells you approximately how long the driver was detained by the officer. Unfortunately, the durations are stored as strings, such as '0-15 Min'. How can you make this data easier to analyze?

# In this exercise, you'll convert the stop durations to integers. Because the precise durations are not available, you'll have to estimate the numbers using reasonable values:

# Convert '0-15 Min' to 8
# Convert '16-30 Min' to 23
# Convert '30+ Min' to 45

# Print the unique values in 'stop_duration'
print(ri.stop_duration.unique())

# Create a dictionary that maps strings to integers
mapping = {'0-15 Min':8,'16-30 Min':23,'30+ Min':45}

# Convert the 'stop_duration' strings to integers using the 'mapping'
ri['stop_minutes'] = ri.stop_duration.map(mapping)

# Print the unique values in 'stop_minutes'
print(ri.stop_minutes.unique())

# # Plotting stop length
# If you were stopped for a particular violation, how long might you expect to be detained?

# In this exercise, you'll visualize the average length of time drivers are stopped for each type of violation. Rather than using the violation column in this exercise, you'll use violation_raw since it contains more detailed descriptions of the violations.

# Calculate the mean 'stop_minutes' for each value in 'violation_raw'
print(ri.groupby('violation_raw').stop_minutes.mean())

# Save the resulting Series as 'stop_length'
stop_length = ri.groupby('violation_raw').stop_minutes.mean()

# Sort 'stop_length' by its values and create a horizontal bar plot
stop_length.sort_values().plot(kind='barh')

# Display the plot
plt.show()