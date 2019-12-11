# How to create legends
# Legends can be added to any glyph by using the legend keyword argument.

# In this exercise, you will plot two circle glyphs for female literacy vs fertility in Africa and Latin America.

# Two ColumnDataSources called latin_america and africa have been provided.

# Your job is to plot two circle glyphs for these two objects with fertility on the x axis and female_literacy on the y axis and add the legend values. The figure p has been provided for you.
# Add the first circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=latin_america, size=10, color='red', legend='Latin America')

# Add the second circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=africa, size=10, color='blue', legend='Africa')

# Specify the name of the output_file and show the result
output_file('fert_lit_groups.html')
show(p)

# Positioning and styling legends
# Properties of the legend can be changed by using the legend member attribute of a Bokeh figure after the glyphs have been plotted.

# In this exercise, you'll adjust the background color and legend location of the female literacy vs fertility plot from the previous exercise.

# The figure object p has been created for you along with the circle glyphs.
# Assign the legend to the bottom left: p.legend.location
p.legend.location = 'bottom_left'

# Fill the legend background with the color 'lightgray': p.legend.background_fill_color
p.legend.background_fill_color = 'lightgray'

# Specify the name of the output_file and show the result
output_file('fert_lit_groups.html')
show(p)

# Adding a hover tooltip
# Working with the HoverTool is easy for data stored in a ColumnDataSource.
# In this exercise, you will create a HoverTool object and display the country for each circle glyph in the figure that you created in the last exercise. This is done by assigning the tooltips keyword argument to a list-of-tuples specifying the label and the column of values from the ColumnDataSource using the @ operator.
# The figure object has been prepared for you as p.
# After you have added the hover tooltip to the figure, be sure to interact with it by hovering your mouse over each point to see which country it represents.
# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool object: hover
hover = HoverTool(tooltips = [('Country','@Country')])

# Add the HoverTool object to figure p
p.add_tools(hover)

# Specify the name of the output_file and show the result
output_file('hover.html')
show(p)