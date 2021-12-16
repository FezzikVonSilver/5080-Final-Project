
import random_metric_graph as rmg
from min_span_tree import mst
from combine import combine
from create_tour import create_tour
import networkx as nx
import numpy as np
from networkx.algorithms.approximation.traveling_salesman import christofides


def our_christofides(G):
    T = mst(G)
    M = combine(T, G)
    tsp_tour = create_tour(M, G)
    return tsp_tour


#main function
if __name__ == "__main__":
    n = 5
    rand_graph = rmg.randCompleteMetricGraph(n)

    our_tour = our_christofides(rand_graph)
    print(our_tour)
    # print(adj_matrix(our_tour,n))
    # print(to_array(our_tour))

    tour = christofides(nx.Graph(rand_graph))
    print(tour)
    # print(adj_matrix(tour,n))
