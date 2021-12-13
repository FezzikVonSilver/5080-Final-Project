import numpy as np
import networkx as nx
from networkx.convert_matrix import from_numpy_array
from networkx.algorithms.matching import max_weight_matching
# from min_span_tree import mst
"""
Return even degree vertices in graph G as list. (Chose Even instead of odd because easier to induce subgraph)
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

	#remove odd vertices from multigraph
    for odd_node in V:	
        G.remove_node(odd_node)
    return G 
"""
Networkx min-weight perfect matching, returns a set of paris of vertices
PARAMS- G: adjacency matrix
"""
def perfect_match(G):
	# G = np.array(G)
	# gnx = nx.Graph(from_numpy_array(G))

    #this command wouldn't run for me I think my python is old, but try on your comp 
	# gmin = min_weight_matching(gnx)
	if len(G.edges) == 0:
		return max_weight_matching(G)
    	    
	G_edges = G.edges(data="weight", default=1)
	min_weight = min([w for _, _, w in G_edges])
	InvG = nx.MultiGraph()
	edges = ((u, v, 1 / (1 + w - min_weight)) for u, v, w in G_edges)
	InvG.add_weighted_edges_from(edges, weight="weight")
	gmin = max_weight_matching(InvG)
		
	return gmin
"""
Add min-weight perfect matching to MST, returns the combined graph as a ndarray.
PARAMS- T:MST G:Original graph
"""
def combine(T,G):
    E = even_degree_vertices(T)
    S = induced_subgraph(E,G)
    M = perfect_match(S)

    for m in M:
        g_edge_weight = G.get_edge_data(m[0], m[1])[0]['weight']
        T.add_edge(m[0], m[1], weight=g_edge_weight)
    return T

# import random_metric_graph as rmg
# g = rmg.randCompleteMetricGraph(4)
# print("original graph: " + str(g.adj) + '\n')
# t =  mst(g)
# print("mst: " + str(t.adj) + '\n')
# eulerian_graph = combine(t, g)
# print("combined: " + str(eulerian_graph.adj) + '\n')