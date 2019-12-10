# Visualizing Data
# Univariate -> "One Variable"

# Visualization Techniques for Sampled Univariate Data
# Strip Plots
# Swarm Plots
# Violin Plots

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv('../Dataset/Introduction to Data Visualization with Python/tips.csv')
print(tips.head())

############ Strip Plot ############ 
sns.stripplot(y='tip', data=tips)
plt.ylabel('tip ($)')

# Grouping with stripplot()
sns.stripplot(x='day', y='tip', data=tips) # Grouping By Day
plt.ylabel('tip ($)')

# Spreading Out Strip Plots
sns.stripplot(x='day', y='tip', data=tips, size=4, jitter=True) # Grouping By Day
plt.ylabel('tip ($)')

############ Swarm Plot ############ 
sns.swarmplot(x='day', y='tip', data=tips)
plt.ylabel('tip ($)')

# Grouping with swarmplot()
sns.swarmplot(x='day', y='tip', data=tips, hue='sex')
plt.ylabel('tip ($)')

# Change Orientation
sns.swarmplot(x='day', y='tip', data=tips, hue='sex', orient='h')
plt.ylabel('tip ($)')

############ Box Plot ############ 
plt.subplot(1,2,1)
sns.boxplot(x='day',y='tip',data=tips)
plt.ylabel('tip ($)')

############ Violin Plot ############ 
plt.subplot(1,2,2)
sns.violinplot(x='day',y='tip',data=tips)
plt.ylabel('tip ($)')
plt.tight_layout()
plt.show()

############ Combining Plots ############ 
sns.violinplot(x='day', y='tip', data=tips, inner=None, color='lightgray')
sns.stripplot(x='day', y='tip', data=tips, size=4, jitter=True)
plt.show()

# Constructing strip plots
# Regressions are useful to understand relationships between two continuous variables. Often we want to explore how the distribution of a single continuous variable is affected by a second categorical variable. Seaborn provides a variety of plot types to perform these types of comparisons between univariate distributions.

# The strip plot is one way of visualizing this kind of data. It plots the distribution of variables for each category as individual datapoints. For vertical strip plots (the default), distributions of continuous values are laid out parallel to the y-axis and the distinct categories are spaced out along the x-axis.

# For example, sns.stripplot(x='type', y='length', data=df) produces a sequence of vertical strip plots of length distributions grouped by type (assuming length is a continuous column and type is a categorical column of the DataFrame df).
# Overlapping points can be difficult to distinguish in strip plots. The argument jitter=True helps spread out overlapping points.
# Other matplotlib arguments can be passed to sns.stripplot(), e.g., marker, color, size, etc.
# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='hp', data=auto)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x='cyl', y='hp', data=auto, size=3, jitter=True)

# Display the plot
plt.show()

# Here, 'hp' is the continuous variable, and 'cyl' is the categorical variable. The strip plot shows that automobiles with more cylinders tend to have higher horsepower.

# Constructing swarm plots
# As you have seen, a strip plot can be visually crowded even with jitter applied and smaller point sizes. An alternative is provided by the swarm plot (sns.swarmplot()), which is very similar but spreads out the points to avoid overlap and provides a better visual overview of the data.

# The syntax for sns.swarmplot() is similar to that of sns.stripplot(), e.g., sns.swarmplot(x='type', y='length', data=df).
# The orientation for the continuous variable in the strip/swarm plot can be inferred from the choice of the columns x and y from the DataFrame data. The orientation can be set explicitly using orient='h' (horizontal) or orient='v' (vertical).
# Another grouping can be added in using the hue keyword. For instance, using sns.swarmplot(x='type', y='length', data=df, hue='build year') makes a swarm plot from the DataFrame df with the 'length' column values spread out vertically, horizontally grouped by the column 'type' and each point colored by the categorical column 'build year'.
# In this exercise, you'll use the auto DataFrame again to illustrate the use of sns.swarmplot() with grouping by hue and with explicit specification of the orientation using the keyword orient.
# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'  
plt.subplot(2,1,1)
sns.swarmplot(x='cyl',y='hp',data=auto)

# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
plt.subplot(2,1,2)
sns.swarmplot(x='cyl',y='hp',orient='v',data=auto,hue='origin')

# Display the plot
plt.show()

# Constructing swarm plots
# As you have seen, a strip plot can be visually crowded even with jitter applied and smaller point sizes. An alternative is provided by the swarm plot (sns.swarmplot()), which is very similar but spreads out the points to avoid overlap and provides a better visual overview of the data.

# The syntax for sns.swarmplot() is similar to that of sns.stripplot(), e.g., sns.swarmplot(x='type', y='length', data=df).
# The orientation for the continuous variable in the strip/swarm plot can be inferred from the choice of the columns x and y from the DataFrame data. The orientation can be set explicitly using orient='h' (horizontal) or orient='v' (vertical).
# Another grouping can be added in using the hue keyword. For instance, using sns.swarmplot(x='type', y='length', data=df, hue='build year') makes a swarm plot from the DataFrame df with the 'length' column values spread out vertically, horizontally grouped by the column 'type' and each point colored by the categorical column 'build year'.
# In this exercise, you'll use the auto DataFrame again to illustrate the use of sns.swarmplot() with grouping by hue and with explicit specification of the orientation using the keyword orient.

# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'  
plt.subplot(2,1,1)
sns.swarmplot(x='cyl',y='hp',data=auto)

# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
plt.subplot(2,1,2)
sns.swarmplot(x='hp',y='cyl',data=auto,hue='origin',orient='h')

# Display the plot
plt.show()
# Swarm plots are generally easier to understand than strip plots because they spread out the points to avoid overlap.

# Constructing violin plots
# Both strip and swarm plots visualize all the datapoints. For large datasets, this can result in significant overplotting. Therefore, it is often useful to use plot types which reduce a dataset to more descriptive statistics and provide a good summary of the data. Box and whisker plots are a classic way of summarizing univariate distributions but seaborn provides a more sophisticated extension of the standard box plot, called a violin plot.

# Here, you will produce violin plots of the distribution of horse power ('hp') by the number of cylinders ('cyl'). Additionally, you will combine two different plot types by overlaying a strip plot on the violin plot.

# As before, the DataFrame has been pre-loaded for you as auto.
# Generate a violin plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='hp', data=auto, inner=None, color='lightgray')

# Overlay a strip plot on the violin plot
sns.stripplot(x='cyl', y='hp', data=auto, size=1.5, jitter=True)

# Display the plot
plt.show()

#  As you can see, violin plots are a nice way of visualizing the relationship between a continuous variable and a categorical variable.