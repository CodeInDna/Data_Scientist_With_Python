import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv('../Dataset/Introduction to Data Visualization with Python/tips.csv')
sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()

# Using Hue
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='Set1')
plt.show()

# Using Col
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
plt.show()

# Using residplot()
sns.residplot(x='age', y='fare', data=df, palette='indianred')
plt.show()

# Simple linear regressions
# As you have seen, seaborn provides a convenient interface to generate complex and great-looking statistical plots. One of the simplest things you can do using seaborn is to fit and visualize a simple linear regression between two variables using sns.lmplot().

# One difference between seaborn and regular matplotlib plotting is that you can pass pandas DataFrames directly to the plot and refer to each column by name. For example, if you were to plot the column 'price' vs the column 'area' from a DataFrame df, you could call sns.lmplot(x='area', y='price', data=df).

# In this exercise, you will once again use the DataFrame auto containing the auto-mpg dataset. You will plot a linear regression illustrating the relationship between automobile weight and horse power.
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='weight', y='hp', data=auto)

# Display the plot
plt.show()
# Unsurprisingly, there is a strong correlation between 'hp' and 'weight', and a linear regression is easily able to capture this trend.

# Plotting residuals of a regression
# Often, you don't just want to see the regression itself but also see the residuals to get a better idea how well the regression captured the data. Seaborn provides sns.residplot() for that purpose, visualizing how far datapoints diverge from the regression line.
# In this exercise, you will visualize the residuals of a regression between the 'hp' column (horse power) and the 'mpg' column (miles per gallon) of the auto DataFrame used previously.
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()


# Higher-order regressions
# When there are more complex relationships between two variables, a simple first order regression is often not sufficient to accurately capture the relationship between the variables. Seaborn makes it simple to compute and visualize regressions of varying orders.

# Here, you will plot a second order regression between the horse power ('hp') and miles per gallon ('mpg') using sns.regplot() (the function sns.lmplot() is a higher-level interface to sns.regplot()). However, before plotting this relationship, compare how the residual changes depending on the order of the regression. Does a second order regression perform significantly better than a simple linear regression?

# A principal difference between sns.lmplot() and sns.regplot() is the way in which matplotlib options are passed (sns.regplot() is more permissive).
# For both sns.lmplot() and sns.regplot(), the keyword order is used to control the order of polynomial regression.
# The function sns.regplot() uses the argument scatter=None to prevent plotting the scatter plot points again.
# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, color='blue',scatter=None, label='First Order')

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, color='green',scatter=None, order = 2, label='Second Order')

# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()

# Grouping linear regressions by hue
# Often it is useful to compare and contrast trends between different groups. Seaborn makes it possible to apply linear regressions separately for subsets of the data by applying a groupby operation. Using the hue argument, you can specify a categorical variable by which to group data observations. The distinct groups of points are used to produce distinct regressions with different hues in the plot.

# In the automobile dataset - which has been pre-loaded here as auto - you can view the relationship between weight ('weight') and horsepower ('hp') of the cars and group them by their origin ('origin'), giving you a quick visual indication how the relationship differs by continent.
# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight', y='hp', data=auto, hue='origin', palette='Set1')

# Display the plot
plt.show()
# It looks like US automobiles tend to have higher hp.

# Grouping linear regressions by row or column
# Rather than overlaying linear regressions of grouped data in the same plot, we may want to use a grid of subplots. The sns.lmplot() accepts the arguments row and/or col to arrangements of subplots for regressions.

# You'll use the automobile dataset again and, this time, you'll use the keyword argument row to display the subplots organized in rows. That is, you'll produce horsepower vs. weight regressions grouped by continent of origin in separate subplots stacked vertically.
# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto, row = 'origin')

# Display the plot
plt.show()