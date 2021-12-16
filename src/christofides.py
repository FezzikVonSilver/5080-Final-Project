
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

def get_cost(G, tour):
    cost = 0
    for i in range(0, len(tour)-1):
        u = tour[i]
        v = tour[i+1] 
        weight = G[u][v]['weight']
        cost += weight
    return cost

if __name__ == 'main':
    G = rmg.randCompleteMetricGraph(5)
    print(our_christofides(G))
