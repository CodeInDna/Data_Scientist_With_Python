# Using meshgrid()
import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2, 2, 3)
v = np.linspace(-1, 1, 5)
X,Y = np.meshgrid(u, v)
Z = X ** 2/25 + Y ** 2/4

print('Z:\n', Z)

# Z:
#  [[0.41   0.25   0.41  ]
#  [0.2225 0.0625 0.2225]
#  [0.16   0.     0.16  ]
#  [0.2225 0.0625 0.2225]
#  [0.41   0.25   0.41  ]]

plt.set_cmap('Greys_r')
plt.pcolor(Z)
plt.show()

# Generating meshes
# In order to visualize two-dimensional arrays of data, it is necessary to understand how to generate and manipulate 2-D arrays. Many Matplotlib plots support arrays as input and in particular, they support NumPy arrays. The NumPy library is the most widely-supported means for supporting numeric arrays in Python.

# In this exercise, you will use the meshgrid function in NumPy to generate 2-D arrays which you will then visualize using plt.imshow(). The simplest way to generate a meshgrid is as follows:

# import numpy as np
# Y,X = np.meshgrid(range(10),range(20))
# This will create two arrays with a shape of (20,10), which corresponds to 20 rows along the Y-axis and 10 columns along the X-axis. In this exercise, you will use np.meshgrid() to generate a regular 2-D sampling of a mathematical function.
# Import numpy and matplotlib.pyplot
# Generate two 1-D arrays: u, v
u = np.linspace(-2, +2, 41)
v = np.linspace(-1, +1, 21)

# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u,v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2)) 

# Display the resulting image with pcolor()
plt.pcolor(Z, cmap='Blues')
plt.show()

# Save the figure to 'sine_mesh.png'
plt.savefig('sine_mesh.png')

# The commands

# In [1]: plt.pcolor(A, cmap='Blues')
# In [2]: plt.colorbar()
# In [3]: plt.show()

# Visualizing bivariate functions
# Contour & filled contour plots
# Although plt.imshow() or plt.pcolor() are often used to visualize a 2-D array in entirety, there are other ways of visualizing such data without displaying all of the available sample values. One option is to use the array to compute contours that are visualized instead.

# Two types of contour plot supported by Matplotlib are plt.contour() and plt.contourf() where the former displays the contours as lines and the latter displayed filled areas between contours. Both these plotting commands accept a two dimensional array from which the appropriate contours are computed.

# In this exercise, you will visualize a 2-D array repeatedly using both plt.contour() and plt.contourf(). You will use plt.subplot() to display several contour plots in a common figure, using the meshgrid X, Y as the axes. For example, plt.contour(X, Y, Z) generates a default contour map of the array Z.

# Don't forget to include the meshgrid in each plot for this exercise!

# Generate a default contour map of the array Z
plt.subplot(2,2,1)
plt.contour(X,Y,Z)

# Generate a contour map with 20 contours
plt.subplot(2,2,2)
plt.contour(X,Y,Z,20)

# Generate a default filled contour map of the array Z
plt.subplot(2,2,3)
plt.contourf(X,Y,Z)

# Generate a default filled contour map with 20 contours
plt.subplot(2,2,4)
plt.contourf(X,Y,Z, 20)

# Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()

# Modifying colormaps
# When displaying a 2-D array with plt.imshow() or plt.pcolor(), the values of the array are mapped to a corresponding color. The set of colors used is determined by a colormap which smoothly maps values to colors, making it easy to understand the structure of the data at a glance.

# It is often useful to change the colormap from the default 'jet' colormap used by matplotlib. A good colormap is visually pleasing and conveys the structure of the data faithfully and in a way that makes sense for the application.

# Some matplotlib colormaps have unique names such as 'jet', 'coolwarm', 'magma' and 'viridis'.
# Others have a naming scheme based on overall color such as 'Greens', 'Blues', 'Reds', and 'Purples'.
# Another four colormaps are based on the seasons, namely 'summer', 'autumn', 'winter' and 'spring'.
# You can insert the option cmap=<name> into most matplotlib functions to change the color map of the resulting plot.
# In this exercise, you will explore four different colormaps together using plt.subplot(). You will use a pregenerated array Z and a meshgrid X, Y to generate the same filled contour plot with four different color maps. Be sure to also add a color bar to each filled contour plot with plt.colorbar().
# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20, cmap='winter')
plt.colorbar()
plt.title('Winter')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()