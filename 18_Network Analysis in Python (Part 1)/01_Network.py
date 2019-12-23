# Networks!
# ● Examples:
# ● Social
# ● Transportation
# ● Model relationships between entities

# Basics of NetworkX API, using Twitter network
# To get you up and running with the NetworkX API, we will run through some basic functions that let you query a Twitter network that has been pre-loaded for you and is available in the IPython Shell as T. The Twitter network comes from KONECT, and shows a snapshot of a subset of Twitter users. It is an anonymized Twitter network with metadata.

# You're now going to use the NetworkX API to explore some basic properties of the network, and are encouraged to experiment with the data in the IPython Shell.

# Wait for the IPython shell to indicate that the graph that has been preloaded under the variable name T (representing a Twitter network), and then answer the following question:

# What is the size of the graph T, the type of T.nodes(), and the data structure of the third element of the last edge listed in T.edges(data=True)? The len() and type() functions will be useful here. To access the last entry of T.edges(data=True), you can use list(T.edges(data=True))[-1].
# 23369, networkx.classes.reportviews.NodeView, dict

# Basic drawing of a network using NetworkX
# NetworkX provides some basic drawing functionality that works for small graphs. We have selected a subset of nodes from the graph for you to practice using NetworkX's drawing facilities. It has been pre-loaded as T_sub.
# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt

# Draw the graph to screen
nx.draw(T_sub)
plt.show()