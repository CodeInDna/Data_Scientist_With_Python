# Selection and non-selection glyphs
# In this exercise, you're going to add the box_select tool to a figure and change the selected and non-selected circle glyph properties so that selected glyphs are red and non-selected glyphs are transparent blue.

# You'll use the ColumnDataSource object of the Olympic Sprint dataset you made in the last exercise. It is provided to you with the name source.

# After you have created the figure, be sure to experiment with the Box Select tool you added! As in previous exercises, you may have to scroll down to view the lower portion of the figure.

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label = 'Year', y_axis_label = 'Time', tools='box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle('Year', 'Time', source=source, selection_color='red', nonselection_alpha=0.1 , nonselection_color = 'blue')

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)

# Hover glyphs
# Now let's practice using and customizing the hover tool.
# In this exercise, you're going to plot the blood glucose levels for an unknown patient. The blood glucose levels were recorded every 5 minutes on October 7th starting at 3 minutes past midnight.
# The date and time of each measurement are provided to you as x and the blood glucose levels in mg/dL are provided as y.
# A bokeh figure is also provided in the workspace as p.
# Your job is to add a circle glyph that will appear red when the mouse is hovered near the data points. You will also add a customized hover tool object to the plot.
# When you're done, play around with the hover tool you just created! Notice how the points where your mouse hovers over turn red.

# import the HoverTool
from bokeh.models import HoverTool

# Add circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color='grey', alpha=0.1, line_color=None,
         hover_fill_color='firebrick', hover_alpha=0.5,
         hover_line_color='white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)

# Colormapping
# The final glyph customization we'll practice is using the CategoricalColorMapper to color each glyph by a categorical property.

# Here, you're going to use the automobile dataset to plot miles-per-gallon vs weight and color each circle glyph by the region where the automobile was manufactured.

# The origin column will be used in the ColorMapper to color automobiles manufactured in the US as blue, Europe as red and Asia as green.

# The automobile data set is provided to you as a Pandas DataFrame called df. The figure is provided for you as p.
#Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])

# Add a circle glyph to the figure p
p.circle('weight', 'mpg', source=source,
            color= dict(field='origin', transform=color_mapper),
            legend ='origin')

# Specify the name of the output file and show the result
output_file('colormap.html')
show(p)