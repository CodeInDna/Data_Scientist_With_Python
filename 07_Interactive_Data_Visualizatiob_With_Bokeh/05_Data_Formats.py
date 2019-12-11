# NumPy Arrays
# Import output_file and show from bokeh.io
from bokeh.io import output_file, show
# Import figure from bokeh.plotting
from bokeh.plotting import figure

import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x) + np.random.random(1000) * 0.2

plot = figure()

plot.line(x,y)

output_file('Bokeh_Output/numpy.html')

# show(plot)

# Pandas
from bokeh.sampledata.iris import flowers

plot.circle(flowers['petal_length'], flowers['sepal_length'], size=10)

output_file('Bokeh_Output/pandas.html')

# show(plot)

# Data Structure Essential to Bokeh: Column Data Source
from bokeh.models import ColumnDataSource
from bokeh.sampledata.iris import flowers as df

# IMP : All Column in Column DataSource, must be of same length.
source = ColumnDataSource(data={
	'x': [1,2,3,4,5],
	'y': [8,6,5,2,3]
	})

print(source.data) # {'x': [1, 2, 3, 4, 5], 'y': [8, 6, 5, 2, 3]}
print(df.head())
# sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa
source = ColumnDataSource(df)

# Plotting data from NumPy arrays
# In the previous exercises, you made plots using data stored in lists. You learned that Bokeh can plot both numbers and datetime objects.

# In this exercise, you'll generate NumPy arrays using np.linspace() and np.cos() and plot them using the circle glyph.

# np.linspace() is a function that returns an array of evenly spaced numbers over a specified interval. For example, np.linspace(0, 10, 5) returns an array of 5 evenly spaced samples calculated over the interval [0, 10]. np.cos(x) calculates the element-wise cosine of some array x.

# For more information on NumPy functions, you can refer to the NumPy User Guide and NumPy Reference.

# The figure p has been provided for you.

# Import numpy as np
import numpy as np

# Create array using np.linspace: x
x = np.linspace(0, 5, 100)

# Create array using np.cos: y
y = np.cos(x)

# Add circles at x and y
p.circle(x,y)

# Specify the name of the output file and show the result
output_file('Bokeh_Output/numpy.html')
show(p)

# Plotting data from Pandas DataFrames
# You can create Bokeh plots from Pandas DataFrames by passing column selections to the glyph functions.

# Bokeh can plot floating point numbers, integers, and datetime data types. In this example, you will read a CSV file containing information on 392 automobiles manufactured in the US, Europe and Asia from 1970 to 1982.

# The CSV file is provided for you as 'auto.csv'.

# Your job is to plot miles-per-gallon (mpg) vs horsepower (hp) by passing Pandas column selections into the p.circle() function. Additionally, each glyph will be colored according to values in the color column.
# Import pandas as pd
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('../Dataset/Introduction to Data Visualization with Python/auto.csv')

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create the figure: p
p = figure(x_axis_label='HP', y_axis_label='MPG')

# Plot mpg vs hp by color
p.circle(hp,mpg,color=df['color'],size=10)

# Specify the name of the output file and show the result
output_file('Bokeh_Output/auto-df.html')
show(p)

# The Bokeh ColumnDataSource (continued)
# You can create a ColumnDataSource object directly from a Pandas DataFrame by passing the DataFrame to the class initializer.

# In this exercise, we have imported pandas as pd and read in a data set containing all Olympic medals awarded in the 100 meter sprint from 1896 to 2012. A color column has been added indicating the CSS colorname we wish to use in the plot for every data point.

# Your job is to import the ColumnDataSource class, create a new ColumnDataSource object from the DataFrame df, and plot circle glyphs with 'Year' on the x-axis and 'Time' on the y-axis. Color each glyph by the color column.

# The figure object p has already been created for you.

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p.circle(x='Year', y='Time', color='color', size=8, source=source)

# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)