
import random_metric_graph as rmg
from min_span_tree import mst
from combine import combine
from create_tour import create_tour

def christofides(G):
    T = mst(G)
    M = combine(T, G)
    tsp_tour = create_tour(M, G)
    return tsp_tour

rand_graph = rmg.randCompleteMetricGraph(4)
tour = christofides(rand_graph)

print("total weight: " + str(tour.size(weight="weight")))