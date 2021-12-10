## TESTING FOR NETWORKX CONVERSION AND DISPLAY 
import random_metric_graph as rmg

import random as r
import numpy as np

# importing networkx stuff
import networkx as nx
from networkx.convert_matrix import from_numpy_array
from networkx.algorithms.approximation.traveling_salesman import christofides
# importing matplotlib.pyplot
import matplotlib.pyplot as plt






g = rmg.randCompleteMetricGraph(10)

# convert the Graph adjacency matrix array to a numpy matrix of the edges
g2 = np.matrix(g)

# create a networkx graph from the numpy matrix
g3 = nx.Graph(from_numpy_array(g2))

# draw the graph 
nx.draw_networkx(g3, node_size=200)

# display the graph
plt.show()

# create a TSP object to use
tsp = nx.approximation.traveling_salesman_problem

# run the TSP function using Christofides and print the path
path = tsp(g3, cycle=False, method=christofides)
print(path)