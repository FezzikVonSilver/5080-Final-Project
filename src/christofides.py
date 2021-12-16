
import random_metric_graph as rmg
from min_span_tree import mst
from combine import combine
from create_tour import create_tour
import networkx as nx
import numpy as np
from networkx.algorithms.approximation.traveling_salesman import christofides
import matplotlib.pyplot as plt

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


# # n = 10
# G = span_root_example()

# our_tour = our_christofides(G)
# print(our_tour, "cost: " + str(get_cost(G, our_tour)))

# # print(adj_matrix(our_tour,n))
# # print(to_array(our_tour))

# tour = christofides(G)
# print(tour, "cost: " + str(get_cost(G, tour)))
# # print(adj_matrix(tour,n))

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


def span_root_example(): #creates an MST with root 0 having 3 edges
	example = [(0, 1, 2), (0, 2, 2), (0, 3, 1), (1, 2, 4), (1, 3, 2), (2, 3, 2)]
	newG = nx.Graph()
	newG.add_weighted_edges_from(example)
	return newG
	# print("g: " + str([(u,v,newG[u][v]['weight']) for u,v in newG.edges]))

def failing_k6_example():
    edges = [(0, 1, 570), (0, 2, 740), (0, 3, 170), 
    (0, 4, 290), (0, 5, 950), (1, 2, 377), 
    (1, 3, 480), (1, 4, 546), (1, 5, 376), 
    (2, 3, 581), (2, 4, 544), (2, 5, 510), 
    (3, 4, 149), (3, 5, 853), (4, 5, 901)]
    newG = nx.Graph()
    newG.add_weighted_edges_from(edges)
    return newG

def print_weighted_graph(name, g):
	print(f"{name}: {[(u,v,g[u][v]['weight']) for u,v in g.edges]}")

def print_weighted_multigraph(name, wg):
	print(f"{name}: ")
	for u,v,w in wg.edges:
		edge_data = wg.get_edge_data(u,v)
		print(f"{(u,v)}: {edge_data}")

# G = rmg.randCompleteMetricGraph(6)
# G = span_root_example()
# G = failing_k6_example()
# print_weighted_graph("G", G)
# T = mst(G)
# print_weighted_graph("T", T)
# M = combine(T, G)
# print_weighted_multigraph("M", M)
# our_tour = create_tour(M, G)
# print(create_tour(M, G), "cost: " + str(get_cost(G,our_tour)))
# nx_tour = christofides(G)
# print(nx_tour, "cost: " + str(get_cost(G,nx_tour)))
# weights = nx.get_edge_attributes(G,'weight')
# nx.draw(T, with_labels=True)
# plt.draw()
# plt.show()
