
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

if __name__ == 'main':
    G = rmg.randCompleteMetricGraph(5)
    print(our_christofides(G))