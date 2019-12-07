# Do the genders commit different violations?
# Counting unique values
# value_counts(): Counts the unique values in a Series
# Best suited for categorical data
 
ri.stop_outcome.value_counts()

# Citation            77091
# Warning              5136
# Arrest Driver        2735
# No Action             624
# N/D                   607
# Arrest Passenger      343
# Name: stop_outcome, dtype: int64
ri.stop_outcome.value_counts().sum()
# 86536
ri.shape
# (86536, 13)
# Expressing counts as proportions
ri.stop_outcome.value_counts()

# Citation            77091
# Warning              5136
# Arrest Driver        2735
# No Action             624
# N/D                   607
# Arrest Passenger      343
# Name: stop_outcome, dtype: int64
# 77091/86536
# 0.8908546731995932
ri.stop_outcome.value_counts(normalize=True)

# Citation            0.890855
# Warning             0.059351
# Arrest Driver       0.031605
# No Action           0.007211
# N/D                 0.007014
# Arrest Passenger    0.003964
# Name: stop_outcome, dtype: float64

# Filtering DataFrame rows
ri.driver_race.value_counts()

# White       61870
# Black       12285
# Hispanic     9727
# Asian        2389
# Other         265
# Name: driver_race, dtype: int64
white = ri[ri.driver_race == 'White']
white.shape
(61870, 13)

# Comparing stop outcomes for two groups
white.stop_outcome.value_counts(normalize=True)

# Citation            0.902263
# Warning             0.057508
# Arrest Driver       0.024018
# No Action           0.007031
# N/D                 0.006433
# Arrest Passenger    0.002748
# Name: stop_outcome, dtype: float64

asian = ri[ri.driver_race == 'Asian']
asian.stop_outcome.value_counts(normalize=True)

# Citation            0.922980
# Warning             0.045207
# Arrest Driver       0.017581
# No Action           0.008372
# N/D                 0.004186
# Arrest Passenger    0.001674
# Name: stop_outcome, dtype: float64

# Examining traffic violations
# Before comparing the violations being committed by each gender, you should examine the violations committed by all drivers to get a baseline understanding of the data.

# In this exercise, you'll count the unique values in the violation column, and then separately express those counts as proportions.
# Count the unique values in 'violation'
print(ri.violation.value_counts())

# Express the counts as proportions
print(ri.violation.value_counts(normalize=True))

# <script.py> output:
#     Speeding               48423
#     Moving violation       16224
#     Equipment              10921
#     Other                   4409
#     Registration/plates     3703
#     Seat belt               2856
#     Name: violation, dtype: int64

#     Speeding               0.559571
#     Moving violation       0.187483
#     Equipment              0.126202
#     Other                  0.050950
#     Registration/plates    0.042791
#     Seat belt              0.033004
#     Name: violation, dtype: float64

# More than half of all violations are for speeding, followed by other moving violations and equipment violations.

# Comparing violations by gender
# The question we're trying to answer is whether male and female drivers tend to commit different types of traffic violations.
# In this exercise, you'll first create a DataFrame for each gender, and then analyze the violations in each DataFrame separately.
# Create a DataFrame of female drivers
female = ri[ri.driver_gender == 'F']

# Create a DataFrame of male drivers
male = ri[ri.driver_gender == 'M']

# Compute the violations by female drivers (as proportions)
print(female.violation.value_counts(normalize = True))

# Compute the violations by male drivers (as proportions)
print(male.violation.value_counts(normalize = True))

# About two-thirds of female traffic stops are for speeding, whereas stops of males are more balanced among the six categories. This doesn't mean that females speed more often than males, however, since we didn't take into account the number of stops or drivers.

# Rules for Filtering
print(female = ri[ri.driver_gender == 'F'])
print(female.shape)
# (23774, 13)
print(female_and_arrested = ri[(ri.driver_gender == 'F') &
                         (ri.is_arrested == True)])
# Each condition is surrounded by parentheses
# Ampersand (&) represents the and operator
 
print(female_and_arrested.shape)
# (669, 13)
 
# Only includes female drivers who were arrested

# Rules for filtering by multiple conditions
# Ampersand (&): only include rows that satisfy both conditions

# Pipe (|): include rows that satisfy either condition

# Each condition must be surrounded by parentheses

# Conditions can check for equality (==), inequality (!=), etc.

# Comparing speeding outcomes by gender
# When a driver is pulled over for speeding, many people believe that gender has an impact on whether the driver will receive a ticket or a warning. Can you find evidence of this in the dataset?

# First, you'll create two DataFrames of drivers who were stopped for speeding: one containing females and the other containing males.

# Then, for each gender, you'll use the stop_outcome column to calculate what percentage of stops resulted in a "Citation" (meaning a ticket) versus a "Warning".

# Create a DataFrame of female drivers stopped for speeding
female_and_speeding = ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]

# Create a DataFrame of male drivers stopped for speeding
male_and_speeding = ri[(ri.driver_gender == 'M') & (ri.violation == 'Speeding')]

# Compute the stop outcomes for female drivers (as proportions)
print(female_and_speeding.stop_outcome.value_counts(normalize = True))

# Compute the stop outcomes for male drivers (as proportions)
print(male_and_speeding.stop_outcome.value_counts(normalize = True))

# The numbers are similar for males and females: about 95% of stops for speeding result in a ticket. Thus, the data fails to show that gender has an impact on who gets a ticket for speeding.

# Comparing groups using groupby
# Study the arrest rate by police district
 
ri.district.unique()

# array(['Zone X4', 'Zone K3', 'Zone X1', 'Zone X3', 'Zone K1', 'Zone K2'],
#       dtype=object)
ri[ri.district == 'Zone K1'].is_arrested.mean()
# 0.024349083895853423
ri[ri.district == 'Zone K2'].is_arrested.mean()
# 0.030800588834786546
ri.groupby('district').is_arrested.mean()

# district
# Zone K1    0.024349
# Zone K2    0.030801
# Zone K3    0.032311
# Zone X1    0.023494
# Zone X3    0.034871
# Zone X4    0.048038
# Name: is_arrested, dtype: float64

# Grouping by multiple categories
ri.groupby(['district', 'driver_gender']).is_arrested.mean()

# district  driver_gender
# Zone K1   F                0.019169
#           M                0.026588
# Zone K2   F                0.022196
#           M                0.034285
# Zone K3   F                0.025156
#           M                0.034961
# Zone X1   F                0.019646
#           M                0.024563
# Zone X3   F                0.027188
#           M                0.038166
# Zone X4   F                0.042149
#           M                0.049956
ri.groupby(['driver_gender', 'district']).is_arrested.mean()

# driver_gender  district
# F              Zone K1     0.019169
#                Zone K2     0.022196
#                Zone K3     0.025156

# Calculating the search rate
# During a traffic stop, the police officer sometimes conducts a search of the vehicle. In this exercise, you'll calculate the percentage of all stops that result in a vehicle search, also known as the search rate.
# Check the data type of 'search_conducted'
print(ri.search_conducted.dtype)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize=True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())

# It looks like the search rate is about 3.8%. Next, you'll examine whether the search rate varies by driver gender.

# Comparing search rates by gender
# In this exercise, you'll compare the rates at which female and male drivers are searched during a traffic stop. Remember that the vehicle search rate across all stops is about 3.8%.

# First, you'll filter the DataFrame by gender and calculate the search rate for each group separately. Then, you'll perform the same calculation for both genders at once using a .groupby().

# Calculate the search rate for female drivers
print(ri[(ri.driver_gender == 'F')].search_conducted.mean())

# Calculate the search rate for male drivers
print(ri[(ri.driver_gender == 'M')].search_conducted.mean())

# Calculate the search rate for both groups simultaneously
print(ri.groupby('driver_gender').search_conducted.mean())

# Wow! Male drivers are searched more than twice as often as female drivers. Why might this be?
# <script.py> output:
#     driver_gender
#     F    0.019181
#     M    0.045426
#     Name: search_conducted, dtype: float64

# Adding a second factor to the analysis
# Even though the search rate for males is much higher than for females, it's possible that the difference is mostly due to a second factor.

# For example, you might hypothesize that the search rate varies by violation type, and the difference in search rate between males and females is because they tend to commit different violations.

# You can test this hypothesis by examining the search rate for each combination of gender and violation. If the hypothesis was true, you would find that males and females are searched at about the same rate for each violation. Find out below if that's the case!

# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['driver_gender','violation']).search_conducted.mean())

# Reverse the ordering to group by violation before gender
print(ri.groupby(['violation','driver_gender']).search_conducted.mean())

#  For all types of violations, the search rate is higher for males than for females, disproving our hypothesis.

# Examining the Search Types
print(ri.search_conducted.value_counts())
# False 83229
# True   3307

print(ri.search_type.value_counts(dropna=False))
# Nan 	83229
# Incident to Arrest 1290

# value_counts excludes missing values by default
# dropna = False Displays missing values

# Searching for a string
ri['inventory'] = ri.search_type.str.contains('Inventory', na=False)
# str.contains() returns True if string is found, False if not found
# na= False returns False when it finds a missing value
print(ri.inventory.dtype) # bool
# True means an inventory was done, False means it was not
print(ri.inventory.sum()) # 441

# Calculating the Inventory Rate
print(ri.inventory.mean()) # 0.0050961449570121106

# 0.5% of all traffic stops resulted in an inventory
searched = ri[ri.search_conducted == True]
searched.inventory.mean() # 0.13335349259147264
# 13.3% of searches included an inventory

# Counting protective frisks
# During a vehicle search, the police officer may pat down the driver to check if they have a weapon. This is known as a "protective frisk."

# In this exercise, you'll first check to see how many times "Protective Frisk" was the only search type. Then, you'll use a string method to locate all instances in which the driver was frisked.

# Count the 'search_type' values
print(ri.search_type.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

# Check the data type of 'frisk'
print(ri.frisk.dtype)

# Take the sum of 'frisk'
print(ri.frisk.sum())

# It looks like there were 303 drivers who were frisked.

# Comparing frisk rates by gender
# In this exercise, you'll compare the rates at which female and male drivers are frisked during a search. Are males frisked more often than females, perhaps because police officers consider them to be higher risk?

# Before doing any calculations, it's important to filter the DataFrame to only include the relevant subset of data, namely stops in which a search was conducted.
# Create a DataFrame of stops in which a search was conducted
searched = ri[ri.search_conducted == True]

# Calculate the overall frisk rate by taking the mean of 'frisk'
print(searched.frisk.mean())

# Calculate the frisk rate for each gender
print(searched.groupby('driver_gender').frisk.mean())
# The frisk rate is higher for males than for females, though we can't conclude that this difference is caused by the driver's gender.