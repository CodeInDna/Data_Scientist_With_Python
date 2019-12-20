# Inertia measures clustering quality
# ● Measures how spread out the clusters are (lower is be!er)
# ● Distance from each sample to centroid of its cluster
# ● A"er fit(), available as a!ribute inertia_
# ● k-means a!empts to minimize the inertia when choosing clusters
# In [1]: from sklearn.cluster import KMeans
# In [2]: model = KMeans(n_clusters=3)
# In [3]: model.fit(samples)
# In [4]: print(model.inertia_)
# 78.9408414261

# How many clusters of grain?
# In the video, you learned how to choose a good number of clusters for a dataset using the k-means inertia graph. You are given an array samples containing the measurements (such as area, perimeter, length, and several others) of samples of grain. What's a good number of clusters in this case?
# KMeans and PyPlot (plt) have already been imported for you.
# This dataset was sourced from the UCI Machine Learning Repository.

ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)
    
    # Fit model to samples
    model.fit(samples)
    
    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)
    
# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()
#  The inertia decreases very slowly from 3 clusters to 4, so it looks like 3 clusters would be a good choice for this data.

# Evaluating the grain clustering
# In the previous exercise, you observed from the inertia plot that 3 is a good number of clusters for the grain data. In fact, the grain samples come from a mix of 3 different grain varieties: "Kama", "Rosa" and "Canadian". In this exercise, cluster the grain samples into three clusters, and compare the clusters to the grain varieties using a cross-tabulation.

# You have the array samples of grain samples, and a list varieties giving the grain variety for each sample. Pandas (pd) and KMeans have already been imported for you.
# Create a KMeans model with 3 clusters: model
model = KMeans(n_clusters=3)

# Use fit_predict to fit model and obtain cluster labels: labels
labels = model.fit_predict(samples)

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties'])

# Display ct
print(ct)
# varieties  Canadian wheat  Kama wheat  Rosa wheat
# labels                                           
# 0                      68           9           0
# 1                       0           1          60
# 2                       2          60          10
# The cross-tabulation shows that the 3 varieties of grain separate really well into 3 clusters. But depending on the type of data you are working with, the clustering may not always be this good. Is there anything you can do in such situations to improve your clustering? 