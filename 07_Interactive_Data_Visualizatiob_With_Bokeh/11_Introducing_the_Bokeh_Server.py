# Basic App Outline (outline.py)
# from boken.io import curdoc

# # Create plots and widgets

# # Add callbacks

# # Arrange plots and widgets in layout

# curdoc().add_root(layout)

# Running Bokeh Applications
# Run Single Module Apps at the Shell or Windows
# bokeh serve --show myapp.py

# Bokeh server will automatically keep every property of any Bokeh object in sync.

# Using the current document
# Let's get started with building an interactive Bokeh app. This typically begins with importing the curdoc, or "current document", function from bokeh.io. This current document will eventually hold all the plots, controls, and layouts that you create. Your job in this exercise is to use this function to add a single plot to your application.

# In the video, Bryan described the process for running a Bokeh app using the bokeh serve command line tool. In this chapter and the one that follows, the DataCamp environment does this for you behind the scenes. Notice that your code is part of a script.py file. When you hit 'Submit Answer', you'll see in the IPython Shell that we call bokeh serve script.py for you.

# Remember, as in the previous chapters, that there are different options available for you to interact with your plots, and as before, you may have to scroll down to view the lower portion of the plots.
# Perform necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure

# Create a new plot: plot
plot = figure()

# Add a line to the plot
plot.line(x=[1,2,3,4,5], y =[2,5,4,6,7])

# Add the plot to the current document
curdoc().add_root(plot)

# Add a single slider
# In the previous exercise, you added a single plot to the "current document" of your application. In this exercise, you'll practice adding a layout to your current document.
# Your job here is to create a single slider, use it to create a widgetbox layout, and then add this layout to the current document.
# The slider you create here cannot be used for much, but in the later exercises, you'll use it to update your plots!

# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create a slider: slider
slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)

# Create a widgetbox layout: layout
layout = widgetbox(slider)

# Add the layout to the current document
curdoc().add_root(layout)

# Multiple sliders in one document
# Having added a single slider in a widgetbox layout to your current document, you'll now add multiple sliders into the current document.

# Your job in this exercise is to create two sliders, add them to a widgetbox layout, and then add the layout into the current document.

# Perform necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create first slider: slider1
slider1 = Slider(title='slider1',start=0,end=10,step=0.1,value=2)

# Create second slider: slider2
slider2 = Slider(title='slider2',start=10,end=100,step=1,value=20)

# Add slider1 and slider2 to a widgetbox
layout = widgetbox(slider1, slider2)

# Add the layout to the current document
curdoc().add_root(layout)

# How to combine Bokeh models into layouts
# Let's begin making a Bokeh application that has a simple slider and plot, that also updates the plot based on the slider.

# In this exercise, your job is to first explicitly create a ColumnDataSource. You'll then combine a plot and a slider into a single column layout, and add it to the current document.

# After you are done, notice how in the figure you generate, the slider will not actually update the plot, because a widget callback has not been defined. You'll learn how to update the plot using widget callbacks in the next exercise.

# All the necessary modules have been imported for you. The plot is available in the workspace as plot, and the slider is available as slider.
# Create ColumnDataSource: source
source = ColumnDataSource(data = {'x':x, 'y':y})

# Add a line to the plot
plot.line('x', 'y', source=source)

# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)

# Since a widget callback hasn't been defined here, the slider does not update the figure.

# Learn about widget callbacks
# You'll now learn how to use widget callbacks to update the state of a Bokeh application, and in turn, the data that is presented to the user.

# Your job in this exercise is to use the slider's on_change() function to update the plot's data from the previous example. NumPy's sin() function will be used to update the y-axis data of the plot.

# Now that you have added a widget callback, notice how as you move the slider of your app, the figure also updates!

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)