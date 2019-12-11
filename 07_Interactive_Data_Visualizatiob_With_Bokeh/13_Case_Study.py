# Introducing the project dataset
# For the final chapter, you'll be looking at some of the Gapminder datasets combined into one tidy file called "gapminder_tidy.csv". This data set is available as a pandas DataFrame under the variable name data.

# It is always a good idea to begin with some Exploratory Data Analysis. Pandas has a number of built-in methods that help with this. For example, data.head() displays the first five rows/entries of data, while data.tail() displays the last five rows/entries. data.shape gives you information about how many rows and columns there are in the data set. Another particularly useful method is data.info(), which provides a concise summary of data, including information about the number of entries, columns, data type of each column, and number of non-null entries in each column.

# Use the IPython Shell and the pandas methods mentioned above to explore this data set. How many entries and columns does this data set have?

# Some exploratory plots of the data
# Here, you'll continue your Exploratory Data Analysis by making a simple plot of Life Expectancy vs Fertility for the year 1970.

# Your job is to import the relevant Bokeh modules and then prepare a ColumnDataSource object with the fertility, life and Country columns, where you only select the rows with the index value 1970.

# Remember, as with the figures you generated in previous chapters, you can interact with your figures here with a variety of tools.
# Perform necessary imports
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
import pandas as pd

data = pd.read_csv('../Dataset/Interactive Data Visualization with Bokeh/gapminder_tidy.csv', index_col='Year')

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'       : data.loc[1970].fertility,
    'y'       : data.loc[1970].life,
    'country' : data.loc[1970].Country,
})

# Create the figure: p
p = figure(title='1970', x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips='@country')])

# Add a circle glyph to the figure p
p.circle(x='x', y='y', source=source)

# Output the file and show the figure
output_file('Bokeh_Output/gapminder.html')
show(p)