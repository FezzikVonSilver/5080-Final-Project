import math
import heapdict as h
import random as r
import numpy as np
import networkx as nx
"""
Return's MST as ndarray
"""
def mst(g):
	prev, cost = find_mst(g)
	return construct_mst(prev,cost)

"""
Prim's Algoritm to find a MST
"""
def find_mst(G):
	cost = []
	prev = []
	
	for i in range(len(G)): #initialize cost and prev arrays
		cost.append(math.inf)
		prev.append(None)
	
	cost[0] = 0 #tree will always start from node 0
	
	q = h.heapdict() #priority queue
	
	for i in range(len(G)): #initialize priority queue based on cost values
		q[i] = cost[i]
	

	
	while len(q) != 0: #update cost and prev
		v,c = q.popitem()
		not_added = list(q.keys())
		for i in not_added:
			if G.has_edge(v, i):
				edge_weight = G.get_edge_data(v, i)[0]['weight']
				if cost[i] > edge_weight:
					cost[i] = edge_weight
					prev[i] = v
					q[i] = cost[i]
	return prev,cost

"""
Helper to construct tree. Returns networkx multigraph
"""
def construct_mst(prev,cost):
    mst = nx.MultiGraph()

    for i in range(len(prev)):
        mst.add_node(i)
        if prev[i] != None:
            if not mst.has_node(prev[i]):
                mst.add_node(prev[i])
            mst.add_edge(i, prev[i], weight=cost[i])
    return mst
		
	