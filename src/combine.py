import numpy as np
import networkx as nx
from networkx.convert_matrix import from_numpy_array
from networkx.algorithms.matching import max_weight_matching

"""
Return even degree vertices in graph G. (Chose Even instead of odd because easier to induce subgraph)
"""
def even_degree_vertices(G):
	V = []
	for i in range(len(G)):
		count = 0
		for j in range(len(G)):
			if G[i,j] > 0:
				count += 1
		if count%2 is 0:
			V.append(i)
	return V

"""
Returns an induced subgraph containing vertices v in G-V. Has the same shape as
original graph G to keep track of nodes. Rows/columns of nodes v in V are 0
PARAMS- V: vertices to exclude G: original graph
"""
def induced_subgraph(V,G):
    if (len(V) == 0):
        return G
    S = np.array(G)
    S[V] = 0
    S[:,V] = 0
    return S
"""
Networkx min-weight perfect matching, returns a set of paris of vertices
PARAMS- G: adjacency matrix
"""
def perfect_match(G):
	G = np.array(G)
	gnx = nx.Graph(from_numpy_array(G))
	
	if len(gnx.edges) == 0:
		return max_weight_matching(gnx)
    	    
	G_edges = gnx.edges(data="weight", default=1)
	min_weight = min([w for _, _, w in G_edges])
	InvG = nx.Graph()
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
        T[m[0],m[1]] = G[m[0],m[1]]
        T[m[1],m[0]] = G[m[1],m[0]]
    return T