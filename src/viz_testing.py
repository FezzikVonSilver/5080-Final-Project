import random as r
from networkx.convert_matrix import from_numpy_array
import numpy as np

# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt
from networkx.algorithms.approximation.traveling_salesman import christofides


"""
Helper function to check that random edge obeys the triangle inequality/is metric space
"""
def obeysMetric(g, i, j):
    for k in range(len(g)):
        # triangle inequality: edge weight w(i->j) should be less than or equal to w(i->k)+w(k->j)
        if g[i][k] == 0 or g[j][k] == 0: 
            continue
        if g[i][k]+g[k][j] < g[i][j]:
            return False
    return True

"""
n: number of vertices in the complete graph
w_rnge: default edge weight range is 1 to 10

return: adjacency matrix representing complete metric graph
"""
def randCompleteMetricGraph(n, w_rnge = (1,10)):
    g = [[0 for _ in range(n)] for _ in range(n)] # initialize adjacency matrix
    for i in range(n):
        for j in range(n):
            if g[j][i] != 0: # matrix is symmetric b/c graph's undirected
                g[i][j] = g[j][i]
            elif i != j: #if vertex is not itself, create random edge
                g[i][j] = r.randint(w_rnge[0], w_rnge[1])
                while not obeysMetric(g, i, j):
                    g[i][j] = r.randint(w_rnge[0], w_rnge[1])
    return g


g = randCompleteMetricGraph(10)

# convert the Graph adjacency matrix array to a numpy matrix
g2 = np.matrix(g)

# create a networkx graph from the numpy matrix
g3 = nx.Graph(from_numpy_array(g2))


# set position using spring layout (this should result in the nodes displaying at the same position each time the same graph object is drawn if used in call)
pos = nx.spring_layout(g3, seed=123)


# draw the nodes only for the graph
nx.draw_networkx_nodes(g3, pos, nodelist=set(g3.nodes))
# display the graph
plt.show()

# draw the edges only for the graph 
nx.draw_networkx_edges(g3, pos, edgelist=set(g3.edges))
# display the graph
plt.show()

# draw the full graph 
nx.draw_networkx(g3, pos)
# display the graph
plt.show()


# Get a shortest path (this will be only 1 edge long as the graph is complete) 
path = nx.shortest_path(g3,source=1,target=7)
path_edges = list(zip(path,path[1:]))

# Draw nodes not in the shortest path
nx.draw_networkx_nodes(g3, pos, nodelist=set(g3.nodes)-set(path))
# draw the edges not in the shortest path
nx.draw_networkx_edges(g3, pos, edgelist=set(g3.edges)-set(path_edges), connectionstyle='arc3, rad = 0.3')

# Draw nodes and edges included in path, both as red
nx.draw_networkx_nodes(g3, pos, nodelist=path, node_color='r')
nx.draw_networkx_edges(g3,pos,edgelist=path_edges,edge_color='r', connectionstyle='arc3, rad = 0.3')

# display the graph
plt.show()


# create a TSP object to use
tsp = nx.approximation.traveling_salesman_problem

# run the TSP function using Christofides and save the path
path = tsp(g3, cycle=False, method=christofides)
# print(path)

path_edges = list(zip(path,path[1:]))

# draw the edges not in the TSP path
# nx.draw_networkx_edges(g3, pos, edgelist=set(g3.edges)-set(path_edges), connectionstyle='arc3, rad = 0.3')

# Draw nodes and edges included in path, nodes blue and edges red
nx.draw_networkx_nodes(g3, pos, nodelist=path, node_color='b')
nx.draw_networkx_edges(g3,pos,edgelist=path_edges,edge_color='r', connectionstyle='arc3, rad = 0.3')

# display the graph
plt.show()

# plt.show()