# Arranging Multiple Plts
# Arrange plots (and controls) visually on a page:
	# rows, columns
	# grid, arrangements
	# tabbed layouts

# Creating rows of plots
# Layouts are collections of Bokeh figure objects.

# In this exercise, you're going to create two plots from the Literacy and Birth Rate data set to plot fertility vs female literacy and population vs female literacy.

# By using the row() method, you'll create a single layout of the two figures.

# Remember, as in the previous chapter, once you have created your figures, you can interact with them in various ways.

# In this exercise, you may have to scroll sideways to view both figures in the row layout. Alternatively, you can view the figures in a new window by clicking on the expand icon to the right of the "Bokeh plot" tab.

# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p1
p1.circle('fertility', 'female_literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p2
p2.circle('population' , 'female_literacy', source=source)

# Put p1 and p2 into a horizontal row: layout
layout = row(p1, p2)

# Specify the name of the output_file and show the result
output_file('fert_row.html')
show(layout)

# Creating columns of plots
# In this exercise, you're going to use the column() function to create a single column layout of the two plots you created in the previous exercise.

# Figure p1 has been created for you.

# In this exercise and the ones to follow, you may have to scroll down to view the lower portion of the figure.
# Import column from the bokeh.layouts module
from bokeh.layouts import column

# Create a blank figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add circle scatter to the figure p1
p1.circle('fertility', 'female_literacy', source=source)

# Create a new blank figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add circle scatter to the figure p2
p2.circle('population', 'female_literacy', source=source)

# Put plots p1 and p2 in a column: layout
layout = column(p1,p2)

# Specify the name of the output_file and show the result
output_file('fert_column.html')
show(layout)

# Nesting rows and columns of plots
# You can create nested layouts of plots by combining row and column layouts. In this exercise, you'll make a 3-plot layout in two rows using the auto-mpg data set. Three plots have been created for you of average mpg vs year (avg_mpg), mpg vs hp (mpg_hp), and mpg vs weight (mpg_weight).

# Your job is to use the row() and column() functions to make a two-row layout where the first row will have only the average mpg vs year plot and the second row will have mpg vs hp and mpg vs weight plots as columns.

# By using the sizing_mode argument, you can scale the widths to fill the whole figure.
# Import column and row from bokeh.layouts
from bokeh.layouts import row, column

# Make a row layout that will be used as the second row: row2
row2 = row([mpg_hp, mpg_weight], sizing_mode='scale_width')

# Make a column layout that includes the above row layout: layout
layout = column([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)