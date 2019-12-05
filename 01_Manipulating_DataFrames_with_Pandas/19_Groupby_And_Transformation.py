def zscore(series):
	return (series - series.mean()) / series.std()

import pandas as pd

auto_mpg = pd.read_csv('../Datasets/01_Manipulating_DataFrames_with_Pandas/auto_mpg.csv')

print(auto_mpg.head())

# MPG z-score
print(zscore(auto_mpg['mpg']).head())

# MPG z-score by year
print(auto_mpg.groupby('yr')['mpg'].transform(zscore).head())

# Apply Transformation and Aggregation
# Aggregation: agg method apply reduction.
# Transformation: Tranformation method apply function element wise to groups

def zscore_with_year_and_name(group):
	df = pd.DataFrame({
		'mpg':zscore(group['mpg']),
		'year': group['yr'],
		'name': group['name']
		})
	return df

print(auto.groupby('yr').apply(zscore_with_year_and_name).head())