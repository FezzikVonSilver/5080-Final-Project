import random as r
import numpy as np
import time

# importing networkx
import networkx as nx
from networkx.convert_matrix import from_numpy_array
from networkx.algorithms.approximation.traveling_salesman import christofides
# importing matplotlib.pyplot
from matplotlib import pyplot as plt, animation


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


g = randCompleteMetricGraph(5)

# convert the Graph adjacency matrix array to a numpy matrix
g2 = np.matrix(g)

# create a networkx graph from the numpy matrix
g3 = nx.Graph(from_numpy_array(g2))



"""
Function to create graph from a simple 2d-array
Takes the 

n: number of vertices in the complete graph
G: adjacency matrix representing complete metric graph 

return: a networkx graph object
"""
def create_nwx_Graph(n, G):
        g4 = nx.Graph()

        for i in range (n):
            g4.add_node(i)

    #Adds edges along with their weights to the graph 
        for i in range(n) :
         for j in range(n)[i:] :
          if G[i][j] != 0 :
               g4.add_edge(i, j, weight = G[i][j]) 
               print(G[i][j])
        return g4




g3 = create_nwx_Graph(5,g)
print(g3)

for edge in g3.edges:
    print(edge)


print(g)



# set position using spring layout (this will result in the nodes displaying at the same position each time the same graph object is drawn if used in call)
pos = nx.spring_layout(g3, seed=123)

# get the edge weights as labels
labels = nx.get_edge_attributes(g3,'weight')
# draw the graph
nx.draw_networkx(g3, pos)
# add the edge weights to the graph
nx.draw_networkx_edge_labels(g3,pos,edge_labels=labels)
plt.show()



# create fig object for animation
fig = plt.figure()

# Function to animate a series of steps which can be displayed
def animate(frame):
    fig.clear()

    # for i in range (6):
    if frame <= 1:
        # draw the nodes only for the graph
        nx.draw_networkx_nodes(g3, pos, nodelist=set(g3.nodes))
        plt.show()

    if frame == 2:
        # draw the edges only for the graph 
        nx.draw_networkx_edges(g3, pos, edgelist=set(g3.edges))
        plt.show()

    if frame ==3:
        # draw the full graph 
        nx.draw_networkx(g3, pos)
        plt.show()

    if frame ==4:
        # Get a shortest path (this will be only 1 edge long as the graph is complete) 
        path = nx.shortest_path(g3,source=1,target=4)
        path_edges = list(zip(path,path[1:]))
        # Draw nodes and edges not in the shortest path
        nx.draw_networkx_nodes(g3, pos, nodelist=set(g3.nodes)-set(path))
        nx.draw_networkx_edges(g3, pos, edgelist=set(g3.edges)-set(path_edges), connectionstyle='arc3, rad = 0.3')
        # Draw nodes and edges included in path, both as red
        # nx.draw_networkx_nodes(g3, pos, nodelist=path, node_color='r')
        nx.draw_networkx_nodes(g3, pos, nodelist=path)
        nx.draw_networkx_edges(g3, pos, edgelist=path_edges,edge_color='r', connectionstyle='arc3, rad = 0.3')
        plt.show()

    if frame >=5:
        # create a TSP object to use
        tsp = nx.approximation.traveling_salesman_problem
        # run the TSP function using Christofides and save the path
        path = tsp(g3, cycle=True, method=christofides)
        print(path)
        # get the edges in a list
        path_edges = list(zip(path,path[1:]))
        # draw the edges not in the TSP path
        # nx.draw_networkx_edges(g3, pos, edgelist=set(g3.edges)-set(path_edges), connectionstyle='arc3, rad = 0.3')
        # Draw nodes and edges included in path, nodes blue and edges red
        nx.draw_networkx_nodes(g3, pos, nodelist=path, node_color='b')
        nx.draw_networkx_edges(g3,pos,edgelist=path_edges,edge_color='r', connectionstyle='arc3, rad = 0.3')
        plt.show()

    return

# create the animation object
# ani = animation.FuncAnimation(fig, animate, frames=6, interval=1000, repeat=False)

# display the animation on screen in a popup window
# plt.show()
