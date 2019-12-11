# A scatter plot with different shapes
# By calling multiple glyph functions on the same figure object, we can overlay multiple data sets in the same figure.

# In this exercise, you will plot female literacy vs fertility for two different regions, Africa and Latin America. Each set of x and y data has been loaded separately for you as fertility_africa, female_literacy_africa, fertility_latinamerica, and female_literacy_latinamerica.

# Your job is to plot the Latin America data with the circle() glyph, and the Africa data with the x() glyph.


# Import output_file and show from bokeh.io
from bokeh.io import output_file, show
# Import figure from bokeh.plotting
from bokeh.plotting import figure

fertility_africa = [5.172999999999999, 2.8160000000000003, 5.211, 5.9079999999999995, 2.505, 5.52, 4.058, 4.859, 2.342, 6.254, 2.334, 4.22, 4.967, 4.513999999999999, 4.62, 4.541, 5.6370000000000005, 5.841, 5.455, 7.069, 5.405, 5.737, 3.363, 4.89, 6.081, 1.841, 5.329, 5.33, 5.377999999999999, 4.45, 4.166, 2.642, 5.165, 4.5280000000000005, 4.697, 5.011, 4.388, 3.29, 3.264, 2.822, 4.968999999999999, 5.659, 3.24, 1.7919999999999998, 3.45, 5.2829999999999995, 3.885, 2.6630000000000003, 3.718]
female_literacy_africa = [48.8, 57.8, 22.8, 56.1, 88.1, 66.3, 59.6, 82.8, 63.9, 66.8, 44.1, 59.3, 40.1, 44.3, 65.3, 67.8, 57.0, 21.6, 65.8, 15.1, 18.2, 61.0, 88.8, 33.0, 21.9, 71.0, 26.4, 66.1, 28.1, 59.9, 53.7, 81.3, 28.9, 54.5, 41.1, 53.0, 49.5, 87.7, 95.1, 83.5, 34.3, 36.5, 83.2, 84.8, 85.6, 89.1, 67.8, 79.3, 83.3]
fertility_latinamerica = [1.827, 2.156, 2.404, 2.2230000000000003, 2.53, 2.498, 1.926, 4.018, 2.513, 1.505, 2.612, 3.3710000000000004, 3.19, 2.977, 2.295, 2.6830000000000003, 1.943, 2.516, 2.089, 2.362, 1.6469999999999998, 2.373, 3.3710000000000004, 1.732]
female_literacy_latinamerica = [90.2, 91.5, 93.4, 97.7, 84.6, 94.9, 98.7, 68.7, 81.7, 99.8, 88.3, 86.0, 83.5, 93.5, 81.4, 77.9, 96.2, 92.8, 98.5, 90.8, 98.2, 88.4, 96.5, 98.0]

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility_latinamerica,female_literacy_latinamerica)

# Add an x glyph to the figure p
p.x(fertility_africa,female_literacy_africa)

# Specify the name of the file
output_file('Bokeh_Output/fert_lit_separate.html')

# Display the plot
show(p)
#  it is quite straightforward to add multiple glyph functions to the same Bokeh figure object.