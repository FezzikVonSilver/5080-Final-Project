
import random_metric_graph as rmg
from min_span_tree import mst
from combine import combine
from create_tour import create_tour
import networkx as nx
import numpy as np

def christofides(G):
    T = mst(G)
    M = combine(T, G)
    tsp_tour = create_tour(M, G)
    return tsp_tour
    
def adj_matrix(g,n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g.has_edge(i, j):
                # print("edge data: " + g.get_edge_data(i, j))
                weight = g.get_edge_data(i,j)[0]['weight']
                matrix[i][j] = weight
    return matrix

# n = 4
# rand_graph = rmg.randCompleteMetricGraph(n)
# print(adj_matrix(rand_graph,n))

# tour = christofides(rand_graph)
# print(adj_matrix(tour,n))
