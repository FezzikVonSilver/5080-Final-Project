import random as r
import numpy as np
import time

# importing networkx
import networkx as nx
from networkx.convert_matrix import from_numpy_array
from networkx.algorithms.approximation.traveling_salesman import christofides
# importing matplotlib.pyplot
from matplotlib import pyplot as plt, animation

# project file imports
import random_metric_graph as rmg
from min_span_tree import mst
from combine import combine
from create_tour import create_tour


"""
Function to create graph from the tsp_tour returned

n: number of vertices in the complete tour
TSP: the tour object

return: a networkx graph object
"""
def translate_TSP_Tour(n, TSP):
    g2 = nx.Graph()

    for i in range (n):
        g2.add_node(i)

    #Adds edges along with their weights to the graph 
        for i in range(n-1) :
                # dummy weight of one for the graph, not sure if needed?
                g2.add_edge(TSP[i], TSP[i+1], weight = 1) 
        return g2

# create the starting random graph
g = rmg.randCompleteMetricGraph(10)

# set position using spring layout (this will result in the nodes displaying at the same position each time the same graph object is drawn if used in call)
pos = nx.spring_layout(g, seed=123)

# get MST of g
T = mst(g)

# get combined
M = combine(T, g)

# get tour
tsp_tour = create_tour(M, g)

#translate to play nicely with drawing
g_tsp = translate_TSP_Tour(11, tsp_tour)


# create fig object for animation
fig = plt.figure()

# Function to animate steps in the TSP algorithm
def animate(frame):
    fig.clear()

    # for i in range (6):
    if frame == 0:
        # draw the full graph 
        nx.draw_networkx(g, pos)
        plt.show()
        plt.savefig("filename1.png")
        print("0 - Starting Graph")

    if frame == 1:
        # draw the MST of the graph 
        nx.draw_networkx(T, pos)
        plt.show()
        plt.savefig("filename2.png")
        print("1 - MST")

    if frame == 2:
        # draw combined min-weight matching and MST
        nx.draw_networkx(M, pos)
        plt.show()
        plt.savefig("filename3.png")
        print("2 - Min-Weight Matching & MST")

    if frame >= 3:
        # draw our TSP tour
        nx.draw_networkx(g_tsp, pos, edge_color='r')
        plt.show()
        plt.savefig("filename4.png")
        # print(tsp_tour)
        # print(g_tsp)
        print("3 - TSP Tour")

    # if frame == 3:
        # # Draw edges not in the tour
        # nx.draw_networkx_edges(g, pos, edgelist=set(g.edges)-set(tsp_tour), connectionstyle='arc3, rad = 0.3')
        # # Draw nodes and edges included in path, both as red
        # # nx.draw_networkx_nodes(g3, pos, nodelist=path, node_color='r')
        # nx.draw_networkx_nodes(g, pos, nodelist=tsp_tour)
        # nx.draw_networkx_edges(g, pos, edgelist=tsp_tour,edge_color='r', connectionstyle='arc3, rad = 0.3')
        # plt.show()
        # print(3)

    # if frame >= 4:
    #     # create a TSP object to use
    #     tsp = nx.approximation.traveling_salesman_problem
    #     # run the TSP function using Christofides and save the path
    #     path = tsp(g, cycle=True, method=christofides)
    #     print(path)
    #     # get the edges in a list
    #     path_edges = list(zip(path,path[1:]))
    #     # draw the edges not in the TSP path
    #     # nx.draw_networkx_edges(g3, pos, edgelist=set(g3.edges)-set(path_edges), connectionstyle='arc3, rad = 0.3')
    #     # Draw nodes and edges included in path, nodes blue and edges red
    #     # nx.draw_networkx_nodes(g2, pos, nodelist=path, node_color='b')
    #     nx.draw_networkx_nodes(g, pos, nodelist=path)
    #     nx.draw_networkx_edges(g,pos,edgelist=path_edges,edge_color='r', connectionstyle='arc3, rad = 0.3')
    #     plt.show()
    #     print("4 - networkx TSP")

    return

# create the animation object
ani = animation.FuncAnimation(fig, animate, frames=4, interval=3000, repeat=False)


# display the animation on screen in a popup window
plt.show()

# not set up correctly to work, animation does not include frame 0?
# ani.save('test.gif', writer='imagemagick', savefig_kwargs={'facecolor':'white'}, fps=0.5)