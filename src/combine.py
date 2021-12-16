from random import randbytes
from create_tour import create_tour
import numpy as np
import networkx as nx
from networkx.convert_matrix import from_numpy_array
from networkx.algorithms.matching import min_weight_matching
from min_span_tree import mst
import random_metric_graph as rmg

"""
Return even degree vertices in MST graph as list. (Chose Even instead of odd because easier to induce subgraph)
"""
def even_degree_vertices(G):
	V = []
	for node in G.nodes:
		count = 0
		for _ in G.neighbors(node):
			count += 1
		if count%2 == 0:
			V.append(node)
	return V

"""
Returns an induced subgraph containing vertices v in G-V. Has the same shape as
original graph G to keep track of nodes. Rows/columns of nodes v in V are 0. Return type is ndarray
PARAMS- V: vertices to exclude G: original graph
"""
def induced_subgraph(V,G):
    # if (len(V) == 0):
    #     return G
    # S = np.array(G)
    # S[V] = 0
    # S[:,V] = 0
    G = G.copy()

	#remove even vertices from multigraph
    for even_node in V:	
        G.remove_node(even_node)
    return G 
"""
Networkx min-weight perfect matching, returns a set of paris of vertices
PARAMS- G: adjacency matrix
"""
def perfect_match(G):
	# G = np.array(G)
	gnx = nx.Graph(G)

	return min_weight_matching(gnx)
"""
Add min-weight perfect matching to MST, returns the combined graph as a ndarray.
PARAMS- T:MST G:Original graph
"""
def combine(T,G):
    E = even_degree_vertices(T)
    S = induced_subgraph(E,G) #create graph composed of all edges (in whole graph), but only b/t the odd deg. nodes in MST
    # print("induced subgraph: " + str(S.edges))
    M = perfect_match(S) # get min perfect matching between those nodes
    # print("perfect match: " + str(M))

    combined_graph = nx.MultiGraph(T) # convert the MST to a multigraph
    # add edges from perfecting matching to the MST multigraph; 
	# if all edges are added, all nodes of the resulting graph should have even degree
    for edge in M:
        u, v = edge
        weight = G[u][v]['weight']
        combined_graph.add_edge(u, v, weight = weight)
    return combined_graph

def print_weighted_graph(name, g):
	print(f"{name}: {[(u,v,g[u][v]['weight']) for u,v in g.edges]}")

#main function
if __name__ == "__main__":
	g = rmg.randCompleteMetricGraph(4)
	print_weighted_graph("g", g)
	t =  mst(g)
	print_weighted_graph("mst", t)
	combined = combine(t, g)
	print(combined)	
