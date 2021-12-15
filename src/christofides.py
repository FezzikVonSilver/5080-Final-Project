
import random_metric_graph as rmg
from min_span_tree import mst
from combine import combine, span_root_example
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


# n = 10
G = span_root_example()

our_tour = our_christofides(G)
print(our_tour, "cost: " + str(get_cost(G, our_tour)))

# print(adj_matrix(our_tour,n))
# print(to_array(our_tour))

tour = christofides(G)
print(tour, "cost: " + str(get_cost(G, tour)))
# print(adj_matrix(tour,n))

def compare_costs(trials, n):
    same_cost = 0
    for _ in range(trials):
        G = rmg.randCompleteMetricGraph(n)
        tour = christofides(nx.Graph(G))
        tour_cost = get_cost(G, tour)
        our_tour = our_christofides(G)
        our_tour_cost = get_cost(G, our_tour)
        if tour_cost == our_tour_cost:
            same_cost += 1
        print(f"ours: {our_tour_cost}, theirs: {tour_cost}")
    return same_cost/trials

def test_tour(tour, G):
    assert tour[0] == tour[-1] == 0
    assert len(set(tour)) == len(G.nodes)

def compare_tours(tour1, tour2):
    assert tour1 == tour2 or tour1 == list(reversed(tour2))

# print(compare_costs(100, 10))

