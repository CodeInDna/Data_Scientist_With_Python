# Dealing with Categorical Features
# Need to encode categorical features numerically.
# Convert to 'dummy variables'
	# 0 : Observation was NOT that category
	# 1 : Observation was that category

# Dealing with Categorical Features in Python 
# scikit-learn: OneHotEncoder()
# pandas: get_dummies()

# Exploring categorical features
# The Gapminder dataset that you worked with in previous chapters also contained a categorical 'Region' feature, which we dropped in previous exercises since you did not have the tools to deal with it. Now however, you do, so we have added it back in!

# Your job in this exercise is to explore this feature. Boxplots are particularly useful for visualizing categorical features such as this.
import pandas as pd

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('../Dataset/Supervised Learning with scikit-learn/gm_2008_region.csv')

# Create a boxplot of life expectancy per region
df.boxplot('life', 'Region', rot=60)

# Show the plot
plt.show()

# Exploratory data analysis should always be the precursor to model building.

# Creating dummy variables
# As Andy discussed in the video, scikit-learn does not accept non-numerical features. You saw in the previous exercise that the 'Region' feature contains very useful information that can predict life expectancy. For example, Sub-Saharan Africa has a lower life expectancy compared to Europe and Central Asia. Therefore, if you are trying to predict life expectancy, it would be preferable to retain the 'Region' feature. To do this, you need to binarize it by creating dummy variables, which is what you will do in this exercise.
# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)
# Index(['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP',
#        'BMI_female', 'life', 'child_mortality', 'Region_America',
#        'Region_East Asia & Pacific', 'Region_Europe & Central Asia',
#        'Region_Middle East & North Africa', 'Region_South Asia',
#        'Region_Sub-Saharan Africa'],
#       dtype='object')
# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df,drop_first=True)

# Print the new columns of df_region
print(df_region.columns)

# Index(['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP',
#        'BMI_female', 'life', 'child_mortality', 'Region_East Asia & Pacific',
#        'Region_Europe & Central Asia', 'Region_Middle East & North Africa',
#        'Region_South Asia', 'Region_Sub-Saharan Africa'],
#       dtype='object')

# Regression with categorical features
# Having created the dummy variables from the 'Region' feature, you can build regression models as you did before. Here, you'll use ridge regression to perform 5-fold cross-validation.

# The feature array X and target variable array y have been pre-loaded.
# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X,y,cv=5)

# Print the cross-validated scores
print(ridge_cv)