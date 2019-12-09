# Using hist2d()
# Given a set of ordered pairs describing data points, you can count the number of points with similar values to construct a two-dimensional histogram. This is similar to a one-dimensional histogram, but it describes the joint variation of two random variables rather than just one.

# In matplotlib, one function to visualize 2-D histograms is plt.hist2d().

# You specify the coordinates of the points using plt.hist2d(x,y) assuming x and y are two vectors of the same length.
# You can specify the number of bins with the argument bins=(nx, ny) where nx is the number of bins to use in the horizontal direction and ny is the number of bins to use in the vertical direction.
# You can specify the rectangular region in which the samples are counted in constructing the 2D histogram. The optional parameter required is range=((xmin, xmax), (ymin, ymax)) where
# xmin and xmax are the respective lower and upper limits for the variables on the x-axis and
# ymin and ymax are the respective lower and upper limits for the variables on the y-axis. Notice that the optional range argument can use nested tuples or lists.
# In this exercise, you'll use some data from the auto-mpg data set. There are two arrays mpg and hp that respectively contain miles per gallon and horse power ratings from over three hundred automobiles built.

import matplotlib.pyplot as plt
import pandas as pd

auto_mpg = pd.read_csv('../Dataset/Introduction to Data Visualization with Python/auto-mpg.csv')

hp = auto_mpg['hp'] 
mpg = auto_mpg['mpg']

# Generate a 2-D histogram
plt.hist2d(hp, mpg, bins=(20,20),range=((40,235),(8,48)))

# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()

# As you might expect, cars with higher hp have lower mpg.
# Generate a 2d histogram with hexagonal bins
plt.hexbin(hp,mpg, gridsize=(15,12), extent=(40,235,8,48))

           
# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()