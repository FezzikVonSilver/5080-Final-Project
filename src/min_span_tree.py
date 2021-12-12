import math
import heapdict
import random as r
import numpy as np

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
	
	q = heapdict() #priority queue
	
	for i in range(len(G)): #initialize priority queue based on cost values
		q[i] = cost[i]
	

	
	while len(q) is not 0: #update cost and prev
		v,c = q.popitem()
		not_added = list(q.keys())
		for i in not_added:
			if G[v,i] is not 0:
				if cost[i] > G[v,i]:
					cost[i] = G[v,i]
					prev[i] = v
					q[i] = cost[i]
	return prev,cost

"""
Helper to construct tree. Returns ndarry adjacency matrix
"""
def construct_mst(prev,cost):
    mst = np.zeros((len(prev),len(prev)))
    for i in range(len(prev)):
        if prev[i] is not None:
            mst[prev[i],i] = cost[i]
            mst[i,prev[i]] = cost[i]
    return mst
		
	