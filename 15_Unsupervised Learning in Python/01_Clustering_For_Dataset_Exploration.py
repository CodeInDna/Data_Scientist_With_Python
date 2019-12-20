# How many clusters?
# You are given an array points of size 300x2, where each row gives the (x, y) co-ordinates of a point on a map. Make a scatter plot of these points, and use the scatter plot to guess how many clusters there are.

# matplotlib.pyplot has already been imported as plt. In the IPython Shell:

# Create an array called xs that contains the values of points[:,0] - that is, column 0 of points.
# Create an array called ys that contains the values of points[:,1] - that is, column 1 of points.
# Make a scatter plot by passing xs and ys to the plt.scatter() function.
# Call the plt.show() function to show your plot.
# How many clusters do you see?
# The scatter plot suggests that there are 3 distinct clusters.

# Clustering 2D points
# From the scatter plot of the previous exercise, you saw that the points seem to separate into 3 clusters. You'll now create a KMeans model to find 3 clusters, and fit it to the data points from the previous exercise. After the model has been fit, you'll obtain the cluster labels for some new points using the .predict() method.

# You are given the array points from the previous exercise, and also an array new_points.

# Import KMeans
from sklearn.cluster import KMeans

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters = 3)

# Fit model to points
model.fit(points)

# Determine the cluster labels of new_points: labels
labels = model.predict(new_points)

# Print cluster labels of new_points
print(labels)
# You've successfully performed k-Means clustering and predicted the labels of new points. But it is not easy to inspect the clustering by just looking at the printed labels. A visualization would be far more useful.

# Inspect your clustering
# Let's now inspect the clustering you performed in the previous exercise!
# A solution to the previous exercise has already run, so new_points is an array of points and labels is the array of their cluster labels.
# Import pyplot
import matplotlib.pyplot as plt

# Assign the columns of new_points: xs and ys
xs = new_points[:,0]
ys = new_points[:,1]

# Make a scatter plot of xs and ys, using labels to define the colors
plt.scatter(xs, ys, c=labels, alpha = 0.5)

# Assign the cluster centers: centroids
centroids = model.cluster_centers_

# Assign the columns of centroids: centroids_x, centroids_y
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]

# Make a scatter plot of centroids_x and centroids_y
plt.scatter(centroids_x, centroids_y, marker='D', s=50)
plt.show()
# The clustering looks great! But how can you be sure that 3 clusters is the correct choice? In other words, how can you evaluate the quality of a clustering?